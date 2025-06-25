# 跨平台使用指南

## 🌍 支持的操作系统

- ✅ **Windows** 7/8/10/11 (32位/64位)
- ✅ **macOS** 10.12+ (Intel/Apple Silicon)
- ✅ **Linux** Ubuntu/CentOS/Fedora/Debian等

## 🚀 快速启动

### Windows系统

#### 方法1: 双击启动（推荐）
```
双击 start.bat 文件
```

#### 方法2: 命令行启动
```cmd
python launcher.py
```

#### 方法3: 直接运行
```cmd
python md_to_word_converter.py
```

### macOS系统

#### 方法1: 终端启动（推荐）
```bash
chmod +x start.sh
./start.sh
```

#### 方法2: Python启动器
```bash
python3 launcher.py
```

#### 方法3: 直接运行
```bash
python3 md_to_word_converter.py
```

#### 方法4: 创建应用程序包
```bash
python3 create_mac_app.py
# 然后双击生成的 Markdown转换器.app
```

### Linux系统

#### 方法1: 脚本启动（推荐）
```bash
chmod +x start.sh
./start.sh
```

#### 方法2: Python启动器
```bash
python3 launcher.py
```

#### 方法3: 直接运行
```bash
python3 md_to_word_converter.py
```

## 🛠️ 环境配置

### Windows

1. **安装Python 3.7+**
   - 从 [python.org](https://python.org) 下载安装
   - 确保勾选"Add to PATH"

2. **验证安装**
   ```cmd
   python --version
   pip --version
   ```

### macOS

1. **安装Python 3（如果未安装）**
   ```bash
   # 使用Homebrew（推荐）
   brew install python3
   
   # 或从python.org下载安装包
   ```

2. **验证安装**
   ```bash
   python3 --version
   pip3 --version
   ```

### Linux (Ubuntu/Debian)

1. **安装Python和依赖**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-tk
   ```

2. **验证安装**
   ```bash
   python3 --version
   pip3 --version
   ```

### Linux (CentOS/RHEL)

1. **安装Python和依赖**
   ```bash
   sudo yum install python3 python3-pip tkinter
   # 或对于较新版本
   sudo dnf install python3 python3-pip python3-tkinter
   ```

### Linux (Fedora)

1. **安装Python和依赖**
   ```bash
   sudo dnf install python3 python3-pip python3-tkinter
   ```

## 🎨 系统适配特性

### 字体适配

| 系统 | 界面字体 | 代码字体 | 文档字体 |
|------|----------|----------|----------|
| Windows | 微软雅黑 | Consolas | 微软雅黑 |
| macOS | SF Pro Display | SF Mono | PingFang SC |
| Linux | DejaVu Sans | DejaVu Sans Mono | DejaVu Sans |

### 主题适配

- **Windows**: Vista/默认主题
- **macOS**: Aqua原生主题
- **Linux**: GTK兼容主题

### 文件路径处理

程序自动处理不同系统的路径格式：
- **Windows**: `C:\Users\...\file.md`
- **macOS/Linux**: `/home/.../file.md`

## 🔧 故障排除

### 问题1: "No module named 'tkinter'"

**Windows/macOS**: Tkinter通常预装，如果缺失需重新安装Python

**Linux解决方案**:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install tkinter

# Fedora
sudo dnf install python3-tkinter
```

### 问题2: 字体显示异常

**Windows**: 
- 确保已安装微软雅黑字体
- 更新到最新的Windows版本

**macOS**:
- 系统会自动处理字体
- 确保系统版本10.12+

**Linux**:
```bash
# 安装中文字体支持
sudo apt-get install fonts-dejavu fonts-wqy-*
```

### 问题3: 程序无法启动

1. **检查Python版本**
   ```bash
   python --version  # 应该是3.7+
   ```

2. **检查依赖安装**
   ```bash
   python -c "import tkinter, docx, markdown"
   ```

3. **重新安装依赖**
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

### 问题4: 权限问题（macOS/Linux）

```bash
# 给脚本执行权限
chmod +x start.sh
chmod +x launcher.py

# 如果仍有问题，检查目录权限
ls -la
```

### 问题5: 中文乱码

1. **确保文件编码为UTF-8**
2. **检查系统区域设置**
3. **重新保存Markdown文件并指定UTF-8编码**

## 📞 技术支持

如果遇到问题：

1. **运行测试脚本诊断**
   ```bash
   python test_converter.py
   ```

2. **查看详细错误信息**
   - 启动程序后查看日志窗口
   - 记录具体错误信息

3. **环境信息收集**
   ```bash
   python --version
   pip list | grep -E "(docx|markdown|beautifulsoup)"
   ```

## 🎯 性能优化建议

### 大文件处理
- 对于大型Markdown文件（>10MB），建议分段处理
- 关闭不必要的选项以提高速度

### 内存使用
- 处理大量图片时确保有足够内存（建议2GB+）
- 定期重启程序以释放内存

### 跨平台最佳实践
- 使用相对路径引用图片
- 避免使用系统特定的文件路径
- 保持Markdown文件编码为UTF-8

---

*享受跨平台的无缝体验！* 🌟
