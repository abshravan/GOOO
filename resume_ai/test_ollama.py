"""
Ollama Connection Diagnostic Script
Tests connection to Ollama and provides troubleshooting information
"""

import requests
import json


def test_ollama_connection():
    """Test connection to Ollama and diagnose issues."""

    print("=" * 70)
    print("OLLAMA CONNECTION DIAGNOSTIC")
    print("=" * 70)
    print()

    base_url = "http://localhost:11434"

    # Test 1: Check if Ollama is running
    print("Test 1: Checking if Ollama is running...")
    print("-" * 70)
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        print(f"✅ Ollama is responding on {base_url}")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text[:100]}")
    except requests.exceptions.ConnectionError:
        print(f"❌ Cannot connect to Ollama on {base_url}")
        print("\n💡 Solution:")
        print("   1. Check if Ollama is installed: ollama --version")
        print("   2. Start Ollama service: ollama serve")
        print("   3. Or check if it's running on a different port")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

    print()

    # Test 2: List available models
    print("Test 2: Checking available models...")
    print("-" * 70)
    try:
        response = requests.get(f"{base_url}/api/tags", timeout=5)
        if response.status_code == 200:
            data = response.json()
            models = data.get("models", [])

            if models:
                print(f"✅ Found {len(models)} model(s):")
                for model in models:
                    print(f"   - {model.get('name', 'Unknown')}")
            else:
                print("⚠️  No models installed")
                print("\n💡 Solution:")
                print("   Pull a model: ollama pull llama3.1")
                return False
        else:
            print(f"❌ Error listing models. Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

    print()

    # Test 3: Test generate endpoint
    print("Test 3: Testing generate endpoint...")
    print("-" * 70)
    try:
        # Use the first available model
        test_model = models[0].get('name') if models else 'llama3.1'

        payload = {
            "model": test_model,
            "prompt": "Say 'hello' in one word",
            "stream": False,
            "options": {
                "num_predict": 10
            }
        }

        print(f"   Using model: {test_model}")
        print(f"   Sending request to: {base_url}/api/generate")

        response = requests.post(
            f"{base_url}/api/generate",
            json=payload,
            timeout=30
        )

        print(f"   Status Code: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            generated_text = result.get("response", "")
            print(f"✅ Generate endpoint working!")
            print(f"   Response: {generated_text[:100]}")
            print()
            print("=" * 70)
            print("✅ ALL TESTS PASSED - Ollama is working correctly!")
            print("=" * 70)
            return True
        elif response.status_code == 404:
            print(f"❌ 404 Error - Generate endpoint not found")
            print(f"\n💡 This might mean:")
            print(f"   1. Ollama version is outdated")
            print(f"   2. API endpoint has changed")
            print(f"   3. Try updating Ollama: curl -fsSL https://ollama.ai/install.sh | sh")
            print(f"\n   Response: {response.text}")
            return False
        else:
            print(f"❌ Error. Status: {response.status_code}")
            print(f"   Response: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

    print()


def check_ollama_version():
    """Try to get Ollama version information."""
    print("\nChecking Ollama version...")
    print("-" * 70)

    import subprocess
    try:
        result = subprocess.run(
            ["ollama", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print(f"✅ Ollama Version: {result.stdout.strip()}")
        else:
            print(f"⚠️  Could not get version: {result.stderr}")
    except FileNotFoundError:
        print("❌ Ollama command not found in PATH")
        print("\n💡 Install Ollama from: https://ollama.ai")
    except Exception as e:
        print(f"⚠️  Error checking version: {e}")

    print()


def main():
    """Run all diagnostics."""
    check_ollama_version()
    success = test_ollama_connection()

    if not success:
        print("\n" + "=" * 70)
        print("TROUBLESHOOTING GUIDE")
        print("=" * 70)
        print("""
1. Install Ollama (if not installed):
   • Visit: https://ollama.ai
   • Or run: curl -fsSL https://ollama.ai/install.sh | sh

2. Start Ollama service:
   • Run in terminal: ollama serve
   • Leave it running in the background

3. Pull a model:
   • Run: ollama pull llama3.1
   • Or: ollama pull llama3.2

4. Verify Ollama is running:
   • Open: http://localhost:11434 in your browser
   • Should see "Ollama is running"

5. Check logs:
   • Look for errors when running 'ollama serve'
   • Check if another instance is already running

6. Port conflicts:
   • Ollama uses port 11434 by default
   • Check if something else is using this port
        """)


if __name__ == "__main__":
    main()
