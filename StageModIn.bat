@echo off
:: Ensure a file was dragged and dropped
if "%~1"=="" (
    echo Please drag and drop a YAML file onto this script.
    pause
    exit /b
)

:: Get the script directory and input file
set SCRIPT_DIR=%~dp0
set PYTHON_SCRIPT="%SCRIPT_DIR%StageModifyIn.py"
set INPUT_FILE="%~1"

:: Extract filename without path
for %%F in ("%INPUT_FILE%") do set FILE_NAME=%%~nF

:: Set output file path (same folder as the batch script)
set OUTPUT_FILE="%SCRIPT_DIR%%FILE_NAME%_modified.yml"

:: Run the Python script using 'py -3' (ensures Python 3 is used)
py -3 "%PYTHON_SCRIPT%" %INPUT_FILE% %OUTPUT_FILE%

:: Pause to see the output
pause
