@echo off
:: Set the Python executable
set PYTHON_PATH=python

:: Get the directory of the batch script
set SCRIPT_DIR=%~dp0
set PYTHON_SCRIPT=%SCRIPT_DIR%StageModifyOut.py

:: Get the dragged file
set INPUT_FILE=%~1

:: Check if a file was provided
if "%INPUT_FILE%"=="" (
    echo Please drag and drop a YAML file onto this script.
    pause
    exit /b
)

:: Extract filename without path
for %%F in ("%INPUT_FILE%") do set FILE_NAME=%%~nF

:: Set output file path (same folder as the batch script)
set OUTPUT_FILE=%SCRIPT_DIR%%FILE_NAME%_final.yml

:: Run the Python script with the correct arguments
%PYTHON_PATH% "%PYTHON_SCRIPT%" "%INPUT_FILE%" "%OUTPUT_FILE%"

:: Pause to see the output
pause
