# TrustVault - Short Project Write-up

## Problem
Organisations share confidential documents with employees, clients, and external partners. Broad folder permissions, old sharing links, and weak auditability can expose documents to people who should not have access. After an incident, teams may also struggle to determine who attempted to access a document and whether the action succeeded.

## Proposed solution
TrustVault is a Flask web application prototype for controlled document sharing. Users authenticate before accessing the dashboard. Documents are stored in a private server-side directory using generated storage keys rather than public filenames. The application stores document metadata in a database and applies per-document read/edit permissions. Owners can grant or revoke access. The application checks permissions on document detail, download, edit, delete, and sharing routes rather than relying only on hiding buttons in the interface.

## Main features
- Role-aware registration and login (public registration cannot create an administrator).
- Document upload with an extension allow-list and size limit; basic file-signature checks for selected formats.
- Per-document read/edit grants and owner-controlled revocation.
- Search by title, category, owner email, and date range, limited to documents the user can access.
- Audit events for important actions and denied document-access attempts.
- Administrator pages for audit metadata and account activation status.
- Automated tests covering important access-control boundaries.

## Security approach
Access checks are performed on the server for each protected route. Uploaded files are kept outside the public static directory. Passwords are stored as hashes. CSRF protection and several browser security headers are enabled. Revoking a permission removes the active grant used by subsequent access checks.

## Limitations and next steps
This is a demonstration prototype, not a production-certified document management service. The hash-linked audit events are not independently tamper-proof; malware scanning and comprehensive content-type validation are not included; rate limiting and production monitoring need to be configured; and deployment requires HTTPS, strong secret management, persistent private storage, database backups, and an independent security review. The included demo credentials must never be exposed as public production credentials.
