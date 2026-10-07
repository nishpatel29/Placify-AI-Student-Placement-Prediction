# GitHub Setup

## Repository

Recommended public repository name:

`Placify-AI-Student-Placement-Prediction`

Recommended topics:

`machine-learning`, `student-placement`, `decision-tree`, `scikit-learn`, `streamlit`, `python`, `data-analytics`

## Before the first push

Run locally and confirm the app works. Then check:

```powershell
git status
git diff
git ls-files
```

Make sure there are no secrets, `.venv`, SQLite databases, private datasets, or personal student records.

## Create the repository

Create a **public** GitHub repository with the recommended name. Do not select another license during repository creation; the repository already contains the correct `LICENSE` file.

## First push

From the project root:

```powershell
git init
git branch -M main
git add .
git status
git commit -m "feat: publish Placify AI student placement prediction"
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## After publishing

Check that:

- README renders correctly;
- `LICENSE` is present;
- `LICENSE-DOCS.md` is present;
- `SECURITY.md` is present;
- `.gitignore` is present;
- no secrets appear;
- no `placify.db` appears;
- author attribution is visible;
- website links no longer contain placeholders.

For a public repository, enable GitHub security features such as secret scanning/push protection and Dependabot where available.

## Licensing summary

- Source code: MIT.
- Original documentation/non-code content: CC BY-NC 4.0 unless otherwise stated.
- Dataset: see `data/DATASET.md`.
