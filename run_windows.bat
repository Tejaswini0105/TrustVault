@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (set "PY=py") else (set "PY=python")
if not exist "venv\Scripts\python.exe" (
  echo Creating virtual environment...
  %PY% -m venv venv
  if errorlevel 1 goto failed
)
echo Installing requirements...
venv\Scripts\python.exe -m pip install --upgrade pip
if errorlevel 1 goto failed
venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto failed
echo Creating local demo accounts...
venv\Scripts\python.exe scripts\seed_demo.py
if errorlevel 1 goto failed
echo Starting TrustVault at http://127.0.0.1:5000
venv\Scripts\python.exe app.py
goto end
:failed
echo Setup failed. Read the error above and see START_HERE_TELUGU.md.
pause
:end
endlocal
