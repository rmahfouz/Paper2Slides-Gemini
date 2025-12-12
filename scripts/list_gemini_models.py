"""List all available Gemini models"""
import os
from google import genai

# Use your API key
api_key = "AIzaSyAEfYPHPyIOh9W8JP8hJmjR3LY7teI4gbg"

client = genai.Client(api_key=api_key)

print("Fetching all available models...\n")
print("=" * 80)

# List all models
models = client.models.list()

# Separate by type
text_models = []
image_models = []
other_models = []

for model in models:
    model_name = model.name
    
    # Check if it's an image generation model
    if any(keyword in model_name.lower() for keyword in ['imagen', 'image', 'generate']):
        image_models.append(model)
    elif any(keyword in model_name.lower() for keyword in ['gemini', 'flash', 'pro']):
        text_models.append(model)
    else:
        other_models.append(model)

# Print image generation models
print("\n🎨 IMAGE GENERATION MODELS:")
print("-" * 80)
if image_models:
    for model in image_models:
        print(f"  ✓ {model.name}")
        if hasattr(model, 'description'):
            print(f"    Description: {model.description}")
        print()
else:
    print("  ❌ No image generation models found")

# Print text models
print("\n💬 TEXT/CHAT MODELS:")
print("-" * 80)
for model in text_models[:10]:  # Show first 10
    print(f"  ✓ {model.name}")

if len(text_models) > 10:
    print(f"  ... and {len(text_models) - 10} more")

# Print other models
if other_models:
    print("\n🔧 OTHER MODELS:")
    print("-" * 80)
    for model in other_models[:5]:
        print(f"  ✓ {model.name}")

print("\n" + "=" * 80)
print(f"Total models found: {len(list(models))}")
