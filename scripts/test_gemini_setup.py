import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv(PROJECT_ROOT / ".env")

def test_imports():
    print("Testing imports...")
    try:
        from google import genai
        print("✅ google-genai installed")
    except ImportError:
        print("❌ google-genai NOT installed")
        return False
    return True

def test_env_vars():
    print("\nTesting environment variables...")
    
    rag_key = os.getenv("RAG_LLM_API_KEY")
    rag_base = os.getenv("RAG_LLM_BASE_URL")
    img_key = os.getenv("IMAGE_GEN_API_KEY")
    
    if not rag_key:
        print("❌ RAG_LLM_API_KEY is missing")
    else:
        print("✅ RAG_LLM_API_KEY is set")
        
    if rag_base == "https://generativelanguage.googleapis.com/v1beta/openai/":
        print("✅ RAG_LLM_BASE_URL is correctly set for Gemini")
    else:
        print(f"⚠️ RAG_LLM_BASE_URL is '{rag_base}' (Expected: 'https://generativelanguage.googleapis.com/v1beta/openai/')")

    if not img_key:
        print("❌ IMAGE_GEN_API_KEY is missing")
    else:
        print("✅ IMAGE_GEN_API_KEY is set")
        
    return bool(rag_key and img_key)

def test_client_init():
    print("\nTesting client initialization...")
    try:
        from paper2slides.generator.image_generator import ImageGenerator
        
        # Test ImageGenerator init
        gen = ImageGenerator(model="gemini-2.0-flash-exp") # Or whatever model user wants
        print("✅ ImageGenerator initialized successfully")
        
        # Check if it detects Gemini mode
        is_gemini = "gemini" in gen.model.lower() or "google" in gen.base_url.lower()
        if is_gemini:
             print("✅ ImageGenerator detected Gemini mode")
        else:
             print("⚠️ ImageGenerator did NOT detect Gemini mode (check model name or base_url)")

    except Exception as e:
        print(f"❌ Client initialization failed: {e}")
        return False
    return True

if __name__ == "__main__":
    print("=== Gemini Setup Verification ===\n")
    if test_imports():
        test_env_vars()
        test_client_init()
    print("\n=================================")
