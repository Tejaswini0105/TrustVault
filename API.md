# TrustVault route and access documentation

| Endpoint | Method | Required access | Notes |
|---|---|---|---|
| `/` | GET | Public | Landing page |
| `/register` | GET/POST | Public | Only owner/viewer roles accepted |
| `/login` | GET/POST | Public | Password checked against hash |
| `/logout` | POST | Authenticated + CSRF token | Ends session |
| `/dashboard` | GET | Authenticated | Lists owned and actively shared documents |
| `/documents/upload` | GET/POST | Owner/Admin | Extension allowlist, 10 MB cap, private storage |
| `/documents/<id>` | GET | Owner or active read/edit grant | Document metadata |
| `/documents/<id>/download` | GET | Owner or active read/edit grant | File bytes returned only after access check |
| `/documents/<id>/edit` | GET/POST | Owner or active Edit grant |
| `/documents/<id>/delete` | POST | Document owner only |
| `/documents/<id>/share` | GET/POST | Document owner | Grant/update read/edit permission |
| `/documents/<id>/revoke/<user_id>` | POST | Document owner | Revoke active permission |
| `/search` | GET | Authenticated | Restricted to owned/shared documents |
| `/admin/audit` | GET | Admin | Latest 500 audit events |
| `/admin/users` | GET/POST | Admin | Activate/deactivate accounts |

All state-changing HTML forms use CSRF tokens. These are server-rendered web routes, not a versioned JSON API.
