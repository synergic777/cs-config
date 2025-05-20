@echo off
set SOURCE_CFG=%USERPROFILE%\Desktop\cs-config\autoexec.cfg
set TARGET_CFG="C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg\autoexec.cfg"
set TARGET_DIR="C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg"

copy /Y "%SOURCE_CFG%" %TARGET_CFG%

REM Open destination folder in Explorer
explorer %TARGET_DIR%