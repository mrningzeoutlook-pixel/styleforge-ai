#!/usr/bin/env python3
"""
StyleForge AI - Command Line Interface

AI-powered content generation pipeline for social commerce.
Upload flat-lay photos, get platform-ready content for Xiaohongshu, Douyin and more.
"""

import sys
import os
import argparse
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from styleforge import StyleForgePipeline
from styleforge.config.platforms import list_platforms, get_platform


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="StyleForge AI - Social Commerce Content Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate content for a single product
  python styleforge.py --input ./photos/garment.jpg --platforms xiaohongshu,douyin
  
  # Skip video generation
  python styleforge.py --input ./photos/garment.jpg --no-video
  
  # Batch process multiple images
  python styleforge.py --batch ./photos/*.jpg --platforms xiaohongshu
  
  # List supported platforms
  python styleforge.py --list-platforms

For more information, visit: https://github.com/mrningzeoutlook-pixel/styleforge-ai
        """
    )
    
    # Input options (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--input", "-i", help="Path to flat-lay garment photo")
    input_group.add_argument("--batch", "-b", nargs="+", help="Batch process multiple images")
    input_group.add_argument("--list-platforms", "-l", action="store_true", help="List supported platforms")
    
    # Platform options
    parser.add_argument("--platforms", "-p", default="xiaohongshu,douyin",
                       help="Comma-separated list of target platforms (default: xiaohongshu,douyin)")
    
    # Output options
    parser.add_argument("--output", "-o", default="./output", help="Output directory (default: ./output)")
    parser.add_argument("--variants", "-v", type=int, default=3, help="Number of image variants per platform (default: 3)")
    
    # Processing options
    parser.add_argument("--no-video", action="store_true", help="Skip video generation")
    parser.add_argument("--no-cache", action="store_true", help="Disable caching")
    
    # Logging options
    parser.add_argument("--verbose", "-V", action="store_true", help="Verbose output")
    parser.add_argument("--quiet", "-q", action="store_true", help="Quiet mode (errors only)")
    
    args = parser.parse_args()
    
    # Handle --list-platforms
    if args.list_platforms:
        print("Supported platforms:\n")
        for platform_name in list_platforms():
            platform = get_platform(platform_name)
            print(f"  {platform_name:15} - {platform.display_name}")
            print(f"  {'':15}   {platform.aspect_ratio} | {platform.image_width}x{platform.image_height}")
            print()
        return 0
    
    # Validate platforms
    platforms = [p.strip() for p in args.platforms.split(",")]
    invalid_platforms = [p for p in platforms if get_platform(p) is None]
    
    if invalid_platforms:
        print(f"Error: Invalid platform(s): {', '.join(invalid_platforms)}")
        print(f"Supported platforms: {', '.join(list_platforms())}")
        return 1
    
    # Initialize pipeline
    pipeline = StyleForgePipeline(output_dir=args.output)
    
    # Process single image or batch
    if args.input:
        if not os.path.exists(args.input):
            print(f"Error: Input file not found: {args.input}")
            return 1
        
        print(f"\n📸 Processing single image: {args.input}\n")
        results = pipeline.run(
            input_path=args.input,
            platforms=platforms,
            output_dir=args.output,
            num_variants=args.variants,
            generate_video=not args.no_video,
        )
        
    else:  # batch mode
        print(f"\n📸 Processing batch: {len(args.batch)} images\n")
        
        # Validate all input files exist
        missing = [f for f in args.batch if not os.path.exists(f)]
        if missing:
            print(f"Error: Missing input files:")
            for f in missing:
                print(f"  - {f}")
            return 1
        
        results = pipeline.run_batch(
            input_paths=args.batch,
            platforms=platforms,
            output_dir=args.output,
            num_variants=args.variants,
            generate_video=not args.no_video,
        )
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 Generation Summary")
    print("=" * 60)
    
    for platform_name, content in results.items():
        if isinstance(content, dict) and "error" in content:
            print(f"\n❌ {platform_name}:")
            print(f"   Error: {content['error']}")
        else:
            platform_config = content.get("config")
            images = content.get("images", [])
            video = content.get("video")
            
            print(f"\n✅ {platform_config.display_name if platform_config else platform_name}:")
            print(f"   Images: {len(images)}")
            if video:
                print(f"   Video: {video}")
    
    print("\n" + "=" * 60)
    print(f"📁 Output directory: {os.path.abspath(args.output)}")
    print("=" * 60 + "\n")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
