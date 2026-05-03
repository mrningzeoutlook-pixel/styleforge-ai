"""
Utilities package for StyleForge AI.

Common utility functions for image processing, video processing, and file I/O.
"""

from typing import Optional
import os


def ensure_dir(path: str) -> str:
    """Ensure directory exists, create if not.
    
    Args:
        path: Directory path
        
    Returns:
        Absolute path to directory
    """
    abs_path = os.path.abspath(path)
    os.makedirs(abs_path, exist_ok=True)
    return abs_path


def get_file_extension(filename: str) -> str:
    """Get file extension (lowercase, without dot).
    
    Args:
        filename: Filename or path
        
    Returns:
        Extension string (e.g., "png", "jpg")
    """
    return os.path.splitext(filename)[1].lower().lstrip('.')


def is_image_file(filename: str) -> bool:
    """Check if file is an image based on extension.
    
    Args:
        filename: Filename or path
        
    Returns:
        True if image file, False otherwise
    """
    image_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp', 'tiff'}
    return get_file_extension(filename) in image_extensions


def is_video_file(filename: str) -> bool:
    """Check if file is a video based on extension.
    
    Args:
        filename: Filename or path
        
    Returns:
        True if video file, False otherwise
    """
    video_extensions = {'mp4', 'avi', 'mov', 'mkv', 'webm', 'flv', 'wmv'}
    return get_file_extension(filename) in video_extensions


def format_file_size(size_bytes: int) -> str:
    """Format file size in human-readable format.
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted string (e.g., "1.5 MB", "2.3 GB")
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"


def safe_filename(filename: str, replacement: str = "_") -> str:
    """Create safe filename by removing/replacing invalid characters.
    
    Args:
        filename: Original filename
        replacement: Replacement character for invalid chars
        
    Returns:
        Safe filename
    """
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    safe = filename
    for char in invalid_chars:
        safe = safe.replace(char, replacement)
    return safe
