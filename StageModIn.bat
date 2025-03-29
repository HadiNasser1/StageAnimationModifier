@echo off
:: Set the Python executable (if needed, update with full path)
set PYTHON_PATH=python

:: Get the directory of the batch script (assumes Python script is in the same folder)
set SCRIPT_DIR=%~dp0
set PYTHON_SCRIPT=%SCRIPT_DIR%StageModifyIn.py

:: Get the dropped file
set INPUT_FILE=%~1

:: Check if a file was provided
if "%INPUT_FILE%"=="" (
    echo Please drag and drop a YAML file onto this script.
    pause
    exit /b
)

:: Extract filename without path
for %%F in ("%INPUT_FILE%") do set FILE_NAME=%%~nF

:: Set output file path (same directory as the batch script)
set OUTPUT_FILE=%SCRIPT_DIR%%FILE_NAME%_modified.yml


:: Run the Python script with the input and output paths
%PYTHON_PATH% "%PYTHON_SCRIPT%" "%INPUT_FILE%" "%OUTPUT_FILE%"

:: Pause to see the output
pause
