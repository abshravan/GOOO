"""
Utility Functions Module
Helper functions for the application
"""

import os
import tempfile
from typing import Optional


def save_uploaded_file(uploaded_file) -> str:
    """
    Save uploaded file to a temporary location.

    Args:
        uploaded_file: Gradio UploadedFile object

    Returns:
        Path to saved temporary file
    """
    if uploaded_file is None:
        raise ValueError("No file uploaded")

    # If it's already a file path (string), return it
    if isinstance(uploaded_file, str):
        return uploaded_file

    # Otherwise, it should have a name attribute
    return uploaded_file


def validate_file_type(file_path: str, allowed_extensions: list = ['.pdf', '.docx', '.doc']) -> bool:
    """
    Validate that file has an allowed extension.

    Args:
        file_path: Path to file
        allowed_extensions: List of allowed file extensions

    Returns:
        True if file type is valid, False otherwise
    """
    if not file_path:
        return False

    file_ext = os.path.splitext(file_path)[1].lower()
    return file_ext in allowed_extensions


def truncate_text(text: str, max_length: int = 10000) -> str:
    """
    Truncate text to maximum length to avoid token limits.

    Args:
        text: Input text
        max_length: Maximum character length

    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text

    return text[:max_length] + "\n\n[... Text truncated due to length ...]"


def format_error_message(error: Exception) -> str:
    """
    Format error message for display to user.

    Args:
        error: Exception object

    Returns:
        Formatted error message
    """
    error_msg = str(error)

    # Check for common errors and provide helpful messages
    if "Cannot connect to Ollama" in error_msg:
        return (
            "❌ **Cannot connect to Ollama**\n\n"
            "Please ensure Ollama is running:\n"
            "1. Install Ollama from https://ollama.ai\n"
            "2. Run: `ollama serve`\n"
            "3. Pull a model: `ollama pull llama3.1`\n"
            "4. Try again"
        )
    elif "File not found" in error_msg or "No file uploaded" in error_msg:
        return "❌ **File Error**\n\nPlease upload a valid resume file (PDF or DOCX)."
    elif "Unsupported file format" in error_msg:
        return "❌ **Unsupported File Format**\n\nPlease upload a PDF or DOCX file."
    elif "Error extracting text" in error_msg:
        return f"❌ **File Parsing Error**\n\n{error_msg}\n\nThe file might be corrupted or password-protected."
    elif "timed out" in error_msg.lower():
        return "❌ **Request Timeout**\n\nThe LLM took too long to respond. Try again or use a faster model."
    else:
        return f"❌ **Error**\n\n{error_msg}"


def format_success_message(message: str) -> str:
    """
    Format success message for display.

    Args:
        message: Success message

    Returns:
        Formatted success message
    """
    return f"✅ {message}"


def clean_llm_output(text: str) -> str:
    """
    Clean up LLM output by removing excessive whitespace and formatting issues.

    Args:
        text: Raw LLM output

    Returns:
        Cleaned text
    """
    # Remove excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Remove trailing whitespace from lines
    lines = [line.rstrip() for line in text.split('\n')]
    text = '\n'.join(lines)

    return text.strip()


def estimate_tokens(text: str) -> int:
    """
    Rough estimation of token count (4 characters ≈ 1 token).

    Args:
        text: Input text

    Returns:
        Estimated token count
    """
    return len(text) // 4


def check_text_length(text: str, max_tokens: int = 8000) -> tuple:
    """
    Check if text is within token limits.

    Args:
        text: Input text
        max_tokens: Maximum allowed tokens

    Returns:
        Tuple of (is_valid, estimated_tokens, message)
    """
    estimated = estimate_tokens(text)

    if estimated > max_tokens:
        return (
            False,
            estimated,
            f"Text is too long ({estimated} estimated tokens). Maximum is {max_tokens} tokens. "
            "Consider uploading a shorter resume."
        )

    return (True, estimated, "OK")


# Import re for clean_llm_output function
import re
