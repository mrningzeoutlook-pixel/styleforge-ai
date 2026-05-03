"""
StyleForge AI - Social Commerce Content Generation Pipeline

A multi-agent AI system for automating content creation for cross-border e-commerce.
"""

__version__ = "0.2.0"
__author__ = "Mary Ma"
__email__ = "mary@styleforge.ai"
__license__ = "MIT"

from .pipeline import StyleForgePipeline
from .config.platforms import PLATFORMS, PlatformConfig

__all__ = [
    "StyleForgePipeline",
    "PLATFORMS",
    "PlatformConfig",
]
