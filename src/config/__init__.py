"""
Configuration package for StyleForge AI.

Exports platform configurations and utilities.
"""

from .platforms import PlatformConfig, PLATFORMS, get_platform, list_platforms, add_platform

__all__ = [
    "PlatformConfig",
    "PLATFORMS",
    "get_platform",
    "list_platforms",
    "add_platform",
]
