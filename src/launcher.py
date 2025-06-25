#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
跨平台启动器 - 自动检测系统并启动Markdown转Word转换器
"""

import os
import sys
import platform
import subprocess
from pathlib import Path


def get_python_command():
    """获取合适的Python命令"""
    commands = ['python3', 'python']
    for cmd in commands:
        try:
            result = subprocess.run([cmd, '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                return cmd
        except FileNotFoundError:
            continue
    return None


def check_dependencies():
    """检查依赖包是否已安装"""
    required_packages = [
        'tkinter',
        'python-docx', 
        'markdown',
        'beautifulsoup4',
        'lxml',
        'Pillow'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'tkinter':
                import tkinter
            elif package == 'python-docx':
                import docx
            elif package == 'beautifulsoup4':
                import bs4
            else:
                __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    return missing_packages


def install_dependencies():
    """安装依赖包"""
    python_cmd = get_python_command()
    if not python_cmd:
        print("错误: 未找到Python解释器")
        return False
    
    try:
        print("正在安装依赖包...")
        result = subprocess.run([
            python_cmd, '-m', 'pip', 'install', '-r', 'requirements.txt'
        ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"安装依赖包失败: {e}")
        return False


def main():
    """主函数"""
    print("=" * 50)
    print("    Markdown转Word转换器 - 跨平台启动器")
    print("=" * 50)
    
    # 检测系统信息
    system = platform.system()
    print(f"操作系统: {system}")
    print(f"Python版本: {platform.python_version()}")
    print(f"架构: {platform.machine()}")
    print()
    
    # 获取Python命令
    python_cmd = get_python_command()
    if not python_cmd:
        print("错误: 未找到Python解释器")
        print("请确保已安装Python 3.7或更高版本")
        input("按Enter键退出...")
        return
    
    print(f"使用Python命令: {python_cmd}")
    
    # 检查依赖
    print("检查依赖包...")
    missing = check_dependencies()
    
    if missing:
        print(f"缺少以下依赖包: {', '.join(missing)}")
        if input("是否自动安装? (y/n): ").lower() == 'y':
            if not install_dependencies():
                print("依赖安装失败，程序无法启动")
                input("按Enter键退出...")
                return
        else:
            print("程序需要依赖包才能运行")
            input("按Enter键退出...")
            return
    else:
        print("✅ 所有依赖包已安装")
    
    # 启动主程序
    print("\n正在启动Markdown转Word转换器...")
    try:
        converter_path = Path(__file__).parent / "md_to_word_converter.py"
        if converter_path.exists():
            os.system(f"{python_cmd} {converter_path}")
        else:
            print("错误: 找不到主程序文件 md_to_word_converter.py")
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"启动程序时出错: {e}")
    
    print("\n程序已退出")


if __name__ == "__main__":
    main()
