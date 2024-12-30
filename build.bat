@echo off
REM Install dependencies
pip install pyinstaller pillow

REM Run PyInstaller to create the .exe
pyinstaller --name AmbientHouse --onefile --windowed --distpath build app.py

REM Clean up build files
rmdir /s /q build\__pycache__
rmdir /s /q build\build
del app.spec

echo Build completed. The executable is located in the 'build' folder.
pause