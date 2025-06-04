import os
import random
import datetime
from PIL import Image, ImageDraw, ImageFont

# Load a random meme template from templates folder
def load_random_image():
    templates_dir = "templates"
    files = os.listdir(templates_dir)
    img_name = random.choice(files)
    return os.path.join(templates_dir, img_name)

# Ask user for a meme quote
def get_quote():
    return input("Enter your meme quote: ")

# Draw the quote on the image
def draw_text_on_image(image_path, text):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Try to use a TTF font; fallback to default
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    # Calculate text position using textbbox (for Pillow 10+)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (img.width - text_width) // 2
    y = img.height - text_height - 20

    # Optional: Draw text outline for visibility
    outline_range = 2
    for dx in range(-outline_range, outline_range + 1):
        for dy in range(-outline_range, outline_range + 1):
            draw.text((x + dx, y + dy), text, font=font, fill="black")

    # Draw main white text
    draw.text((x, y), text, font=font, fill="white")
    return img

# Save the new image in the generated/ folder
def save_image(img):
    output_dir = "generated"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filename = datetime.datetime.now().strftime("meme_%Y%m%d_%H%M%S.jpg")
    filepath = os.path.join(output_dir, filename)
    img.save(filepath)
    print(f"Meme saved as: {filepath}")

# Main loop
def main():
    while True:
        image_path = load_random_image()
        quote = get_quote()
        meme = draw_text_on_image(image_path, quote)
        save_image(meme)

        again = input("Generate another meme? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()

