# StyleForge AI - 项目结构说明

## 📂 目录结构

```
styleforge-ai/
├── src/                          # 源代码
│   ├── __init__.py              # 主模块导出
│   ├── pipeline.py               # 主Pipeline编排类
│   ├── agents/                  # Agent模块
│   │   ├── __init__.py
│   │   ├── image_analysis.py    # 图像分析Agent
│   │   ├── scene_generation.py  # 场景生成Agent
│   │   ├── platform_adapter.py  # 平台适配Agent
│   │   └── video_synthesis.py  # 视频合成Agent
│   ├── config/                  # 配置模块
│   │   ├── __init__.py
│   │   └── platforms.py         # 平台配置
│   └── utils/                   # 工具函数
│       └── __init__.py
│
├── tests/                        # 测试套件
│   ├── __init__.py
│   ├── test_config.py           # 配置测试
│   ├── test_pipeline.py         # Pipeline测试
│   └── test_agents.py          # Agent测试（待创建）
│
├── docs/                         # 文档
│   ├── CONTRIBUTING.md         # 贡献指南
│   ├── CODE_OF_CONDUCT.md      # 行为准则
│   ├── API.md                  # API文档（待创建）
│   ├── ARCHITECTURE.md        # 架构说明（待创建）
│   ├── AGENTS.md               # Agent规范（待创建）
│   └── PLATFORMS.md           # 平台指南（待创建）
│
├── examples/                     # 使用示例
│   ├── basic_usage.py          # 基本使用
│   ├── batch_processing.py     # 批量处理（待创建）
│   ├── custom_platform.py      # 自定义平台（待创建）
│   └── video_only.py          # 仅视频生成（待创建）
│
├── scripts/                      # 实用脚本（待添加）
│
├── .github/                     # GitHub配置
│   └── workflows/
│       └── ci.yml              # CI/CD配置
│
├── styleforge.py                # CLI入口点
├── setup.py                    # Python包配置
├── requirements.txt             # Python依赖
├── .env.example                # 环境变量模板
├── Dockerfile                  # Docker配置
├── docker-compose.yml          # Docker编排
├── .gitignore                 # Git忽略文件
├── LICENSE                     # MIT许可证
└── README.md                  # 项目说明（你已经有了）
```

## 🚀 快速开始

### 1. 安装依赖

```bash
# 克隆仓库
git clone https://github.com/mrningzeoutlook-pixel/styleforge-ai.git
cd styleforge-ai

# 安装依赖
pip install -r requirements.txt

# 或作为开发包安装
pip install -e ".[dev]"
```

### 2. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env 文件，添加你的API密钥
```

### 3. 运行示例

```bash
# 基本使用
python examples/basic_usage.py

# CLI使用
python styleforge.py --input ./photos/garment.jpg --platforms xiaohongshu,douyin
```

### 4. 运行测试

```bash
# 运行所有测试
pytest tests/ -v

# 运行特定测试文件
pytest tests/test_config.py -v

# 带覆盖率
pytest --cov=src --cov-report=html
```

## 🔧 开发指南

### 添加新平台

1. 编辑 `src/config/platforms.py`
2. 在 `PLATFORMS` 字典中添加新平台配置
3. 运行测试确保没有破坏现有功能
4. 提交Pull Request

示例：

```python
"new_platform": PlatformConfig(
    name="new_platform",
    display_name="New Platform",
    aspect_ratio="1:1",
    image_width=1080,
    image_height=1080,
    video_duration=15.0,
    style_prompt="your style prompt here",
)
```

### 添加新的Agent

1. 在 `src/agents/` 创建新文件
2. 实现Agent类
3. 在 `src/agents/__init__.py` 中导出
4. 在 `src/pipeline.py` 中集成

### 代码规范

- 使用 **Black** 格式化代码：`black src/ tests/`
- 使用 **flake8** 检查代码质量：`flake8 src/ tests/`
- 使用 **mypy** 类型检查：`mypy src/`
- 所有公共函数必须有文档字符串（Google风格）

## 📊 项目统计

- **语言**: Python 3.11+
- **代码行数**: ~1000+ （预计）
- **测试覆盖率**: 目标 80%+
- **支持平台**: 5个（小红书、抖音、TikTok、Instagram、YouTube Shorts）

## 📝 TODO（下一步）

- [ ] 实现实际的AI调用（替换mock数据）
- [ ] 完成 `test_agents.py`
- [ ] 创建 `docs/API.md`
- [ ] 创建 `docs/ARCHITECTURE.md`
- [ ] 添加 `examples/batch_processing.py`
- [ ] 添加CI/CD徽章到README
- [ ] 创建演示视频/GIF
- [ ] 添加性能基准测试

## 🤝 贡献

欢迎提交Pull Request！请先阅读 [CONTRIBUTING.md](docs/CONTRIBUTING.md)。

## 📧 联系

- GitHub Issues: [提交问题](https://github.com/mrningzeoutlook-pixel/styleforge-ai/issues)
- 邮件: mary@styleforge.ai

---

**最后更新**: 2026-05-03
**维护者**: Mary Ma (马女士)
