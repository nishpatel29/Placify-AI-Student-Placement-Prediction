# 🎓 Placify AI — Student Placement Prediction

> **A professional academic Machine Learning application for estimating student placement outcomes using Decision Tree Classification.**
>
> **Final-release note:** The included model and dataset are for academic demonstration. Model confidence is not a guarantee of actual placement.

**Author:** Nishita Patel  
**Project type:** Machine Learning / Academic + Portfolio Project  
**Primary stack:** Python, Streamlit, Pandas, NumPy, Scikit-learn, SQLAlchemy, PostgreSQL/SQLite

## Overview

Placify AI takes four demonstration placement-readiness inputs:

- CGPA
- Technical Skills Score
- Internship Experience
- Aptitude Score

It produces an estimated **Placed / Not Placed** outcome with class probability, a career-readiness indicator, actionable improvement guidance, and a personal prediction history after login.

> **Important:** Placify AI is an educational machine-learning application. A prediction is not a guarantee of employment or placement and must not be used as the sole basis for hiring, admissions, scholarships, employment, or other high-impact decisions.

## Features

### 🔐 Account system

- Sign up and login
- Salted PBKDF2-SHA256 password hashing
- Session-based access in Streamlit
- PostgreSQL support for deployment
- SQLite fallback for local development
- User-specific prediction history
- Profile page
- Logout functionality
- Account-specific data isolation

### 🤖 Machine Learning

- Decision Tree Classification
- Gini criterion
- Maximum depth: 5
- Minimum samples per leaf: 6
- Fixed random state: 42
- Accuracy, precision, recall and F1 score
- Feature importance
- Decision-tree visualization
- Prediction probabilities
- Model analytics and dataset overview

### 📊 Student guidance

- Placement outcome estimate
- Career readiness indicator
- Personalized improvement recommendations
- Four-week recovery plan
- Improvement planner
- Action-oriented guidance for students predicted as not placed

### 🌐 Deployment

- Streamlit Community Cloud deployment
- PostgreSQL database support through Neon
- SQLite fallback for local development
- GitHub Pages project website
- Direct Launch Live App integration
- GitHub-ready project structure
- Environment-based database configuration

## How it works

```text
Student inputs
     ↓
CGPA + Technical Skills + Internship + Aptitude
     ↓
Decision Tree Classifier
     ↓
Placement estimate + probability
     ↓
Personalized improvement guidance
     ↓
Prediction saved to authenticated user's history
