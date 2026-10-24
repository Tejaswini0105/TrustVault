# 5-minute Demo Video Script

Use synthetic documents only. Do not show real salary letters, customer contracts, passwords, or personal information.

## 0:00-0:30 - Introduction
"This is TrustVault, a document-sharing prototype focused on least-privilege access and auditability. The main risk we address is one person receiving access to documents they should not see, with no reliable record of what happened."

## 0:30-1:15 - Login and dashboard
Log in as the demo owner. Show the dashboard and explain that it lists documents owned by or explicitly shared with the current user.

## 1:15-2:00 - Upload and search
Upload a small synthetic `.txt` or `.pdf` file with a clear demo title and category. Show the file in the dashboard and search for it by title/category.

## 2:00-3:00 - Grant and revoke access
Open the document sharing page. Grant the demo viewer read access. Log out, log in as the viewer, and show that the viewer can open/download the shared document. Return as the owner and revoke the grant. Log back in as the viewer and demonstrate that access is denied after revocation.

## 3:00-4:00 - Audit and authorization
Log in as the admin and show the audit page. Explain the difference between successful and denied events. Show that admin audit access does not automatically give access to document contents. If the demo environment is ready, attempt a cross-user document URL as a user without permission and show the denial.

## 4:00-4:40 - Automated tests
Show the `tests/` directory and run `python -m pytest -q`. Report the actual test result on screen; do not claim success if tests fail.

## 4:40-5:00 - Limitations
Explain that this is a prototype. Mention that production use needs HTTPS, strong secret management, malware scanning, rate limits, durable private storage, protected audit backups, and independent security review.
