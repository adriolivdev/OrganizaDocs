@echo off
cd /d "%~dp0"
call ..\.venv\Scripts\activate.bat
python organizador_arquivos.py
pause
