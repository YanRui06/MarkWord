# Markdown转Word转换器

一个功能强大的跨平台Markdown文档转换工具，能够将Markdown文件转换为格式良好的Word文档，并尽可能保持原有格式。

## 🌟 跨平台支持

- ✅ **Windows** (Windows 7/8/10/11)
- ✅ **macOS** (macOS 10.12+)
- ✅ **Linux** (Ubuntu, CentOS, Fedora等主流发行版)

## 功能特性

- 🎨 **保持格式**: 完美保持标题、段落、列表等格式
- 📝 **多种元素支持**: 支持表格、代码块、引用、链接等
- 🖼️ **图片处理**: 自动处理本地图片插入
- 🎯 **用户友好**: 简洁直观的图形界面
- ⚡ **快速转换**: 高效的转换引擎
- 📊 **进度显示**: 实时显示转换进度和日志
- 🌍 **跨平台**: 支持Windows、macOS、Linux
- 🎨 **系统适配**: 自动适配各系统的字体和主题

## 支持的Markdown元素

### 文本格式
- ✅ 标题 (H1-H6)
- ✅ 粗体、斜体文本
- ✅ 行内代码
- ✅ 删除线

### 块级元素
- ✅ 段落
- ✅ 有序列表
- ✅ 无序列表
- ✅ 代码块
- ✅ 引用块
- ✅ 表格
- ✅ 分隔线

### 媒体元素
- ✅ 本地图片
- ✅ 链接 (转换为文本形式)

## 安装要求

### 系统要求
- **操作系统**: Windows 7+, macOS 10.12+, 或 Linux
- **Python**: 3.7或更高版本
- **内存**: 至少512MB可用内存
- **磁盘空间**: 至少100MB可用空间

### 依赖包
程序会自动安装以下依赖包：
```
python-docx>=0.8.11
markdown>=3.4.0
beautifulsoup4>=4.11.0
lxml>=4.9.0
Pillow>=9.0.0
python-markdown-math>=0.8
```

## 快速安装和使用

### 方法一: 自动启动器（推荐）

#### Windows用户:
1. 双击 `scripts/start.bat` 文件
2. 程序会自动检查环境并启动

#### macOS/Linux用户:
1. 在终端中运行: `chmod +x scripts/start.sh && ./scripts/start.sh`
2. 或者运行: `python3 src/launcher.py`

### 方法二: 使用主入口文件

适用于所有系统：
```bash
python main.py
```

### 方法三: 手动安装

1. **安装Python依赖**:
   ```bash
   pip install -r requirements.txt
   ```

2. **启动程序**:
   ```bash
   # 直接运行主程序
   python src/md_to_word_converter.py
   
   # 或使用启动器
   python src/launcher.py
   ```

### 方法四: 使用跨平台启动器

```bash
python src/launcher.py
```

### 操作步骤

1. **选择输入文件**: 点击"浏览"按钮选择要转换的Markdown文件(.md)
2. **指定输出位置**: 选择Word文档的保存位置(.docx)
3. **配置选项**:
   - ☑️ **保持原有格式**: 尽可能保持Markdown的原始格式
   - ☑️ **生成目录**: 为文档自动生成目录
   - ☑️ **处理图片**: 将本地图片插入到Word文档中
4. **开始转换**: 点击"开始转换"按钮
5. **查看进度**: 观察进度条和日志输出
6. **完成**: 转换完成后会显示成功消息

## 🔧 系统特定优化

### Windows系统
- 使用微软雅黑字体显示中文
- 采用Vista主题样式
- 支持.ico图标格式
- 代码块使用Consolas字体

### macOS系统
- 使用SF Pro Display字体
- 采用Aqua原生主题
- 支持Retina显示屏
- 代码块使用SF Mono字体

### Linux系统
- 使用DejaVu Sans字体
- 采用适配的GTK主题
- 支持各种桌面环境
- 代码块使用DejaVu Sans Mono字体

## 📁 项目结构

```
markdown-to-word-converter/
├── 📂 src/                        # 源代码目录
│   ├── md_to_word_converter.py    # 主程序文件
│   ├── launcher.py                # 跨平台启动器
│   └── __init__.py                # 包初始化文件
├── 📂 scripts/                    # 启动脚本目录
│   ├── start.bat                  # Windows启动脚本
│   ├── start.sh                   # macOS/Linux启动脚本
│   └── create_mac_app.py          # macOS应用程序包创建
├── 📂 tests/                      # 测试文件目录
│   └── test_converter.py          # 功能测试脚本
├── 📂 examples/                   # 示例文件目录
│   └── sample.md                  # 示例Markdown文件
├── 📂 docs/                       # 文档目录
│   ├── USER_GUIDE.md             # 详细使用指南
│   └── CROSS_PLATFORM_GUIDE.md   # 跨平台使用指南
├── 📄 main.py                     # 项目主入口文件
├── 📄 requirements.txt            # 依赖包列表
├── 📄 pyproject.toml             # 项目配置文件
├── 📄 LICENSE                     # 许可证文件
├── 📄 CHANGELOG.md               # 更新日志
├── 📄 .gitignore                 # Git忽略文件
└── 📄 README.md                  # 项目说明文档
```

## 示例文件

项目包含一个示例Markdown文件 `sample.md`，展示了各种支持的格式元素。您可以使用这个文件来测试转换器的功能。

## 注意事项

- 📄 **文件编码**: 确保Markdown文件使用UTF-8编码
- 🖼️ **图片路径**: 图片应使用相对于Markdown文件的相对路径
- 🔗 **外部链接**: 网络图片不会被下载，仅支持本地图片
- 📝 **复杂格式**: 某些复杂的HTML标签可能无法完美转换

## 🛠️ 故障排除

### 字体问题
如果字体显示不正常：
- **Windows**: 确保已安装微软雅黑字体
- **macOS**: 系统会自动使用合适的字体
- **Linux**: 安装推荐字体包: `sudo apt-get install fonts-dejavu`

### 依赖安装问题
```bash
# 如果pip安装失败，尝试升级pip
python -m pip install --upgrade pip

# 或使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

### Tkinter问题 (Linux)
如果出现"No module named 'tkinter'"错误：
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install tkinter

# Fedora
sudo dnf install python3-tkinter
```

### 权限问题 (macOS/Linux)
给启动脚本执行权限：
```bash
chmod +x start.sh
chmod +x launcher.py
```

## 技术实现

- **GUI框架**: Tkinter
- **Markdown解析**: python-markdown
- **HTML解析**: BeautifulSoup4
- **Word文档生成**: python-docx
- **图片处理**: Pillow

## 版本信息

- **当前版本**: 1.0.0
- **开发语言**: Python 3.10+
- **许可证**: MIT

## 贡献

欢迎提交问题和改进建议！

---

*享受Markdown到Word的无缝转换体验！* 🚀
