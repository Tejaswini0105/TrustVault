# TrustVault


TrustVault is a Flask-based secure document-sharing prototype. It demonstrates authenticated users, per-document read/edit grants, private file storage, revocation, and application audit events.

## Important security status

This is a starter/demo implementation, **not a production-certified secure document platform**. Before using real confidential files, address the limitations in `THREATS.md`, run the tests, and arrange an independent security review. Audit hash chaining in this prototype is not independently tamper-proof. File validation is not malware scanning. Administrators can view audit metadata but do not automatically get document-content access.

## Requirements

- Python 3.11 or newer
- pip
- SQLite for local development (default); MySQL can be configured using `DATABASE_URL`

## Run locally (clean clone)

```bash
python -m venv venv
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
python app.py
```

Open http://127.0.0.1:5000. Set a strong random `SECRET_KEY` in `.env` before deployment. The local development server must not be exposed publicly.

## Demo accounts

Create the synthetic demo accounts by running:

```bash
python scripts/seed_demo.py
```

- Admin: `admin@trustvault.local` / `DemoAdminPassword!2026`
- Owner: `owner@trustvault.local` / `DemoOwnerPassword!2026`
- Viewer: `viewer@trustvault.local` / `DemoViewerPassword!2026`

These are **local demonstration credentials only**. Do not deploy them publicly or reuse them for production. Before public deployment, use a one-time seed process with newly generated credentials and remove/disable the seed accounts afterward.

## Tests

```bash
pytest -q
```

## Database

SQLite is the default for easy local setup. To use MySQL, create a database and dedicated least-privilege user, then set `DATABASE_URL` in the environment, e.g. `mysql+pymysql://USER:PASSWORD@HOST/trustvault`. Do not commit credentials. For a serious deployment, use Flask-Migrate migrations rather than relying on `create_all()`.

## API / route access summary

| Route | Methods | Access |
|---|---|---|
| `/` | GET | Public |
| `/register` | GET, POST | Public; cannot create admin |
| `/login` | GET, POST | Public |
| `/logout` | POST | Authenticated |
| `/dashboard` | GET | Authenticated; lists owned/shared docs |
| `/documents/upload` | GET, POST | Owner/Admin |
| `/documents/<id>` | GET | Owner or active Read/Edit grant |
| `/documents/<id>/download` | GET | Owner or active Read/Edit grant |
| `/documents/<id>/edit` | GET, POST | Owner or active Edit grant |
| `/documents/<id>/delete` | POST | Document owner only |
| `/documents/<id>/share` | GET, POST | Document owner |
| `/documents/<id>/revoke/<user_id>` | POST | Document owner |
| `/search` | GET | Authenticated; results restricted to owned/shared docs |
| `/admin/audit` | GET | Admin |
| `/admin/users` | GET, POST | Admin |

## Deployment notes

Use a production WSGI server such as Gunicorn, HTTPS, `COOKIE_SECURE=1`, strong secrets, a managed database, private persistent storage, backups, monitoring, and a separate protected audit destination. Configure CSRF protection, upload limits, rate limits, and security headers. Do not deploy the development server with debug enabled.

## Submission artefacts

- `THREATS.md`: threat model and known gaps
- `PROMPTS.md`: honest dated AI usage notes, with real commits and verification
- `tests/`: automated security tests
- Five-minute demo video: record only synthetic data

TrustVault is a secure document management and sharing web application developed using Python and Flask. It allows users to register, log in, upload and manage documents, and share files securely with authorized users. The system aims to protect confidential information and provide controlled access to documents 
>>>>>>> 8b0e2b37046d0a0c4a286de82c09ae6c8947320d
