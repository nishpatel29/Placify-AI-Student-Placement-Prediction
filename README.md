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

### 📊 Student guidance

- Placement outcome estimate
- Career readiness indicator
- Personalized improvement recommendations
- Four-week recovery plan
- Improvement planner

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
```

## Dataset

The repository currently contains a **synthetic/demo dataset** created for this academic application. It is **not official institutional placement data** and must not be presented as real placement statistics.

A suitable authoritative public placement dataset was not identified that both matches this application's four-feature schema and provides clear permission for redistribution in this repository. Therefore, this project does **not** falsely label a third-party dataset as “official.”

See [`docs/DATA_AND_MODEL.md`](docs/DATA_AND_MODEL.md) and [`data/DATASET.md`](data/DATASET.md).

## Database and authentication

The app uses SQLAlchemy and supports:

- **Local development:** SQLite (`placify.db` is created automatically and ignored by Git).
- **Hosted deployment:** PostgreSQL using `DATABASE_URL` stored as a deployment secret.

Example PostgreSQL connection format:

```text
postgresql+psycopg://USERNAME:PASSWORD@HOST:5432/DATABASE
```

Do not put a real password in source code or commit it to GitHub.

## Run locally

From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python train_model.py
python -m streamlit run app.py
```

The first local run creates `placify.db` automatically. The file is ignored by Git.

## PostgreSQL setup

For production-like local testing, create a PostgreSQL database and set:

```powershell
$env:DATABASE_URL="postgresql+psycopg://USERNAME:PASSWORD@HOST:5432/DATABASE"
python -m streamlit run app.py
```

For Streamlit hosting, store the connection string as a secret named `DATABASE_URL` instead of committing it.

## Project structure

```text
Placify-AI-Student-Placement-Prediction/
├── app.py
├── train_model.py
├── placement_data.csv
├── model/
│   └── decision_tree_model.pkl
├── data/
│   └── DATASET.md
├── docs/
│   ├── DATA_AND_MODEL.md
│   ├── DEPLOYMENT.md
│   ├── GITHUB_SETUP.md
│   └── LOCAL_CLONE_ISOLATION.md
├── website/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── portfolio/
│   └── placify-project-section.html
├── .github/
│   └── workflows/deploy-pages.yml
├── LICENSE
├── LICENSE-DOCS.md
├── SECURITY.md
├── CONTRIBUTING.md
├── requirements.txt
└── .gitignore
```

## Responsible ML

The included model is dataset-specific. For a real institutional system, authorized data governance, privacy review, representative sampling, cross-validation, fairness evaluation, class-imbalance analysis, calibration, monitoring, and independent validation would be required.

The application should be treated as an **educational decision-support demonstration**, not as an automated decision-maker.

## Security

Never commit:

- passwords
- database credentials
- API keys or tokens
- `.env` files
- `.streamlit/secrets.toml`
- real student records
- confidential college/company data

See [`SECURITY.md`](SECURITY.md).

## Licensing

### Application source code

The Placify AI application source code is licensed under the **MIT License**. See [`LICENSE`](LICENSE).

This permits use, copying, modification, distribution, sublicensing and commercial use, subject to the MIT license conditions.

### Documentation and original project content

Unless otherwise stated, original documentation and original non-code project content are licensed under **CC BY-NC 4.0**. See [`LICENSE-DOCS.md`](LICENSE-DOCS.md).

### Dataset

Dataset provenance and applicable terms are documented separately in [`data/DATASET.md`](data/DATASET.md).

## Ownership

Copyright © 2026 Nishita Patel.

The code and documentation have the separate licenses described above. Do not remove attribution or misrepresent Nishita Patel's original project work.

## Deployment

- [GitHub setup](docs/GITHUB_SETUP.md)
- [Deployment guide](docs/DEPLOYMENT.md)
- [Data and model documentation](docs/DATA_AND_MODEL.md)
- [Local clone isolation](docs/LOCAL_CLONE_ISOLATION.md)

## Project website

The static project website is in `website/` and can be published through GitHub Pages. After creating the repository and deploying the Streamlit app, update the three URLs in `website/script.js`.

## Author

**Nishita Patel**  
Placify AI — Student Placement Prediction
