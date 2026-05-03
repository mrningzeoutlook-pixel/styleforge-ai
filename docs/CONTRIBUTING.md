# Contributing to StyleForge AI 🤝

Thank you for your interest in contributing to StyleForge AI! This document provides guidelines and instructions for contributing.

## 🌟 Ways to Contribute

- 🐛 Report bugs and issues
- 💡 Suggest new features or enhancements
- 📝 Improve documentation
- 🧪 Write tests
- 🔧 Submit pull requests with fixes or features
- 🎨 Create example projects

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Git
- API keys (OpenAI, Replicate) for testing

### Development Setup

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/styleforge-ai.git
cd styleforge-ai

# Add upstream repository
git remote add upstream https://github.com/mrningzeoutlook-pixel/styleforge-ai.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Copy and configure environment
cp .env.example .env
# Edit .env with your API keys
```

## 📋 Development Workflow

### 1. Create a Feature Branch

```bash
# Update your main branch
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Write code following our [Style Guide](#style-guide)
- Add tests for new functionality
- Update documentation as needed
- Keep commits focused and atomic

### 3. Test Your Changes

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest --cov=src --cov-report=html

# Run linters
flake8 src/ tests/
black --check src/ tests/
mypy src/
```

### 4. Commit Your Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "feat: add support for YouTube Shorts platform"
```

#### Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style/formatting
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### 5. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create pull request on GitHub
```

## 🎨 Style Guide

### Python Code Style

- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://black.readthedocs.io/) for formatting
- Use [flake8](https://flake8.pycqa.org/) for linting
- Use [mypy](https://mypy.readthedocs.io/) for type checking

```python
# Good
def process_image(image_path: str, quality: int = 95) -> Image:
    """Process image with specified quality.
    
    Args:
        image_path: Path to input image
        quality: JPEG quality (1-100)
        
    Returns:
        Processed PIL Image object
        
    Raises:
        FileNotFoundError: If image_path doesn't exist
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    img = Image.open(image_path)
    return img


# Bad
def process_image(img, q=95):
    return Image.open(img)
```

### Documentation Style

- Use [Google Style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for docstrings
- Keep line length ≤ 88 characters (Black default)
- Use type hints for all function signatures

## 🧪 Testing Guidelines

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_pipeline.py

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=src --cov-report=term-missing
```

### Writing Tests

```python
import pytest
from src.agents import ImageAnalysisAgent


class TestImageAnalysisAgent:
    """Test suite for ImageAnalysisAgent."""
    
    @pytest.fixture
    def agent(self):
        return ImageAnalysisAgent()
    
    def test_analyze_valid_image(self, agent, tmp_path):
        """Test analysis of valid image file."""
        # Create test image
        test_image = tmp_path / "test.jpg"
        test_image.write_bytes(b"fake_image_data")
        
        result = agent.analyze(str(test_image))
        
        assert "garment_type" in result
        assert "color" in result
    
    def test_analyze_invalid_image(self, agent):
        """Test handling of invalid image file."""
        with pytest.raises(FileNotFoundError):
            agent.analyze("nonexistent.jpg")
```

### Test Coverage

- Aim for ≥ 80% test coverage
- All new features must include tests
- All bug fixes must include regression tests

## 📝 Pull Request Guidelines

### Before Creating PR

- [ ] All tests pass locally
- [ ] Code is properly formatted (Black)
- [ ] No linting errors (flake8)
- [ ] Type checking passes (mypy)
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated (if needed)

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe how you tested your changes

## Screenshots (if applicable)
Add screenshots here

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] CHANGELOG updated
```

## 🐛 Reporting Bugs

### Before Submitting

1. Check [existing issues](https://github.com/mrningzeoutlook-pixel/styleforge-ai/issues)
2. Try to reproduce on `main` branch
3. Collect relevant information

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Run command '...'
2. With input '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., Windows 11, macOS 14]
- Python version: [e.g., 3.11.5]
- Package version: [e.g., 0.2.0]

**Additional context**
Any other context about the problem.
```

## 💡 Suggesting Enhancements

### Enhancement Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of what the problem is.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Any alternative solutions or features you've considered.

**Additional context**
Any other context or screenshots about the feature request.
```

## 📚 Documentation

### Building Docs Locally

```bash
# Install docs dependencies
pip install mkdocs mkdocs-material

# Serve docs locally
mkdocs serve

# Build docs
mkdocs build
```

### Documentation Standards

- Keep README.md up-to-date
- Document all public APIs
- Include usage examples
- Add docstrings to all functions/classes

## 🔒 Security

### Reporting Security Vulnerabilities

**Do NOT open a public issue.**

Email security@styleforge.ai with:
- Description of vulnerability
- Steps to reproduce
- Potential impact

We'll respond within 48 hours.

## 🎯 Project Roadmap

See [ROADMAP.md](ROADMAP.md) for upcoming features and priorities.

## 💬 Community

- Join our [Discord](https://discord.gg/styleforge)
- Follow on [Twitter](https://twitter.com/styleforge_ai)
- Read our [Blog](https://blog.styleforge.ai)

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## ❓ Questions?

Feel free to:
- Open a [Discussion](https://github.com/mrningzeoutlook-pixel/styleforge-ai/discussions)
- Ask in [Discord](https://discord.gg/styleforge)
- Contact maintainers directly

Thank you for contributing to StyleForge AI! 🎉
