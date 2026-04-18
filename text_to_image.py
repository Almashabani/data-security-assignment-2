import random
def generate_color_mapping(text):
    unique_chars = sorted(set(text))
    mapping = {}
    used_colors = set()

    for ch in unique_chars:
        while True:
         color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
        if color not in used_colors:
           used_colors.add(color)
           mapping[ch] = color
           break

    return mapping


    from PIL import Image
    import json
    from mapping_utils import generate_color_mapping


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

    decrypted_chars = []
    count = 0