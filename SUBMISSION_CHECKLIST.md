# Submission Checklist

## Repository
- [ ] Create a public Git repository and push the source code.
- [ ] Make genuine, meaningful commits across the work period; do not fabricate history or dates.
- [ ] Check `.env`, database files, uploaded documents, virtual environments, and secrets are not committed.
- [ ] Add the final repository URL to the submission form.

## Application
- [ ] Install dependencies and run locally.
- [ ] Create synthetic demo accounts and confirm login works.
- [ ] Test upload, search, share, revoke, download, edit, delete, and admin audit flows.
- [ ] Run automated tests and record the real output.
- [ ] Deploy to a hosting platform if a live URL is required; configure environment secrets, HTTPS, persistent database/storage, and disable or replace demo accounts.
- [ ] Add the deployed URL to README and submission form only after verifying it works.

## Required documents
- [ ] `README.md` - setup, usage, demo accounts, tests, architecture and deployment notes.
- [ ] `THREATS.md` - threat model, mitigations and accepted risks.
- [ ] `PROMPTS.md` - at least five honest dated AI-use entries; include authorization/audit entries, specific issue, corrective action, and actual commit links. Update it with what really happened.
- [ ] `API.md` - route/API documentation.
- [ ] `PROJECT_WRITEUP.md` - short project write-up.
- [ ] `DEMO_VIDEO_SCRIPT.md` - script for a roughly five-minute demo; record and submit the actual video separately.
- [ ] `tests/` - automated security tests and actual test results.

## Important honesty checks
- A local URL (`http://127.0.0.1:5000`) is not a public live URL.
- A script describing a demo is not the demo video itself.
- `PROMPTS.md` commit links and dates must be filled using real Git history and real actions, not invented.
- Do not upload confidential or personal documents to a demo deployment.
