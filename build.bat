@echo off
REM Install dependencies
pip install pyinstaller pillow

REM Run PyInstaller to create the .exe
pyinstaller --name AmbientHouse --onefile --windowed --add-data "assets;assets" --distpath build app.py

REM Copy the assets folder to the build directory
xcopy assets build\assets /E /I /Y

REM Clean up build files
rmdir /s /q build\__pycache__
rmdir /s /q build\build
del app.spec

echo Build completed. The executable is located in the 'build' folder.
pause