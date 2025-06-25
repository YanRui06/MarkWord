# 开发者文档

## 项目架构

### 核心组件

#### 1. `src/md_to_word_converter.py`
主程序文件，包含 `MarkdownToWordConverter` 类：
- GUI界面构建
- Markdown解析和转换
- Word文档生成
- 跨平台适配

#### 2. `src/launcher.py`
智能启动器：
- 自动检测系统环境
- 依赖包检查和安装
- 程序启动管理

#### 3. `main.py`
项目主入口文件：
- 简化的启动接口
- 路径管理
- 错误处理

### 跨平台实现

#### 字体系统
```python
if self.system == "Windows":
    self.default_font = ("微软雅黑", 10)
    self.code_font = ("Consolas", 9)
elif self.system == "Darwin":  # macOS
    self.default_font = ("SF Pro Display", 10)
    self.code_font = ("SF Mono", 9)
else:  # Linux
    self.default_font = ("DejaVu Sans", 10)
    self.code_font = ("DejaVu Sans Mono", 9)
```

#### 主题适配
```python
if self.system == "Windows":
    self.style.theme_use('vista')
elif self.system == "Darwin":
    self.style.theme_use('aqua')
else:
    self.style.theme_use('clam')
```

## 开发环境设置

### 1. 克隆项目
```bash
git clone <repository-url>
cd markdown-to-word-converter
```

### 2. 创建虚拟环境
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate.bat  # Windows
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 运行测试
```bash
python tests/test_converter.py
```

## 代码规范

### 文件编码
- 所有Python文件使用UTF-8编码
- 文件头部包含编码声明：`# -*- coding: utf-8 -*-`

### 命名约定
- 类名：PascalCase（如 `MarkdownToWordConverter`）
- 函数名：snake_case（如 `setup_platform_config`）
- 常量：UPPER_CASE（如 `DEFAULT_FONT_SIZE`）
- 变量名：snake_case（如 `input_file_path`）

### 文档字符串
```python
def convert_file(self, input_file, output_file):
    """转换文件
    
    Args:
        input_file (str): 输入的Markdown文件路径
        output_file (str): 输出的Word文件路径
        
    Returns:
        bool: 转换是否成功
        
    Raises:
        FileNotFoundError: 输入文件不存在
        PermissionError: 输出路径无写权限
    """
```

## 测试策略

### 单元测试
- 每个核心功能都有对应的测试用例
- 使用pytest框架进行测试
- 测试覆盖率目标：>80%

### 跨平台测试
- Windows 10/11
- macOS 10.12+
- Ubuntu 18.04+
- CentOS 7+

### 性能测试
- 小文件（<1MB）：<5秒
- 中等文件（1-10MB）：<30秒
- 大文件（>10MB）：提供进度显示

## 构建和发布

### 构建可执行文件

#### 使用PyInstaller
```bash
pip install pyinstaller
pyinstaller --windowed --onefile main.py
```

#### macOS应用程序包
```bash
python scripts/create_mac_app.py
```

### 发布检查清单
- [ ] 更新版本号（`src/__init__.py`、`pyproject.toml`）
- [ ] 更新CHANGELOG.md
- [ ] 运行所有测试
- [ ] 构建可执行文件
- [ ] 测试安装包
- [ ] 更新文档
- [ ] 创建Git标签

## 贡献指南

### 提交代码
1. Fork项目
2. 创建功能分支：`git checkout -b feature-name`
3. 提交更改：`git commit -am 'Add some feature'`
4. 推送分支：`git push origin feature-name`
5. 创建Pull Request

### 代码审查
- 所有代码必须通过代码审查
- 确保测试通过
- 遵循代码规范
- 更新相关文档

### 问题报告
使用GitHub Issues报告问题，包含：
- 详细的错误描述
- 重现步骤
- 系统环境信息
- 错误日志（如有）

## API参考

### MarkdownToWordConverter类

#### 主要方法
- `__init__()`: 初始化转换器
- `setup_platform_config()`: 配置平台相关设置
- `setup_ui()`: 构建用户界面
- `convert_file(input_file, output_file)`: 转换文件
- `setup_document_styles(doc)`: 设置Word文档样式

#### 配置选项
- `preserve_formatting`: 保持原有格式
- `include_toc`: 生成目录
- `process_images`: 处理图片
- `clean_formatting`: 清理格式

## 扩展开发

### 添加新的Markdown元素支持
1. 在`process_element()`方法中添加新的元素处理
2. 更新测试用例
3. 更新文档

### 添加新的输出格式
1. 创建新的转换器类
2. 实现相应的格式处理方法
3. 更新GUI界面选项

### 自定义主题
1. 在`setup_styles()`方法中添加主题选项
2. 定义主题色彩方案
3. 更新配置文件支持

---

*开发愉快！如有问题请查看文档或提交Issue。*
