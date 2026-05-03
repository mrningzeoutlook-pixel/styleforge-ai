"""
Main Pipeline Orchestration for StyleForge AI.

Coordinates all agents to complete the full content generation workflow.
"""

from typing import Dict, Any, List, Optional
import os
import json
from pathlib import Path
from datetime import datetime

from .agents import (
    ImageAnalysisAgent,
    SceneGenerationAgent,
    PlatformAdapterAgent,
    VideoSynthesisAgent,
)
from .config.platforms import get_platform, list_platforms


class StyleForgePipeline:
    """Main pipeline orchestrating all agents for social commerce content generation.
    
    This class coordinates the entire workflow:
    1. Image Analysis
    2. Scene Generation
    3. Platform Adaptation
    4. Video Synthesis (optional)
    
    Attributes:
        analysis_agent: Agent for image analysis
        scene_agent: Agent for scene generation
        adapter_agent: Agent for platform adaptation
        video_agent: Agent for video synthesis
        output_dir: Default output directory
    """
    
    def __init__(self, output_dir: str = "./output", 
                 analysis_agent: Optional[Any] = None,
                 scene_agent: Optional[Any] = None,
                 adapter_agent: Optional[Any] = None,
                 video_agent: Optional[Any] = None):
        """Initialize StyleForgePipeline.
        
        Args:
            output_dir: Default output directory for generated content
            analysis_agent: Custom ImageAnalysisAgent (uses default if None)
            scene_agent: Custom SceneGenerationAgent (uses default if None)
            adapter_agent: Custom PlatformAdapterAgent (uses default if None)
            video_agent: Custom VideoSynthesisAgent (uses default if None)
        """
        self.analysis_agent = analysis_agent or ImageAnalysisAgent()
        self.scene_agent = scene_agent or SceneGenerationAgent()
        self.adapter_agent = adapter_agent or PlatformAdapterAgent()
        self.video_agent = video_agent or VideoSynthesisAgent()
        self.output_dir = output_dir
        
        os.makedirs(output_dir, exist_ok=True)
    
    def run(self, input_path: str, platforms: List[str], 
            output_dir: Optional[str] = None,
            num_variants: int = 3, generate_video: bool = True) -> Dict[str, Any]:
        """Run the full StyleForge AI pipeline.
        
        Args:
            input_path: Path to the flat-lay garment photo
            platforms: List of target platform names
            output_dir: Output directory (overrides default)
            num_variants: Number of image variants per platform
            generate_video: Whether to generate beat-synced videos
            
        Returns:
            Dictionary of generated content organized by platform:
                {
                    "xiaohongshu": {
                        "images": [path1, path2, ...],
                        "video": path_or_None,
                        "config": PlatformConfig
                    },
                    ...
                }
                
        Raises:
            FileNotFoundError: If input_path doesn't exist
            ValueError: If platform name is invalid
        """
        output_dir = output_dir or self.output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        print("=" * 60)
        print("StyleForge AI - Social Commerce Content Generator")
        print("=" * 60)
        print(f"Input: {input_path}")
        print(f"Platforms: {', '.join(platforms)}")
        print(f"Variants per platform: {num_variants}")
        print(f"Generate video: {generate_video}")
        print("=" * 60)
        
        # Step 1: Analyze the input image
        print("\n[Step 1/4] Analyzing garment features...")
        features = self.analysis_agent.analyze(input_path)
        
        results = {}
        
        for platform_name in platforms:
            platform = get_platform(platform_name)
            if platform is None:
                print(f"Warning: Unknown platform '{platform_name}', skipping...")
                continue
            
            print(f"\n--- Processing for {platform.display_name or platform.name} ---")
            
            # Step 2: Generate scene images
            print("\n[Step 2/4] Generating scene images...")
            images = self.scene_agent.generate(features, platform, num_variants)
            
            # Step 3: Adapt for platform
            print("\n[Step 3/4] Adapting for platform...")
            adapted = self.adapter_agent.adapt(images, platform)
            
            # Step 4: Generate video (optional)
            video_path = None
            if generate_video:
                print("\n[Step 4/4] Creating beat-synced video...")
                video_path = self.video_agent.create_video(adapted, platform)
            
            results[platform_name] = {
                "images": adapted,
                "video": video_path,
                "config": platform,
            }
        
        print("\n" + "=" * 60)
        print(f"✓ Pipeline complete! Generated content for: {', '.join(results.keys())}")
        print("=" * 60)
        
        # Save results manifest
        self._save_manifest(results, output_dir)
        
        return results
    
    def run_batch(self, input_paths: List[str], platforms: List[str],
                   output_dir: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """Run pipeline on multiple input images.
        
        Args:
            input_paths: List of paths to flat-lay photos
            platforms: List of target platform names
            output_dir: Output directory
            **kwargs: Additional arguments passed to run()
            
        Returns:
            Nested dictionary: {input_path: {platform: results}}
        """
        batch_results = {}
        
        for input_path in input_paths:
            print(f"\n\nProcessing: {input_path}")
            print("=" * 60)
            
            try:
                results = self.run(input_path, platforms, output_dir, **kwargs)
                batch_results[input_path] = results
            except Exception as e:
                print(f"Error processing {input_path}: {e}")
                batch_results[input_path] = {"error": str(e)}
        
        return batch_results
    
    def _save_manifest(self, results: Dict[str, Any], output_dir: str) -> None:
        """Save results manifest to JSON file.
        
        Args:
            results: Pipeline results dictionary
            output_dir: Output directory
        """
        manifest = {
            "generated_at": datetime.now().isoformat(),
            "pipeline_version": "0.2.0",
            "results": {}
        }
        
        for platform_name, content in results.items():
            manifest["results"][platform_name] = {
                "images": content["images"],
                "video": content["video"],
                "platform_config": {
                    "name": content["config"].name,
                    "aspect_ratio": content["config"].aspect_ratio,
                    "resolution": f"{content['config'].image_width}x{content['config'].image_height}"
                }
            }
        
        manifest_path = os.path.join(output_dir, "manifest.json")
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Manifest saved to: {manifest_path}")
    
    def get_supported_platforms(self) -> List[str]:
        """Get list of supported platform names.
        
        Returns:
            List of platform names
        """
        return list_platforms()
