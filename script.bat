@echo off
setlocal

set SCRIPT_DIR=%~dp0
set SOURCE_CFG=%SCRIPT_DIR%autoexec.cfg
set TARGET_DIR=C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg
set TARGET_CFG=%TARGET_DIR%\autoexec.cfg

copy /Y "%SOURCE_CFG%" "%TARGET_CFG%"

REM Open destination folder in Explorer
explorer "%TARGET_DIR%"

endlocal
