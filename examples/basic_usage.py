"""
Example: Generate content for a single product.

This example demonstrates the basic usage of StyleForge AI
to generate social commerce content from a flat-lay photo.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from styleforge import StyleForgePipeline


def main():
    """Run example: Single product content generation."""
    print("=" * 60)
    print("Example: Single Product Content Generation")
    print("=" * 60 + "\n")
    
    # Initialize pipeline
    pipeline = StyleForgePipeline(output_dir="./output")
    
    # Define input
    input_image = "./examples/input/sample_garment.jpg"
    
    # Check if input exists (for demo, we'll mock it)
    if not os.path.exists(input_image):
        print(f"Note: {input_image} not found. Using mock data.\n")
        # In real usage, you would have an actual image file
        input_image = "mock_image.jpg"
    
    # Define target platforms
    platforms = ["xiaohongshu", "douyin"]
    
    print(f"Input: {input_image}")
    print(f"Platforms: {', '.join(platforms)}")
    print(f"Variants per platform: 3")
    print(f"Generate video: Yes\n")
    
    # Run pipeline (commented out as this is an example)
    # In real usage, uncomment the following lines:
    """
    results = pipeline.run(
        input_path=input_image,
        platforms=platforms,
        output_dir="./output",
        num_variants=3,
        generate_video=True,
    )
    
    # Print results
    print("\n" + "=" * 60)
    print("Results:")
    print("=" * 60)
    
    for platform_name, content in results.items():
        print(f"\n{platform_name}:")
        print(f"  Images: {len(content['images'])}")
        for img in content['images']:
            print(f"    - {img}")
        
        if content['video']:
            print(f"  Video: {content['video']}")
    """
    
    print("\n✓ Example completed (mock mode)")
    print("\nTo run with real images:")
    print("  1. Place your flat-lay photos in ./photos/")
    print("  2. Run: python styleforge.py --input ./photos/your_garment.jpg")
    print("=" * 60)


if __name__ == "__main__":
    main()
