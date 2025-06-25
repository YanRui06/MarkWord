#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
macOS应用程序包创建脚本
将Markdown转换器打包成macOS应用程序
"""

import os
import sys
import shutil
from pathlib import Path

def create_mac_app():
    """创建macOS应用程序包"""
    app_name = "Markdown转换器"
    app_dir = f"{app_name}.app"
    
    # 创建应用程序目录结构
    contents_dir = Path(app_dir) / "Contents"
    macos_dir = contents_dir / "MacOS"
    resources_dir = contents_dir / "Resources"
    
    # 创建目录
    macos_dir.mkdir(parents=True, exist_ok=True)
    resources_dir.mkdir(parents=True, exist_ok=True)
    
    # 创建Info.plist文件
    info_plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>launcher</string>
    <key>CFBundleIdentifier</key>
    <string>com.markdown.converter</string>
    <key>CFBundleName</key>
    <string>{app_name}</string>
    <key>CFBundleVersion</key>
    <string>1.0.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.12</string>
    <key>NSHighResolutionCapable</key>
    <true/>
</dict>
</plist>"""
    
    (contents_dir / "Info.plist").write_text(info_plist, encoding='utf-8')
    
    # 复制程序文件
    current_dir = Path(__file__).parent.parent
    
    # 主程序文件
    files_to_copy = [
        "src/md_to_word_converter.py",
        "src/launcher.py",
        "src/__init__.py",
        "main.py",
        "requirements.txt",
        "examples/sample.md"
    ]
    
    for file in files_to_copy:
        src_file = current_dir / file
        if src_file.exists():
            if "/" in file:
                # 创建子目录
                dest_subdir = resources_dir / Path(file).parent
                dest_subdir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_file, resources_dir / file)
    
    # 创建启动脚本
    launcher_script = f"""#!/bin/bash
cd "$(dirname "$0")/../Resources"
python3 main.py
"""
    
    launcher_path = macos_dir / "launcher"
    launcher_path.write_text(launcher_script, encoding='utf-8')
    launcher_path.chmod(0o755)
    
    print(f"✅ macOS应用程序包已创建: {app_dir}")
    print(f"可以直接双击 {app_dir} 启动程序")

if __name__ == "__main__":
    if sys.platform != "darwin":
        print("此脚本仅适用于macOS系统")
        sys.exit(1)
    
    create_mac_app()
