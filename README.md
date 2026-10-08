# 🎓 Placify AI — Student Placement Prediction

> A professional academic Machine Learning application for estimating student placement outcomes using Decision Tree Classification.

**Final-release note:** Placify AI is an educational and portfolio project. The included dataset is synthetic/demo data, and model confidence is not a guarantee of actual placement.

**Author:** Nishita Patel
**Project type:** Machine Learning / Academic + Portfolio Project
**Primary stack:** Python, Streamlit, Pandas, NumPy, Scikit-learn, SQLAlchemy, PostgreSQL/SQLite

---

## 🌐 Live Project

**Project Website:**
https://nishpatel29.github.io/Placify-AI-Student-Placement-Prediction/

**Live Streamlit Application:**
https://nishpatel29-placify-ai-student-placement-prediction-app-oub93y.streamlit.app/

**GitHub Repository:**
https://github.com/nishpatel29/Placify-AI-Student-Placement-Prediction

---

## 📌 Overview

Placify AI is a student placement prediction application developed using Python, Streamlit, and Scikit-learn.

The application uses a Decision Tree Classification model to estimate whether a student profile is likely to be classified as **Placed** or **Not Placed** based on four demonstration inputs:

- CGPA
- Technical Skills Score
- Internship Experience
- Aptitude Score

In addition to the prediction, the application provides:

- Prediction probability
- Career-readiness indication
- Personalized improvement guidance
- Four-week improvement planning
- Model analytics
- Feature importance
- Decision Tree visualization
- Dataset overview
- User accounts
- User-specific prediction history
- Profile and prediction summary

---

## ✨ Features

### 🔐 Account System

- Sign up and login
- Salted PBKDF2-SHA256 password hashing
- Session-based authentication
- Logout functionality
- User-specific prediction history
- Account-specific data isolation
- Profile page
- Prediction summary

### 🤖 Machine Learning

- Decision Tree Classification
- Gini criterion
- Maximum tree depth: 5
- Minimum samples per leaf: 6
- Fixed random state: 42
- Placement classification
- Prediction probabilities
- Accuracy
- Precision
- Recall
- F1 score
- Feature importance
- Decision Tree visualization
- Model analytics

### 📊 Student Guidance

- Placement outcome estimate
- Career-readiness indicator
- Personalized improvement recommendations
- Four-week recovery plan
- Improvement planner
- Action-oriented guidance for students predicted as not placed

### 🗄️ Database

- SQLite support for local development
- PostgreSQL support for deployment
- SQLAlchemy database layer
- User account storage
- Prediction history storage
- Environment-based database configuration
- Production database connection through `DATABASE_URL`

### 🌐 Deployment

- Streamlit Community Cloud deployment
- Neon PostgreSQL production database
- GitHub Pages project website
- Website-to-app integration
- GitHub Actions deployment workflow
- Public GitHub repository

---

## 🧠 How It Works

```text
Student profile inputs
        ↓
CGPA
Technical Skills
Internship Experience
Aptitude Score
        ↓
Decision Tree Classifier
        ↓
Placed / Not Placed
        ↓
Prediction Probability
        ↓
Career Readiness
        ↓
Personalized Improvement Guidance
        ↓
Prediction saved to authenticated user's history
```

---

## 📥 Application Inputs

| Input            | Description                                            |
| ---------------- | ------------------------------------------------------ |
| CGPA             | Student's academic performance                         |
| Technical Skills | Demonstration score representing technical preparation |
| Internship       | Whether internship experience is present               |
| Aptitude         | Demonstration aptitude score                           |

## 📤 Application Outputs

The application provides:

- Placement prediction
- Prediction probability
- Career-readiness indication
- Improvement recommendations
- Prediction history
- Model analytics

---

## 🌳 Model Configuration

Placify AI uses a `DecisionTreeClassifier`.

Current configuration:

```text
criterion = "gini"
max_depth = 5
min_samples_leaf = 6
random_state = 42
```

The application also reports:

- Accuracy
- Precision
- Recall
- F1 score
- Feature importance

Model performance is dataset-specific and should not be interpreted as real-world placement accuracy.

---

## 📊 Dataset

The included placement dataset is **synthetic/demo data** created for academic demonstration.

It should **not** be interpreted as:

- Official college placement statistics
- Real institutional placement records
- A representative employment dataset
- Evidence of actual hiring outcomes

The project does not claim that its predictions represent real placement probabilities.

Dataset information and related project documentation are included in the repository.

---

## 🔐 Authentication and Data Management

Placify AI supports account-based functionality.

For local development, the application can use SQLite.

For production deployment, the application uses PostgreSQL through a managed database connection.

The database connection is configured through:

```text
DATABASE_URL
```

The actual production database credential must never be committed to GitHub.

User prediction history is associated with the authenticated account.

Local database files are excluded from Git using `.gitignore`.

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/nishpatel29/Placify-AI-Student-Placement-Prediction.git
cd Placify-AI-Student-Placement-Prediction
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
```

### 3. Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run the application

```powershell
streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

---

## 🗄️ PostgreSQL Configuration

Placify AI can use SQLite locally or PostgreSQL when a production-style database connection is provided.

The repository includes:

```text
.env.example
```

Example:

```text
DATABASE_URL=postgresql+psycopg://USERNAME:PASSWORD@HOST:5432/DATABASE
```

Do not replace the placeholder with a real production credential inside the repository.

For Streamlit Community Cloud, configure the actual database connection using the platform's secure secrets configuration.

