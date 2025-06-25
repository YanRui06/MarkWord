#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown转Word转换器 - 主入口文件
作者: GitHub Copilot
版本: 1.0.0
日期: 2025-06-25

这是项目的主入口文件，用于启动Markdown转Word转换器。
"""

import sys
import os
from pathlib import Path

# 添加src目录到Python路径
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def main():
    """主函数 - 启动应用程序"""
    try:
        # 导入并启动转换器
        from md_to_word_converter import MarkdownToWordConverter
        
        print("🚀 启动Markdown转Word转换器...")
        app = MarkdownToWordConverter()
        app.run()
        
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        print("请确保所有依赖包已正确安装。")
        print("运行: pip install -r requirements.txt")
        
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        

if __name__ == "__main__":
    main()
