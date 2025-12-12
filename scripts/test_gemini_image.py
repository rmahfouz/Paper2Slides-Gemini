"""Test Gemini 3 Pro Image Preview model"""
from google import genai

api_key = "AIzaSyAEfYPHPyIOh9W8JP8hJmjR3LY7teI4gbg"
client = genai.Client(api_key=api_key)

model_name = "models/gemini-3-pro-image-preview"
prompt = "A cute cartoon cat wearing sunglasses"

print(f"Testing {model_name}...")
print(f"Prompt: {prompt}\n")

# Try method 1: generate_content (for multimodal models)
try:
    print("Attempting generate_content()...")
    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )
    print("✅ SUCCESS with generate_content()!")
    print(f"Response type: {type(response)}")
    if hasattr(response, 'candidates'):
        for candidate in response.candidates:
            if hasattr(candidate, 'content'):
                print(f"Content: {candidate.content}")
except Exception as e:
    print(f"❌ FAILED with generate_content(): {e}\n")

# Try method 2: generate_images (for image-only models)
try:
    print("Attempting generate_images()...")
    from google.genai import types
    response = client.models.generate_images(
        model=model_name,
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,
            output_mime_type="image/jpeg"
        )
    )
    print("✅ SUCCESS with generate_images()!")
    print(f"Response: {response}")
except Exception as e:
    print(f"❌ FAILED with generate_images(): {e}")
