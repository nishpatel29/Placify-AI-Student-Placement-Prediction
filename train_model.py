from pathlib import Path
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "placement_data.csv"
MODEL_DIR = BASE_DIR / "model"
MODEL_PATH = MODEL_DIR / "decision_tree_model.pkl"

# Copyright (c) 2026 Nishita Patel. Licensed under the MIT License.
# This file is part of the Placify AI academic/portfolio project.

df = pd.read_csv(DATA_PATH)
features = ["CGPA", "Technical_Skills_Score", "Internship_Experience", "Aptitude_Score"]
X = df[features]
y = df["Placement"]

Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    min_samples_leaf=6,
    random_state=42,
)
model.fit(Xtr, ytr)
pred = model.predict(Xte)

print("Accuracy:", round(accuracy_score(yte, pred) * 100, 2), "%")
print("Precision:", round(precision_score(yte, pred, pos_label="Placed") * 100, 2), "%")
print("Recall:", round(recall_score(yte, pred, pos_label="Placed") * 100, 2), "%")
print("F1:", round(f1_score(yte, pred, pos_label="Placed") * 100, 2), "%")

MODEL_DIR.mkdir(exist_ok=True)
with MODEL_PATH.open("wb") as f:
    pickle.dump(model, f)

print(f"Saved model to: {MODEL_PATH}")
