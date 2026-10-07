# Placify AI Setup Notes

This repository is the official GitHub/portfolio packaging of the same Placify AI application. It keeps the Decision Tree placement-prediction model and adds authentication, user prediction history, database support, security documentation, licensing, project website, and deployment guidance.

## Before publishing

Run the application locally and inspect the repository:

```powershell
git status
git diff
git ls-files
```

Never commit secrets, `.env`, `.streamlit/secrets.toml`, private keys, credentials, SQLite databases, or real student personal records.

## Database

Local development defaults to SQLite and creates `placify.db` automatically. For a production deployment, configure `DATABASE_URL` for PostgreSQL through a secret/environment variable.

## Update website URLs

Edit `website/script.js` and replace the GitHub, Streamlit and portfolio placeholders after those URLs exist.

Edit `portfolio/placify-project-section.html` and replace its three placeholder URLs.

## Local clone isolation

If this repository is one of several local clones, change `.streamlit/config.toml` to a unique local port and keep a separate `.venv` for the clone. See `docs/LOCAL_CLONE_ISOLATION.md`.

## Licensing

- Application source code: MIT License (`LICENSE`).
- Original documentation/non-code project content: CC BY-NC 4.0 (`LICENSE-DOCS.md`).
- Dataset: see `data/DATASET.md`.

Public visibility does not remove attribution requirements applicable to documentation/content, and it does not make the dataset “official.”


## Final release checklist

Before publishing the repository:

1. Run `python train_model.py` and confirm the model file is regenerated successfully.
2. Run `python -m py_compile app.py train_model.py`.
3. Run the Streamlit app and test sign-up, login, prediction, history, profile, analytics, improvement plan, about, and logout.
4. Create a second test account and confirm prediction history is isolated per user.
5. Confirm no `.env`, `placify.db`, `.streamlit/secrets.toml`, `.venv`, credentials, tokens, or real student records are tracked.
6. Update the URLs in `website/script.js` and `portfolio/placify-project-section.html` after the real deployment URLs exist.
7. Use PostgreSQL for hosted deployment rather than the local SQLite fallback.