---

## 📁 Project Structure

```text
Placify-AI-Student-Placement-Prediction/
│
├── .devcontainer/
├── .github/
├── .streamlit/
├── data/
├── docs/
├── model/
├── portfolio/
├── website/
│
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── LICENSE-DOCS.md
├── Project_Report_Content.txt
├── README.md
├── SECURITY.md
├── SETUP_NOTES.md
├── app.py
├── placement_data.csv
├── requirements.txt
└── train_model.py
```

---

## 📄 Important Files

| File                 | Purpose                                                          |
| -------------------- | ---------------------------------------------------------------- |
| `app.py`             | Main Streamlit application                                       |
| `train_model.py`     | Model training script                                            |
| `placement_data.csv` | Synthetic/demo placement dataset                                 |
| `requirements.txt`   | Python dependencies                                              |
| `README.md`          | Project documentation                                            |
| `SECURITY.md`        | Security policy                                                  |
| `LICENSE`            | MIT license for application source code                          |
| `LICENSE-DOCS.md`    | License information for original documentation/content           |
| `.env.example`       | Safe environment-variable template                               |
| `.gitignore`         | Prevents secrets, databases and local files from being committed |
| `website/`           | GitHub Pages project website                                     |
| `docs/`              | Supporting project documentation                                 |
| `model/`             | Model-related files                                              |
| `data/`              | Dataset/supporting data                                          |
| `portfolio/`         | Portfolio-related project material                               |

---

## 🛡️ Responsible Use

Placify AI is intended for educational and portfolio purposes.

A prediction from this application:

- Does not guarantee employment.
- Does not guarantee placement.
- Does not represent an official college assessment.
- Does not represent a real hiring decision.
- Must not be used as the sole basis for hiring.
- Must not be used as the sole basis for admissions.
- Must not be used as the sole basis for scholarships.
- Must not be used for other high-impact decisions affecting individuals.

A real institutional deployment would require authorized data, privacy safeguards, representative sampling, fairness evaluation, model validation, monitoring, and appropriate governance.

---

## 🔒 Security

The project includes security documentation covering:

- Password hashing
- Authentication
- User-specific prediction history
- Secret management
- PostgreSQL deployment
- SQLite local development
- Environment variables
- Sensitive-file protection
- Responsible vulnerability reporting

See:

`SECURITY.md`

Never commit:

```text
.env
.streamlit/secrets.toml
*.db
*.sqlite
*.sqlite3
```

or real credentials and private student information.

---

## 🌐 Deployment

### GitHub Pages

The static project website is deployed through GitHub Actions.

Website:

https://nishpatel29.github.io/Placify-AI-Student-Placement-Prediction/

### Streamlit Community Cloud

The interactive application is deployed through Streamlit Community Cloud.

Live application:

https://nishpatel29-placify-ai-student-placement-prediction-app-oub93y.streamlit.app/

### Production Database

The deployed application uses PostgreSQL through Neon.

Database credentials are stored outside the public repository using secure deployment configuration.

---

## 📜 Licensing

### Application Source Code

The Placify AI application source code is licensed under the:

**MIT License**

See:

`LICENSE`

### Original Documentation and Non-Code Content

Original documentation and non-code project content are licensed under:

**CC BY-NC 4.0**

See:

`LICENSE-DOCS.md`

### Dataset

Dataset terms are documented separately.

The included placement dataset is synthetic/demo data created for academic demonstration.

---

## 👤 Ownership

Copyright © 2026 Nishita Patel.

Placify AI is an original academic and portfolio project created by Nishita Patel.

The application source code is licensed under the MIT License.

Original documentation and non-code project content are licensed under CC BY-NC 4.0.

---

## 🤝 Contributing

Contributions should follow the guidelines in:

`CONTRIBUTING.md`

Please do not submit:

- Real student data
- Private information
- Credentials
- Database secrets
- Confidential institutional information

---

## 🚀 Future Improvements

Possible future improvements include:

- Additional verified datasets
- More machine-learning models
- Model comparison
- Cross-validation
- Fairness and bias evaluation
- More detailed analytics
- Improved explainability
- Automated testing
- Expanded student-career resources
- Enhanced production monitoring

These are future possibilities and are not required for the current academic release.

---

## 🎓 Academic / Portfolio Use

Placify AI was developed as an academic Machine Learning project and portfolio project to demonstrate practical skills in:

- Python
- Machine Learning
- Scikit-learn
- Streamlit
- Data handling
- SQLAlchemy
- SQLite
- PostgreSQL
- Authentication
- Git
- GitHub
- GitHub Pages
- Cloud deployment
- Responsible ML documentation

---

## 👩‍💻 Author

**Nishita Patel**

Computer Science & Engineering Student

Placify AI — Student Placement Prediction

---

## ⭐ Project Links

- **Live Website:** https://nishpatel29.github.io/Placify-AI-Student-Placement-Prediction/
- **Live Application:** https://nishpatel29-placify-ai-student-placement-prediction-app-oub93y.streamlit.app/
- **GitHub Repository:** https://github.com/nishpatel29/Placify-AI-Student-Placement-Prediction

---

## 📌 Final Release Note

Placify AI is considered an academic/portfolio release.

The application, authentication, database integration, deployment, documentation, security policy, GitHub repository, and project website have been prepared for demonstration and portfolio use.

**Model predictions are educational estimates and must not be treated as guaranteed placement outcomes.**
