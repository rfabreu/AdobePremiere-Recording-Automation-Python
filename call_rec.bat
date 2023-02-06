@echo off
cd [enter_dir_name]
set PYTHON_EXE=python
set SCRIPT_DIRECTORY=.

for %%f in (%SCRIPT_DIRECTORY%\*.py) do (
	start /B %PYTHON_EXE% "%%f"
)
