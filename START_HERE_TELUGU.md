# TrustVault - Start Here (Windows / VS Code)

## Fastest way (no virtual-environment activation needed)
1. Extract the ZIP file.
2. Open VS Code -> File -> Open Folder -> select the `TrustVault` folder.
3. Open Terminal -> New Terminal.
4. Confirm Python is installed: `py --version` (or `python --version`).
5. Run these commands one at a time:

```powershell
py -m venv venv
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe scripts\seed_demo.py
.\venv\Scripts\python.exe app.py
```

If `py` is not recognised, replace `py` with `python` in each command.

6. Keep the terminal open. Open Chrome and visit: **http://127.0.0.1:5000**
7. Sign in with one of the local demo accounts below.

- Admin: `admin@trustvault.local` / `DemoAdminPassword!2026`
- Owner: `owner@trustvault.local` / `DemoOwnerPassword!2026`
- Viewer: `viewer@trustvault.local` / `DemoViewerPassword!2026`

These accounts are for local testing only. Do not use these passwords on a public deployment. Use synthetic test files only.

## If activation command does not work
You do not need to activate the environment. Use the full path commands above (`.\venv\Scripts\python.exe ...`). This avoids the PowerShell `Activate.ps1` execution-policy issue.

## Useful app pages
- Home/login: `http://127.0.0.1:5000/`
- Dashboard: `http://127.0.0.1:5000/dashboard`
- Upload: `http://127.0.0.1:5000/documents/upload` (owner/admin)
- Search: `http://127.0.0.1:5000/search`
- Admin audit log: `http://127.0.0.1:5000/admin/audit` (admin only)

## Stop server
In the VS Code terminal press `Ctrl + C`.

## Test the project
In another terminal, run:

```powershell
.\venv\Scripts\python.exe -m pytest -q
```

If a test fails, keep the exact error output; do not claim the tests passed until they pass locally.
