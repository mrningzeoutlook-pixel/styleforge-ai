"""
Platform configurations for StyleForge AI.

Defines aspect ratios, resolutions, style prompts, and other
platform-specific settings for social commerce content generation.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class PlatformConfig:
    """Configuration for a social media platform.
    
    Attributes:
        name: Platform identifier (e.g., "xiaohongshu")
        display_name: Human-readable name (e.g., "小红书")
        aspect_ratio: Aspect ratio string (e.g., "3:4")
        image_width: Target image width in pixels
        image_height: Target image height in pixels
        video_duration: Target video duration in seconds
        style_prompt: AI prompt for generating platform-appropriate style
        music_genre: Recommended music genre for videos
        target_audience: Primary audience description
    """
    
    name: str
    display_name: str = ""
    aspect_ratio: str = "1:1"
    image_width: int = 1080
    image_height: int = 1080
    video_duration: float = 8.0
    style_prompt: str = "high quality, professional"
    music_genre: str = "pop"
    target_audience: str = "general"


# Platform-specific configurations
PLATFORMS = {
    "xiaohongshu": PlatformConfig(
        name="xiaohongshu",
        display_name="小红书",
        aspect_ratio="3:4",
        image_width=1080,
        image_height=1440,
        video_duration=8.0,
        style_prompt="warm, lifestyle, aesthetic, soft lighting, cozy atmosphere, Chinese social media style, premium feel",
        music_genre="lo-fi, chill, ambient",
        target_audience="Chinese millennials, fashion enthusiasts",
    ),
    "douyin": PlatformConfig(
        name="douyin",
        display_name="抖音",
        aspect_ratio="9:16",
        image_width=1080,
        image_height=1920,
        video_duration=8.0,
        style_prompt="trendy, dynamic, bold colors, fashion-forward, Gen-Z aesthetic, energetic",
        music_genre="trending Chinese pop, electronic",
        target_audience="Gen Z, trend-conscious consumers",
    ),
    "tiktok": PlatformConfig(
        name="tiktok",
        display_name="TikTok",
        aspect_ratio="9:16",
        image_width=1080,
        image_height=1920,
        video_duration=8.0,
        style_prompt="viral, energetic, global fashion, inclusive, body-positive, diverse representation",
        music_genre="global pop, hip-hop, trending",
        target_audience="Global Gen Z, body-positive community",
    ),
    "instagram": PlatformConfig(
        name="instagram",
        display_name="Instagram",
        aspect_ratio="4:5",
        image_width=1080,
        image_height=1350,
        video_duration=8.0,
        style_prompt="curated, premium, minimal aesthetic, editorial quality, Instagram-worthy, sophisticated",
        music_genre="indie, alternative, sophisticated",
        target_audience="Aesthetic-conscious, premium market",
    ),
    "youtube_shorts": PlatformConfig(
        name="youtube_shorts",
        display_name="YouTube Shorts",
        aspect_ratio="9:16",
        image_width=1080,
        image_height=1920,
        video_duration=60.0,  # YouTube Shorts allows up to 60s
        style_prompt="dynamic, engaging, YouTube-optimized, energetic, hook-driven",
        music_genre="trending, upbeat, engaging",
        target_audience="YouTube viewers, short-form content consumers",
    ),
}


def get_platform(name: str) -> Optional[PlatformConfig]:
    """Get platform configuration by name.
    
    Args:
        name: Platform name (e.g., "xiaohongshu")
        
    Returns:
        PlatformConfig if found, None otherwise
    """
    return PLATFORMS.get(name)


def list_platforms() -> list[str]:
    """List all supported platform names.
    
    Returns:
        List of platform names
    """
    return list(PLATFORMS.keys())


def add_platform(name: str, config: PlatformConfig) -> None:
    """Add a new platform configuration.
    
    Args:
        name: Platform name
        config: PlatformConfig object
    """
    PLATFORMS[name] = config
