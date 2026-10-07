# Deployment

## A. Streamlit Community Cloud

1. Push the repository to GitHub.
2. Sign in to Streamlit Community Cloud with GitHub.
3. Create an app from the public repository.
4. Select branch `main`.
5. Set the main file to `app.py`.
6. Add a secret named `DATABASE_URL` containing your production PostgreSQL connection string.
7. Deploy.
8. Test sign-up, login, prediction, history, logout, and model analytics.

Example secret value format:

```text
postgresql+psycopg://USERNAME:PASSWORD@HOST:5432/DATABASE
```

Do **not** put this value in GitHub source files.

## B. PostgreSQL

A production deployment should use a managed PostgreSQL service with encrypted connections and a restricted database user. Create a dedicated database for Placify AI rather than sharing unrelated application credentials.

The application automatically creates the required `users` and `predictions` tables when it starts.

## C. GitHub Pages project website

The `website/` directory is deployed by `.github/workflows/deploy-pages.yml`.

After pushing the repository:

1. Open repository **Settings → Pages**.
2. Select **GitHub Actions** as the deployment source.
3. Run the Pages workflow or push to `main`.
4. Update `website/script.js` with the real GitHub, Streamlit, and portfolio URLs before the final deployment.

## D. Personal portfolio

Add `portfolio/placify-project-section.html` to the existing portfolio and replace its placeholder URLs.

## Final security check

Before making the project public:

- never commit `.env`;
- never commit `.streamlit/secrets.toml`;
- never commit database passwords;
- never commit API tokens;
- never commit `placify.db`;
- never upload real student records;
- inspect public Git history for accidental secrets.
