# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Nishita Patel
"""Placify AI — Student Placement Prediction."""

from __future__ import annotations

import hashlib
import hmac
import os
import secrets
from datetime import datetime, timezone
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from sqlalchemy import DateTime, Float, Integer, String, Text, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
import pickle

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "placement_data.csv"
MODEL_PATH = BASE_DIR / "model" / "decision_tree_model.pkl"
FEATURES = ["CGPA", "Technical_Skills_Score", "Internship_Experience", "Aptitude_Score"]

st.set_page_config(page_title="Placify AI", page_icon="🎓", layout="wide")


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    graduation_year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class Prediction(Base):
    __tablename__ = "predictions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, index=True)
    cgpa: Mapped[float] = mapped_column(Float)
    technical_skills: Mapped[float] = mapped_column(Float)
    internship: Mapped[int] = mapped_column(Integer)
    aptitude: Mapped[float] = mapped_column(Float)
    outcome: Mapped[str] = mapped_column(String(30))
    confidence: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    recommendation: Mapped[str | None] = mapped_column(Text, nullable=True)


@st.cache_resource
def get_engine():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        try:
            database_url = st.secrets.get("DATABASE_URL")
        except Exception:
            database_url = None
    database_url = database_url or "sqlite:///placify.db"
    # Streamlit/hosted PostgreSQL providers may expose postgres:// URLs.
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql+psycopg://", 1)
    elif database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+psycopg://", 1)
    return create_engine(database_url, pool_pre_ping=True)


@st.cache_resource
def initialize_database():
    engine = get_engine()
    Base.metadata.create_all(engine)
    return engine


def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 310_000)
    return f"pbkdf2_sha256$310000${salt.hex()}${digest.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        algorithm, rounds, salt_hex, digest_hex = stored.split("$")
        if algorithm != "pbkdf2_sha256":
            return False
        digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt_hex), int(rounds))
        return hmac.compare_digest(digest.hex(), digest_hex)
    except (ValueError, TypeError):
        return False


def valid_email(email: str) -> bool:
    return "@" in email and "." in email.rsplit("@", 1)[-1] and " " not in email


def load_model_and_data():
    df = pd.read_csv(DATA_PATH)
    with MODEL_PATH.open("rb") as file:
        model = pickle.load(file)
    return df, model


def model_metrics(df, model):
    x = df[FEATURES]
    y = df["Placement"]
    _, x_test, _, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)
    pred = model.predict(x_test)
    return [
        accuracy_score(y_test, pred),
        precision_score(y_test, pred, pos_label="Placed"),
        recall_score(y_test, pred, pos_label="Placed"),
        f1_score(y_test, pred, pos_label="Placed"),
    ]


def save_prediction(user_id, values, outcome, confidence, recommendation):
    engine = initialize_database()
    with Session(engine) as session:
        session.add(Prediction(user_id=user_id, **values, outcome=outcome, confidence=confidence, recommendation=recommendation))
        session.commit()


def get_history(user_id):
    engine = initialize_database()
    with Session(engine) as session:
        rows = session.scalars(
            select(Prediction).where(Prediction.user_id == user_id).order_by(Prediction.created_at.desc())
        ).all()
        return rows


def recommendations(cgpa, skills, aptitude, internship):
    gaps = []
    if cgpa < 7:
        gaps.append("Improve academic performance and maintain a stronger CGPA.")
    if skills < 70:
        gaps.append("Build practical technical skills through projects and regular practice.")
    if aptitude < 70:
        gaps.append("Practice quantitative, logical and verbal aptitude.")
    if not internship:
        gaps.append("Try to obtain internship, virtual internship or relevant project experience.")
    if not gaps:
        gaps.append("Strengthen communication, resume quality and company-specific preparation.")
    return gaps


# ---------- Styling ----------
st.markdown(
    """<style>
    .block-container{max-width:1250px;padding-top:2rem}
    .hero{padding:28px;border-radius:20px;background:linear-gradient(135deg,#102a43,#1f5f8b);color:white;margin-bottom:22px}
    .hero h1{font-size:42px;margin:0}.card{padding:18px;border-radius:16px;background:white;border:1px solid #e5e7eb}
    .result{padding:22px;border-radius:18px;background:#eef6ff;border-left:7px solid #1976d2}
    .warning{padding:22px;border-radius:18px;background:#fff8e6;border-left:7px solid #f0a500;color:#3b2a00}
    .warning h2,.warning p{color:#3b2a00}
    .success{padding:22px;border-radius:18px;background:#edf9f0;border-left:7px solid #2e8b57;color:#16351f}
    .success h2,.success p{color:#16351f}
    </style>""",
    unsafe_allow_html=True,
)

