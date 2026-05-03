from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="styleforge-ai",
    version="0.2.0",
    author="Mary Ma",
    author_email="mary@styleforge.ai",
    description="AI-powered content generation pipeline for social commerce",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrningzeoutlook-pixel/styleforge-ai",
    project_urls={
        "Bug Tracker": "https://github.com/mrningzeoutlook-pixel/styleforge-ai/issues",
        "Documentation": "https://github.com/mrningzeoutlook-pixel/styleforge-ai/docs",
        "Source Code": "https://github.com/mrningzeoutlook-pixel/styleforge-ai",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.11",
    install_requires=[
        "python-dotenv>=1.0.0",
        "Pillow>=10.0.0",
        "openai>=1.0.0",
        "replicate>=0.15.0",
        "moviepy>=1.0.3",
        "numpy>=1.24.0",
        "requests>=2.31.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "mypy>=1.5.0",
            "flake8>=6.0.0",
            "black>=23.7.0",
            "isort>=5.12.0",
        ],
        "api": [
            "fastapi>=0.101.0",
            "uvicorn>=0.23.0",
            "pydantic>=2.0.0",
        ],
        "worker": [
            "celery>=5.3.0",
            "redis>=5.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "styleforge=styleforge:main",
        ],
    },
    include_package_data=True,
    package_data={
        "styleforge": ["py.typed"],
    },
)
