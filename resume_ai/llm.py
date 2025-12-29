"""
Ollama LLM Client Module
Handles interaction with local Ollama HTTP API
"""

import requests
import json
from typing import Optional, Dict, Any


class OllamaClient:
    """Client for interacting with Ollama HTTP API."""

    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3.1"):
        """
        Initialize Ollama client.

        Args:
            base_url: Base URL for Ollama API
            model: Model name to use (default: llama3.1)
        """
        self.base_url = base_url.rstrip('/')
        self.model = model
        self.generate_url = f"{self.base_url}/api/generate"

    def generate(self, prompt: str, temperature: float = 0.7, max_tokens: int = 2048) -> str:
        """
        Generate text using Ollama API.

        Args:
            prompt: Input prompt for the model
            temperature: Sampling temperature (0.0 to 1.0)
            max_tokens: Maximum tokens to generate

        Returns:
            Generated text response

        Raises:
            Exception: If API call fails
        """
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens
            }
        }

        try:
            response = requests.post(
                self.generate_url,
                json=payload,
                timeout=120  # 2 minute timeout
            )
            response.raise_for_status()

            result = response.json()
            return result.get("response", "").strip()

        except requests.exceptions.ConnectionError:
            raise Exception(
                "Cannot connect to Ollama. Please ensure Ollama is running on "
                f"{self.base_url}. Start it with: ollama serve"
            )
        except requests.exceptions.Timeout:
            raise Exception("Request timed out. The model might be taking too long to respond.")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"HTTP error occurred: {str(e)}")
        except Exception as e:
            raise Exception(f"Error calling Ollama API: {str(e)}")

    def is_available(self) -> bool:
        """
        Check if Ollama service is available.

        Returns:
            True if Ollama is running and accessible, False otherwise
        """
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False

    def list_models(self) -> list:
        """
        List available models in Ollama.

        Returns:
            List of model names
        """
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            response.raise_for_status()
            data = response.json()
            return [model["name"] for model in data.get("models", [])]
        except:
            return []


def create_llm_client(model: str = "llama3.1") -> OllamaClient:
    """
    Factory function to create an Ollama client.

    Args:
        model: Model name to use

    Returns:
        Configured OllamaClient instance
    """
    return OllamaClient(model=model)
