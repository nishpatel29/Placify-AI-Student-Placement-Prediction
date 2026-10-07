# Security Policy

## Scope

Placify AI is an academic/portfolio project. Please report security issues responsibly rather than publishing credentials or exploitable details in a public issue.

## Never commit

- passwords or password hashes from real users
- API keys, access tokens, GitHub tokens, or private keys
- `.env` files
- `.streamlit/secrets.toml`
- database credentials
- real student records or confidential college/company information

## Authentication security

Passwords entered into Placify AI are stored as salted PBKDF2-SHA256 password hashes, not plaintext passwords. Production deployments should use a managed PostgreSQL database and secure secret storage.

## If a secret is exposed

1. Revoke or rotate the exposed credential immediately.
2. Remove it from the working tree.
3. Check Git history for previous exposure.
4. Rotate any credentials that may have been derived from or connected to the exposed secret.
5. If necessary, rewrite Git history before making the repository public.

## Reporting

For a private security report, contact the repository owner through the contact method listed in the project profile. Do not include live credentials in a report.
