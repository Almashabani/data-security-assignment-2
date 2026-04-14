from PIL import Image
import json















def decrypt_image_to_text(input_image, input_key):
    with open(input_key, "r", encoding="utf-8") as f:
        key_data = json.load(f)

    text_length = key_data["text_length"]
    mapping = key_data["mapping"]