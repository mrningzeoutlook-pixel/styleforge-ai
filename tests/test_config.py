"""
Tests for StyleForge AI configuration module.
"""

import pytest
from src.config.platforms import PlatformConfig, PLATFORMS, get_platform, list_platforms, add_platform


class TestPlatformConfig:
    """Test PlatformConfig dataclass."""
    
    def test_create_platform_config(self):
        """Test creating a PlatformConfig instance."""
        config = PlatformConfig(
            name="test_platform",
            display_name="Test Platform",
            aspect_ratio="1:1",
            image_width=1080,
            image_height=1080,
            video_duration=8.0,
            style_prompt="test style",
        )
        
        assert config.name == "test_platform"
        assert config.display_name == "Test Platform"
        assert config.aspect_ratio == "1:1"
        assert config.image_width == 1080
        assert config.image_height == 1080
        assert config.video_duration == 8.0
    
    def test_default_values(self):
        """Test default values of PlatformConfig."""
        config = PlatformConfig(name="test")
        
        assert config.display_name == ""
        assert config.aspect_ratio == "1:1"
        assert config.image_width == 1080
        assert config.image_height == 1080


class TestGetPlatform:
    """Test get_platform function."""
    
    def test_get_existing_platform(self):
        """Test getting an existing platform."""
        config = get_platform("xiaohongshu")
        
        assert config is not None
        assert config.name == "xiaohongshu"
        assert config.display_name == "小红书"
    
    def test_get_nonexistent_platform(self):
        """Test getting a non-existent platform."""
        config = get_platform("nonexistent")
        
        assert config is None


class TestListPlatforms:
    """Test list_platforms function."""
    
    def test_list_platforms_returns_list(self):
        """Test that list_platforms returns a list."""
        platforms = list_platforms()
        
        assert isinstance(platforms, list)
        assert len(platforms) > 0
        assert "xiaohongshu" in platforms
    
    def test_list_platforms_contains_all(self):
        """Test that all expected platforms are listed."""
        platforms = list_platforms()
        
        expected = ["xiaohongshu", "douyin", "tiktok", "instagram"]
        for p in expected:
            assert p in platforms


class TestAddPlatform:
    """Test add_platform function."""
    
    def test_add_new_platform(self):
        """Test adding a new platform."""
        new_config = PlatformConfig(
            name="test_new",
            display_name="Test New",
            aspect_ratio="16:9",
            image_width=1920,
            image_height=1080,
        )
        
        # Add platform
        add_platform("test_new", new_config)
        
        # Verify it was added
        retrieved = get_platform("test_new")
        assert retrieved is not None
        assert retrieved.name == "test_new"
        assert retrieved.display_name == "Test New"
        
        # Cleanup: Remove from PLATFORMS dict
        from src.config.platforms import PLATFORMS
        del PLATFORMS["test_new"]


class TestPLATFORMSConstant:
    """Test PLATFORMS constant."""
    
    def test_xiaohongshu_config(self):
        """Test Xiaohongshu platform configuration."""
        config = PLATFORMS["xiaohongshu"]
        
        assert config.aspect_ratio == "3:4"
        assert config.image_width == 1080
        assert config.image_height == 1440
        assert config.video_duration == 8.0
        assert "warm" in config.style_prompt
    
    def test_douyin_config(self):
        """Test Douyin platform configuration."""
        config = PLATFORMS["douyin"]
        
        assert config.aspect_ratio == "9:16"
        assert config.image_width == 1080
        assert config.image_height == 1920
        assert "trendy" in config.style_prompt
    
    def test_instagram_config(self):
        """Test Instagram platform configuration."""
        config = PLATFORMS["instagram"]
        
        assert config.aspect_ratio == "4:5"
        assert config.image_width == 1080
        assert config.image_height == 1350
        assert "curated" in config.style_prompt
