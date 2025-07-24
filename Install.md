# TikTokDownloader 安装和运行指南

本项目使用 **uv** 作为 Python 依赖管理工具，提供快速、可靠的包管理体验。

## 目录
- [环境要求](#环境要求)
- [uv 安装](#uv-安装)
- [项目依赖安装](#项目依赖安装)
- [程序启动运行](#程序启动运行)
- [开发环境设置](#开发环境设置)
- [常见问题](#常见问题)

## 环境要求

- **Python 版本**: 3.12.x (严格要求，不支持其他版本)
- **操作系统**: Windows、macOS、Linux
- **网络**: 需要稳定的网络连接用于下载依赖

## uv 安装

### 方法一：使用官方安装脚本（推荐）

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 方法二：使用包管理器

**macOS (Homebrew):**
```bash
brew install uv
```

**Windows (Scoop):**
```bash
scoop install uv
```

**Windows (Chocolatey):**
```bash
choco install uv
```

**Linux (Debian/Ubuntu):**
```bash
# 添加 Astral 的 APT 仓库
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 方法三：使用 pip 安装
```bash
pip install uv
```

### 验证安装
```bash
uv --version
```

## 项目依赖安装

### 1. 克隆项目（如果还没有）
```bash
git clone https://github.com/JoeanAmier/TikTokDownloader.git
cd TikTokDownloader
```

### 2. 创建虚拟环境并安装依赖
```bash
# uv 会自动检测 pyproject.toml 并创建虚拟环境
uv sync
```

这个命令会：
- 自动检测并安装 Python 3.12（如果系统没有）
- 创建项目专用的虚拟环境
- 安装所有生产依赖
- 生成或更新 uv.lock 文件

### 3. 仅安装生产依赖（不包含开发依赖）
```bash
uv sync --no-dev
```

### 4. 安装开发依赖
```bash
uv sync --group dev
```

## 程序启动运行

### 方法一：使用 uv run（推荐）
```bash
# 直接运行主程序
uv run python main.py
```

### 方法二：激活虚拟环境后运行
```bash
# 激活虚拟环境
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows

# 运行程序
python main.py
```

### 方法三：使用 uv 的一键运行
```bash
# uv 会自动处理环境和依赖
uv run main.py
```

## 开发环境设置

### 安装开发依赖
```bash
uv sync --group dev
```

### 运行测试
```bash
uv run pytest
```

### 代码格式化（使用 ruff）
```bash
# 检查代码风格
uv run ruff check .

# 自动修复代码风格问题
uv run ruff check --fix .

# 格式化代码
uv run ruff format .
```

### 添加新依赖
```bash
# 添加生产依赖
uv add package_name

# 添加开发依赖
uv add --group dev package_name

# 添加特定版本
uv add "package_name>=1.0.0"
```

### 移除依赖
```bash
uv remove package_name
```

## 项目结构说明

```
TikTokDownloader/
├── pyproject.toml          # 项目配置和依赖定义
├── uv.lock                 # 锁定的依赖版本
├── main.py                 # 程序入口点
├── src/                    # 源代码目录
│   ├── application/        # 应用程序主逻辑
│   ├── config/            # 配置管理
│   ├── downloader/        # 下载器模块
│   └── ...                # 其他模块
└── .venv/                 # 虚拟环境（uv 自动创建）
```

## 常见问题

### Q: 如何更新依赖？
```bash
# 更新所有依赖到最新兼容版本
uv sync --upgrade

# 更新特定包
uv add package_name --upgrade
```

### Q: 如何查看已安装的包？
```bash
uv pip list
```

### Q: 如何清理环境？
```bash
# 删除虚拟环境
rm -rf .venv

# 重新创建环境
uv sync
```

### Q: Python 版本不匹配怎么办？
项目严格要求 Python 3.12.x，如果系统没有：

```bash
# uv 可以自动安装 Python
uv python install 3.12

# 或者指定使用特定 Python 版本
uv sync --python 3.12
```

### Q: 网络问题导致安装失败？
```bash
# 使用国内镜像源
uv sync --index-url https://pypi.tuna.tsinghua.edu.cn/simple/
```

### Q: 如何在不同环境间切换？
```bash
# 开发环境（包含所有依赖）
uv sync

# 生产环境（仅核心依赖）
uv sync --no-dev
```

## 性能优势

使用 uv 相比传统的 pip + venv 有以下优势：

1. **速度快**: 依赖解析和安装速度比 pip 快 10-100 倍
2. **可靠性**: 确定性的依赖解析，避免版本冲突
3. **简单**: 一个命令完成环境创建和依赖安装
4. **现代**: 原生支持 pyproject.toml 和现代 Python 打包标准

## 更多信息

- [uv 官方文档](https://docs.astral.sh/uv/)
- [项目 GitHub 仓库](https://github.com/JoeanAmier/TikTokDownloader)
- [问题反馈](https://github.com/JoeanAmier/TikTokDownloader/issues)