try:
    df, model = load_model_and_data()
    metrics = model_metrics(df, model)
except Exception as exc:
    st.error(f"Placify AI could not load its model/data: {exc}")
    st.stop()

# ---------- Authentication ----------
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "user_name" not in st.session_state:
    st.session_state.user_name = None

if st.session_state.user_id is None:
    st.markdown('<div class="hero"><h1>🎓 Placify AI</h1><p>Student Placement Prediction & Career Readiness Dashboard</p></div>', unsafe_allow_html=True)
    login_tab, signup_tab = st.tabs(["🔐 Login", "✨ Create Account"])

    with login_tab:
        st.subheader("Welcome back")
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login", type="primary", width="stretch")
        if submitted:
            if not valid_email(email) or not password:
                st.error("Enter a valid email and password.")
            else:
                try:
                    engine = initialize_database()
                    with Session(engine) as session:
                        user = session.scalar(select(User).where(User.email == email.strip().lower()))
                        if user and verify_password(password, user.password_hash):
                            st.session_state.user_id = user.id
                            st.session_state.user_name = user.name
                            st.rerun()
                        st.error("Invalid email or password.")
                except Exception:
                    st.error("Login could not be completed. Check the database configuration and try again.")

    with signup_tab:
        st.subheader("Create your Placify AI account")
        with st.form("signup_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            confirm = st.text_input("Confirm Password", type="password")
            graduation = st.number_input("Graduation Year (optional)", min_value=2020, max_value=2100, value=2027, step=1)
            accepted = st.checkbox("I understand that Placify AI provides educational model estimates and is not a hiring or placement decision system.")
            submitted = st.form_submit_button("Create Account", type="primary", width="stretch")
        if submitted:
            if not name.strip() or not valid_email(email):
                st.error("Please enter a valid name and email.")
            elif len(password) < 8:
                st.error("Password must contain at least 8 characters.")
            elif password != confirm:
                st.error("Passwords do not match.")
            elif not accepted:
                st.error("Please acknowledge the responsible-use statement.")
            else:
                try:
                    engine = initialize_database()
                    with Session(engine) as session:
                        normalized = email.strip().lower()
                        existing = session.scalar(select(User).where(User.email == normalized))
                        if existing:
                            st.error("An account with this email already exists. Please log in.")
                        else:
                            user = User(name=name.strip(), email=normalized, password_hash=hash_password(password), graduation_year=int(graduation))
                            session.add(user)
                            session.commit()
                            st.success("Account created successfully. You can now log in.")
                except Exception:
                    st.error("Account creation could not be completed. Check the database configuration and try again.")

    st.info("Local development uses a project-local SQLite database by default. For hosted deployment, set DATABASE_URL to a PostgreSQL database connection string.")
    st.caption("Placify AI • Code: MIT License • Documentation/content: CC BY-NC 4.0")
    st.stop()

# ---------- Authenticated application ----------
with st.sidebar:
    st.title("🎓 Placify AI")
    st.caption(f"Welcome, {st.session_state.user_name}")
    page = st.radio("Navigate", ["🏠 Prediction", "📜 My History", "📊 Model Analytics", "🚀 Improvement Plan", "👤 Profile", "ℹ️ About"])
    st.divider()
    if st.button("Logout", width="stretch"):
        st.session_state.user_id = None
        st.session_state.user_name = None
        st.rerun()

st.markdown('<div class="hero"><h1>🎓 Placify AI</h1><p>Student Placement Prediction & Career Readiness Dashboard</p></div>', unsafe_allow_html=True)

if page == "🏠 Prediction":
    st.subheader("Predict Placement Outcome")
    st.caption("Academic demonstration using the included synthetic/demo dataset. Predictions are estimates, not placement guarantees.")
    a, b = st.columns(2)
    with a:
        cgpa = st.slider("CGPA", 5.0, 10.0, 7.0, 0.01)
        skills = st.slider("Technical Skills Score", 35.0, 100.0, 70.0, 1.0)
    with b:
        intern = st.selectbox("Internship Experience", ["No", "Yes"])
        apt = st.slider("Aptitude Score", 35.0, 100.0, 70.0, 1.0)

    if st.button("🔍 Predict Placement", width="stretch", type="primary"):
        internship_value = int(intern == "Yes")
        row = pd.DataFrame([{"CGPA": cgpa, "Technical_Skills_Score": skills, "Internship_Experience": internship_value, "Aptitude_Score": apt}])
        pred = model.predict(row)[0]
        probs = model.predict_proba(row)[0]
        classes = list(model.classes_)
        conf = float(probs[classes.index(pred)] * 100)
        gaps = recommendations(cgpa, skills, apt, internship_value)
        recommendation = " ".join(gaps)
        values = {"cgpa": cgpa, "technical_skills": skills, "internship": internship_value, "aptitude": apt}
        try:
            save_prediction(st.session_state.user_id, values, pred, conf, recommendation)
            st.success("Prediction saved to your history.")
        except Exception:
            st.warning("Prediction was generated, but it could not be saved to history. Check the database configuration.")

        confidence_note = (
            "This is the model's confidence for the predicted class based on patterns learned from the training data. "
            "It does not guarantee actual placement."
        )
        if pred == "Placed":
            st.markdown(
                f'<div class="success"><h2>✅ Predicted Outcome: PLACED</h2>'
                f'<p><b>Model confidence:</b> {conf:.1f}%</p>'
                f'<p><b>Conclusion:</b> The current profile matches patterns learned by the model.</p>'
                f'<p><b>Important:</b> {confidence_note}</p></div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="warning"><h2>⚠️ Predicted Outcome: NOT PLACED</h2>'
                f'<p><b>Model confidence:</b> {conf:.1f}%</p>'
                f'<p><b>Conclusion:</b> The current profile may need improvement in one or more placement-related areas.</p>'
                f'<p><b>Important:</b> {confidence_note}</p></div>',
                unsafe_allow_html=True,
            )
            st.markdown("### 🎯 What should the student do next?")
            for gap in gaps:
                st.write("•", gap)
            st.markdown("### 📅 4-Week Recovery Plan")
            for week, plan in {
                "Week 1": "Identify weak areas, update resume and start aptitude practice.",
                "Week 2": "Complete one practical technical mini-project.",
                "Week 3": "Do mock interviews and company-style aptitude tests.",
                "Week 4": "Apply consistently, revise interview topics and track applications.",
            }.items():
                st.info(f"**{week}:** {plan}")

        st.markdown("### 📈 Prediction Probability")
        st.bar_chart(pd.DataFrame({"Probability": probs * 100}, index=classes))
        readiness = float(np.mean([min(cgpa / 8.5, 1), skills / 100, apt / 100, internship_value]) * 100)
        st.markdown("### 🧭 Career Readiness Snapshot")
        st.progress(int(readiness))
        st.write(f"Profile readiness indicator: **{readiness:.0f}%**")

elif page == "📜 My History":
    st.subheader("📜 My Prediction History")
    history = get_history(st.session_state.user_id)
    if not history:
        st.info("You have not made a prediction yet.")
    else:
        table = pd.DataFrame([{
            "Date": item.created_at.strftime("%Y-%m-%d %H:%M") if item.created_at else "",
            "CGPA": item.cgpa,
            "Skills": item.technical_skills,
            "Internship": "Yes" if item.internship else "No",
            "Aptitude": item.aptitude,
            "Outcome": item.outcome,
            "Confidence": f"{item.confidence:.1f}%",
        } for item in history])
        st.dataframe(table, width="stretch", hide_index=True)
        st.caption("History is associated with your account. Do not enter sensitive personal information into prediction fields.")

elif page == "📊 Model Analytics":
    st.subheader("Model Performance & Explainability")
    cols = st.columns(4)
    for col, name, value in zip(cols, ["Accuracy", "Precision", "Recall", "F1 Score"], metrics):
        col.metric(name, f"{value * 100:.1f}%")
    st.info("The model was trained and evaluated on the included synthetic/demo dataset. These metrics describe this dataset and are not evidence of real-world placement performance.")
    st.markdown("### Feature Importance")
    display_feature_names = {
        "CGPA": "CGPA",
        "Technical_Skills_Score": "Technical Skills Score",
        "Internship_Experience": "Internship Experience",
        "Aptitude_Score": "Aptitude Score",
    }
    imp = pd.DataFrame({"Importance": model.feature_importances_}, index=[display_feature_names[x] for x in FEATURES]).sort_values("Importance")
    st.bar_chart(imp)
    st.markdown("### Decision Tree")
    st.caption("Each node represents a decision rule learned from the training data. Leaf nodes show the resulting predicted class. The full tree is displayed for model explainability.")
    fig, ax = plt.subplots(figsize=(16, 8))
    plot_tree(model, feature_names=[display_feature_names[x] for x in FEATURES], class_names=model.classes_, filled=True, rounded=True, fontsize=8, ax=ax)
    st.pyplot(fig)
    plt.close(fig)
    st.markdown("### Dataset Overview")
    st.caption("Synthetic/demo data for academic demonstration only — not official institutional placement data.")
    display_df = df.head(12).copy()
    display_df["Internship_Experience"] = display_df["Internship_Experience"].map({0: "No", 1: "Yes"})
    display_df["Placement"] = display_df["Placement"].astype(str)
    st.dataframe(display_df, width="stretch", hide_index=True)
    st.caption("Metrics are based on the project's fixed 80/20 stratified holdout split and are dataset-specific.")

elif page == "🚀 Improvement Plan":
    st.subheader("Placement Improvement Planner")
    areas = {
        "📚 Academics": ["Track CGPA subject-wise", "Complete assignments on time", "Work on weak subjects"],
        "💻 Technical Skills": ["Build 2–3 practical projects", "Practice SQL/Python", "Develop one analytics/BI tool deeply"],
        "🧠 Aptitude": ["Practice 20–30 questions daily", "Track accuracy and time", "Revise weak topics"],
        "🏢 Experience": ["Apply for internships", "Take relevant virtual internships", "Document projects"],
        "🎤 Interview": ["Practice HR questions", "Do mock technical interviews", "Improve communication"],
        "📄 Resume & Applications": ["Tailor resume to roles", "Maintain application tracker", "Apply consistently"],
    }
    for title, items in areas.items():
        with st.expander(title):
            for item in items:
                st.write("•", item)

elif page == "👤 Profile":
    st.subheader("👤 My Profile")
    engine = initialize_database()
    with Session(engine) as session:
        user = session.get(User, st.session_state.user_id)
        if user:
            history_count = session.query(Prediction).filter(Prediction.user_id == user.id).count()
            latest = session.scalars(
                select(Prediction).where(Prediction.user_id == user.id).order_by(Prediction.created_at.desc())
            ).first()
            profile_cols = st.columns(2)
            with profile_cols[0]:
                st.markdown("### 👤 Account Details")
                st.write(f"**Name:** {user.name}")
                st.write(f"**Email:** {user.email}")
                st.write(f"**Graduation Year:** {user.graduation_year or 'Not specified'}")
                st.write(f"**Account Created:** {user.created_at.strftime('%Y-%m-%d') if user.created_at else '—'}")
            with profile_cols[1]:
                st.markdown("### 📊 Prediction Summary")
                st.metric("Total Predictions", history_count)
                if latest:
                    st.metric("Latest Outcome", latest.outcome)
                    st.caption(f"Latest model confidence: {latest.confidence:.1f}%")
                else:
                    st.caption("No predictions yet. Make your first prediction from the Prediction page.")

else:
    st.subheader("About Placify AI")
    st.write("Placify AI is an academic Machine Learning application for Student Placement Prediction using Decision Tree Classification.")
    st.markdown("**Technology:** Python • Streamlit • Pandas • NumPy • Scikit-learn • Matplotlib • SQLAlchemy • PostgreSQL/SQLite")
    st.markdown("**Inputs:** CGPA, Technical Skills Score, Internship Experience, Aptitude Score")
    st.markdown("**Outputs:** Placed/Not Placed, confidence, probability, improvement guidance and personal prediction history.")
    st.info("The included dataset is synthetic/demo data and is not official institutional placement data. It must not be interpreted as real placement statistics.")
    st.warning("Responsible use: this educational model is a demonstration only. Its predictions do not guarantee placement and must not be used as the sole basis for hiring, admissions, scholarships, employment, or other high-impact decisions.")
    st.markdown("### Licensing")
    st.write("Application code is licensed under the MIT License. Original documentation and project content are licensed under CC BY-NC 4.0. Dataset licensing/provenance is documented separately.")
    st.markdown("### Ownership")
    st.write("Copyright © 2026 Nishita Patel. See LICENSE and LICENSE-DOCS.md for the applicable permissions.")
