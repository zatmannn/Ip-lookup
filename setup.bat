@echo off
chcp 65001 > nul
cls

color 1
echo.
echo  ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄       ██▓     ██▓     ██▓ ███▄    █   ▄████ 
echo  ▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▓██▒    ▓██▒    ▓██▒ ██ ▀█   █  ██▒ ▀█▒
echo  ▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░    ▒██░    ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
echo  ░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░    ▒██░    ░██░▓██▒  ▐▌██▒░▓█  ██▓
echo  ░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░██████▒░██████▒░██░▒██░   ▓██░░▒▓███▀▒
echo  ░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
echo   ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░  ░   ░ 
echo   ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒     ░ ░     ░ ░    ▒ ░   ░   ░ ░ ░ ░   ░ 
echo   ░           ░       ░                 ░  ░    ░  ░    ░  ░ ░           ░       ░ 
echo.


where python > nul 2> nul
if errorlevel 1 (
    echo [!] Install Python!
    pause
    exit /b)

echo [!] Installing requests...
pip install requests
echo [!] Installing pystyle...
pip install pystyle

cls
echo [!] Installed successfully
pause