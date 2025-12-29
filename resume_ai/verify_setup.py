"""
Setup Verification Script
Checks if all files are present and the basic structure is correct
"""

import os
import sys


def check_file_exists(filename):
    """Check if a file exists in the current directory."""
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"✅ {filename:<25} ({size:>6} bytes)")
        return True
    else:
        print(f"❌ {filename:<25} MISSING")
        return False


def check_directory_structure():
    """Verify all required files are present."""
    print("=" * 60)
    print("Resume AI Project - Setup Verification")
    print("=" * 60)
    print()

    required_files = [
        "app.py",
        "llm.py",
        "resume_parser.py",
        "skill_extractor.py",
        "job_roles.py",
        "prompts.py",
        "utils.py",
        "requirements.txt",
        "README.md"
    ]

    print("Checking required files:")
    print("-" * 60)

    all_present = True
    for filename in required_files:
        if not check_file_exists(filename):
            all_present = False

    print("-" * 60)
    print()

    if all_present:
        print("✅ All required files are present!")
        print()
        print("Next steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Install Ollama: https://ollama.ai")
        print("3. Pull a model: ollama pull llama3.1")
        print("4. Start Ollama: ollama serve")
        print("5. Run the app: python app.py")
        print()
        return 0
    else:
        print("❌ Some files are missing. Please check the project structure.")
        print()
        return 1


if __name__ == "__main__":
    exit_code = check_directory_structure()
    sys.exit(exit_code)
