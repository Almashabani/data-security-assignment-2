import random
from PIL import Image
#instalojme paketen 'pillow'
import json

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



    def encrypt_text_to_image(text, image_width, image_height, output_image, output_key, pad_color=(0, 0, 0));
       
       total_pixels = image_width * image height
       if len(text) > total_pixels:
          raise ValueError("Teksti eshte me i gjate se kapaciteti i fotos.")
       
       char_to_color=generate_color_mapping(text)
       
       img = Image.new("RGB", (image_width, image_height), pad_color)
       pixels = img.load()

       key_data = {
           "width": image_width,
           "height": image_height,
           "pad_color": list(pad_color),
           "text_length": len(text),
           "mapping": {ch: list(color) for ch, color in char_to_color.items()}
       }

       index = 0
       for y in range(image_height):
           for x in range(image_width):
               if index < len(text):
                   ch = text[index]
                   pixels[x, y] = char_to_color[ch]
                   index += 1
                else:
                   pixels[x, y] = pad_color

         img.save(output_image)
         
         with open(output_key, "w", encoding="utf-8") as f:
                json.dump(key_data, f, ensure_ascii=False, indent=4)















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

    for y in range(height):
        for x in range(width):
            if count >= text_length:
                break

            color = pixels[x, y]

            if color in color_to_char:
                decrypted_chars.append(color_to_char[color])
            else:
                decrypted_chars.append("?")

            count += 1
        if count >= text_length:
            break

    return "".join(decrypted_chars)

if __name__ == "__main__":
    text = "Pershendetje, ky eshte nje shembull i enkriptimit te tekstit ne foto."

    encrypt_text_to_image(
        text=text,
        image_width=20,
        image_height=10,
        output_image="encrypted_image.png",
        output_key="key.json",
        pad_color=(255, 255, 255)
    )
    decrypted_text = decrypt_image_to_text("encrypted_image.png", "key.json")