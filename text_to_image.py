from PIL import Image
#instalojme paketen 'pillow'
import json















def decrypt_image_to_text(input_image, input_key):
    with open(input_key, "r", encoding="utf-8") as f:
        key_data = json.load(f)

    text_length = key_data["text_length"]
    mapping = key_data["mapping"]

    color_to_char = {}
    for ch, color in mapping.items():
        color_to_char[tuple(color)] = ch

    img = Image.open(input_image).convert("RGB")
    pixels = img.load()
    width, height = img.size