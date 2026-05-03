"""
Tests for StyleForgePipeline.
"""

import pytest
import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from styleforge import StyleForgePipeline
from styleforge.config.platforms import get_platform


class TestStyleForgePipelineInit:
    """Test StyleForgePipeline initialization."""
    
    def test_default_init(self):
        """Test initialization with default parameters."""
        pipeline = StyleForgePipeline()
        
        assert pipeline.output_dir == "./output"
        assert pipeline.analysis_agent is not None
        assert pipeline.scene_agent is not None
        assert pipeline.adapter_agent is not None
        assert pipeline.video_agent is not None
    
    def test_custom_init(self):
        """Test initialization with custom parameters."""
        custom_output = "./custom_output"
        pipeline = StyleForgePipeline(output_dir=custom_output)
        
        assert pipeline.output_dir == custom_output
    
    def test_init_creates_output_dir(self):
        """Test that initialization creates output directory."""
        output_dir = "./test_output"
        
        # Clean up if exists
        import shutil
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        
        pipeline = StyleForgePipeline(output_dir=output_dir)
        
        assert os.path.exists(output_dir)
        
        # Cleanup
        shutil.rmtree(output_dir)


class TestStyleForgePipelineRun:
    """Test StyleForgePipeline.run() method."""
    
    @pytest.fixture
    def pipeline(self):
        """Create a pipeline instance for testing."""
        return StyleForgePipeline(output_dir="./test_output")
    
    @pytest.fixture
    def mock_image(self, tmp_path):
        """Create a mock image file for testing."""
        img_path = tmp_path / "test_garment.jpg"
        img_path.write_bytes(b"mock_image_data")
        return str(img_path)
    
    def test_run_with_valid_input(self, pipeline, mock_image):
        """Test running pipeline with valid input."""
        # Note: This test uses mock data
        # In real scenario, you'd have actual image and API keys
        pass  # Placeholder - actual implementation would need mocking
    
    def test_run_with_invalid_input(self, pipeline):
        """Test running pipeline with non-existent input."""
        with pytest.raises(FileNotFoundError):
            pipeline.run(
                input_path="nonexistent.jpg",
                platforms=["xiaohongshu"],
            )
    
    def test_run_with_invalid_platform(self, pipeline, mock_image):
        """Test running pipeline with invalid platform name."""
        import io
        import contextlib
        
        # Capture output to check warning
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                results = pipeline.run(
                    input_path=mock_image,
                    platforms=["invalid_platform"],
                    output_dir="./test_output",
                )
            
            output = buf.getvalue()
        
        # Should have warning in output
        assert "Warning" in output or "invalid" in output.lower()
        # Results should be empty (no valid platforms)
        assert len(results) == 0


class TestStyleForgePipelineSaveManifest:
    """Test manifest saving functionality."""
    
    @pytest.fixture
    def pipeline(self):
        """Create a pipeline instance."""
        return StyleForgePipeline(output_dir="./test_output")
    
    def test_save_manifest_creates_file(self, pipeline):
        """Test that _save_manifest creates a JSON file."""
        # Mock results
        results = {
            "xiaohongshu": {
                "images": ["img1.png", "img2.png"],
                "video": "video.mp4",
                "config": get_platform("xiaohongshu"),
            }
        }
        
        output_dir = "./test_output"
        pipeline._save_manifest(results, output_dir)
        
        manifest_path = os.path.join(output_dir, "manifest.json")
        assert os.path.exists(manifest_path)
        
        # Verify JSON content
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
        
        assert "generated_at" in manifest
        assert "pipeline_version" in manifest
        assert "results" in manifest
        
        # Cleanup
        os.remove(manifest_path)
    
    def test_save_manifest_content(self, pipeline):
        """Test manifest JSON structure."""
        results = {
            "xiaohongshu": {
                "images": ["img1.png"],
                "video": None,
                "config": get_platform("xiaohongshu"),
            }
        }
        
        output_dir = "./test_output"
        pipeline._save_manifest(results, output_dir)
        
        manifest_path = os.path.join(output_dir, "manifest.json")
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
        
        # Check structure
        assert "xiaohongshu" in manifest["results"]
        platform_data = manifest["results"]["xiaohongshu"]
        assert "images" in platform_data
        assert "video" in platform_data
        assert "platform_config" in platform_data
        
        # Cleanup
        os.remove(manifest_path)


class TestStyleForgePipelineGetSupportedPlatforms:
    """Test get_supported_platforms method."""
    
    def test_get_supported_platforms(self):
        """Test that supported platforms are returned."""
        pipeline = StyleForgePipeline()
        platforms = pipeline.get_supported_platforms()
        
        assert isinstance(platforms, list)
        assert len(platforms) > 0
        assert "xiaohongshu" in platforms


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
