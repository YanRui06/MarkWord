@echo off
echo ====================================
echo     Markdown转Word转换器
echo ====================================
echo.
echo 正在启动程序...
echo.

cd /d "%~dp0"

REM 检查Python是否已安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.7或更高版本
    pause
    exit /b 1
)

REM 检查虚拟环境
if not exist ".venv" (
    echo 正在创建虚拟环境...
    python -m venv .venv
)

REM 激活虚拟环境
call .venv\Scripts\activate.bat

REM 安装依赖
echo 正在检查并安装依赖...
pip install -r requirements.txt --quiet

REM 启动程序
echo 启动转换器...
python ..\main.py

pause
