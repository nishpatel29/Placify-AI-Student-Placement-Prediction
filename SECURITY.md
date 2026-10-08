# Security Policy

## Overview

Placify AI is an academic and portfolio project that includes user authentication, prediction history, and database-backed application features.

Security is treated as an important part of the project, especially because the application handles account credentials and student-related prediction inputs.

Please report security issues responsibly rather than publishing credentials, personal information, or exploitable details in a public issue.

---

## Scope

This security policy applies to:

- The Placify AI Streamlit application
- Authentication and account management
- Prediction history and user-specific data
- Local SQLite database usage
- Deployed PostgreSQL database usage
- Environment variables and application secrets
- Repository and deployment configuration
- Project documentation and supporting files

The included placement dataset is synthetic/demo data and does not represent real institutional placement records.

---

## Never Commit Sensitive Information

Never commit or publish:

- Plaintext passwords
- Real user passwords or password hashes
- API keys
- Access tokens
- GitHub tokens
- Private keys
- Database credentials
- PostgreSQL connection strings containing credentials
- `.env` files
- `.streamlit/secrets.toml`
- Streamlit deployment secrets
- Real student records
- Personally identifiable student information
- Confidential college or company information
- Production database exports containing private information
- Authentication/session secrets

Use `.env.example` only for documenting required environment-variable names and safe placeholder values.

---

## Authentication Security

Placify AI does not store user passwords as plaintext.

Passwords entered by users are processed using salted PBKDF2-SHA256 password hashing before being stored.

The application uses authentication and session handling to restrict account-specific functionality.

Prediction history is associated with the authenticated user so that users should only access their own saved prediction records through the application.

For production deployments, database credentials and other sensitive configuration values should be stored using the deployment platform's secure secret-management mechanism rather than committed to source control.

---

## Database Security

### Local Development

Local development can use SQLite for convenience.

Local SQLite database files are ignored by Git using the repository's `.gitignore` configuration.

Examples of ignored local database files include:

```text
*.db
*.sqlite
*.sqlite3
```
