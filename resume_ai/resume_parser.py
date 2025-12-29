"""
Resume Parser Module
Extracts text from PDF and DOCX files
"""

import os
from typing import Optional
import pdfplumber
from docx import Document


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file using pdfplumber.

    Args:
        file_path: Path to the PDF file

    Returns:
        Extracted text as a string
    """
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip()
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {str(e)}")


def extract_text_from_docx(file_path: str) -> str:
    """
    Extract text from a DOCX file using python-docx.

    Args:
        file_path: Path to the DOCX file

    Returns:
        Extracted text as a string
    """
    try:
        doc = Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        raise ValueError(f"Error extracting text from DOCX: {str(e)}")


def parse_resume(file_path: str) -> str:
    """
    Parse resume from PDF or DOCX file.

    Args:
        file_path: Path to the resume file

    Returns:
        Extracted text from the resume

    Raises:
        ValueError: If file format is not supported or extraction fails
    """
    if not os.path.exists(file_path):
        raise ValueError(f"File not found: {file_path}")

    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == ".pdf":
        return extract_text_from_pdf(file_path)
    elif file_extension in [".docx", ".doc"]:
        return extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}. Only PDF and DOCX are supported.")


def validate_resume_text(text: str) -> bool:
    """
    Validate if extracted text is meaningful.

    Args:
        text: Extracted resume text

    Returns:
        True if text appears valid, False otherwise
    """
    if not text or len(text.strip()) < 50:
        return False
    return True
