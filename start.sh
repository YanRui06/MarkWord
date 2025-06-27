#!/bin/bash

# Markdown转Word转换器启动脚本 (macOS/Linux)

echo "===================================="
echo "     Markdown转Word转换器"
echo "===================================="
echo

# 检测操作系统
OS="$(uname -s)"
case "${OS}" in
    Linux*)     MACHINE=Linux;;
    Darwin*)    MACHINE=Mac;;
    *)          MACHINE="UNKNOWN:${OS}"
esac

echo "检测到操作系统: $MACHINE"
echo "正在启动程序..."
echo

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 检查Python是否已安装
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "错误: 未找到Python，请先安装Python 3.7或更高版本"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "使用Python命令: $PYTHON_CMD"

# 检查Python版本
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1)
echo "Python版本: $PYTHON_VERSION"

# 检查虚拟环境
if [ ! -d ".venv" ]; then
    echo "正在创建虚拟环境..."
    $PYTHON_CMD -m venv .venv
fi

# 激活虚拟环境
echo "激活虚拟环境..."
if [ "$MACHINE" = "Mac" ]; then
    source .venv/bin/activate
elif [ "$MACHINE" = "Linux" ]; then
    source .venv/bin/activate
else
    echo "警告: 未知操作系统，尝试使用Linux方式激活虚拟环境"
    source .venv/bin/activate
fi

# 安装依赖
echo "正在检查并安装依赖..."
pip install -r requirements.txt --quiet

# 启动程序 - 修正这里的路径
echo "启动转换器..."
$PYTHON_CMD main.py

echo
echo "程序已退出。"