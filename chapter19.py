# Chapter 19: Manipulating Images

from PIL import Image, ImageDraw, ImageFont
import os
# 1. Opening and Viewing Images
def open_and_view_image(image_path):
    try:
        # Open an image file
        img = Image.open(image_path)
        # Display the image
        img.show()
        print(f"Opened image: {image_path}")  
    except Exception as e:
        print(f"Error opening image: {e}")  

# 2. Creating New Images
def create_new_image():
    # Create a new blank image with white background
    img = Image.new('RGBA', (200, 200), 'white')
    # Save the new image
    img.save('new_image.png')
    print("New image created and saved as new_image.png")  # Output: New image created and saved as new_image.png

# 3. Class for Cropping, Resizing, and Rotating Images
class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        try:
            self.img = Image.open(image_path)
            print(f"Image loaded successfully: {image_path}")
        except Exception as e:
            print(f"Error loading image: {e}")
            self.img = None

    def crop_image(self, crop_area=(100, 100, 400, 400), save_as='cropped_image.png'):
        try:
            cropped_img = self.img.crop(crop_area)
            cropped_img.save(save_as)
            print(f"Image cropped and saved as {save_as}")  # Output: Image cropped and saved as cropped_image.png
        except Exception as e:
            print(f"Error cropping image: {e}")

    def resize_image(self, size=(300, 300), save_as='resized_image.png'):
        try:
            resized_img = self.img.resize(size)
            resized_img.save(save_as)
            print(f"Image resized and saved as {save_as}")  # Output: Image resized and saved as resized_image.png
        except Exception as e:
            print(f"Error resizing image: {e}")

    def rotate_image(self, degrees=90, save_as='rotated_image.png'):
        try:
            rotated_img = self.img.rotate(degrees)
            rotated_img.save(save_as)
            print(f"Image rotated and saved as {save_as}")  # Output: Image rotated and saved as rotated_image.png
        except Exception as e:
            print(f"Error rotating image: {e}")

# 4. Drawing on Images (Converted to Class)
class ImageDrawer:
    def __init__(self, image_path):
        self.image_path = image_path
        try:
            self.img = Image.open(image_path)
            print(f"Image loaded successfully: {image_path}")
        except Exception as e:
            print(f"Error loading image: {e}")
            self.img = None

    def draw_rectangle(self, rect_coords=(50, 50, 150, 150), outline_color="red", outline_width=5, save_as='rectangle_image.png'):
        try:
            draw_img = self.img.copy()
            draw = ImageDraw.Draw(draw_img)
            draw.rectangle(rect_coords, outline=outline_color, width=outline_width)
            draw_img.save(save_as)
            print(f"Rectangle drawn and image saved as {save_as}")  # Output: Rectangle drawn and image saved as rectangle_image.png
        except Exception as e:
            print(f"Error drawing rectangle: {e}")

    def draw_text(self, text="Hello!", position=(60, 60), text_color="blue", save_as='text_image.png'):
        try:
            draw_img = self.img.copy()
            draw = ImageDraw.Draw(draw_img)
            # Load a default font
            font = ImageFont.load_default()
            draw.text(position, text, fill=text_color, font=font)
            draw_img.save(save_as)
            print(f"Text drawn and image saved as {save_as}")  # Output: Text drawn and image saved as text_image.png
        except Exception as e:
            print(f"Error drawing text: {e}")

# 5. Practice Project: Adding Watermarks
def add_watermark(image_path, watermark_text, font_path=None):
    try:
        img = Image.open(image_path).convert('RGBA')
        watermark_img = img.copy()
        draw = ImageDraw.Draw(watermark_img)

        # Use a custom font if provided, otherwise use the default font
        if font_path and os.path.exists(font_path):
            font = ImageFont.truetype(font_path, 32)
        else:
            font = ImageFont.load_default()

        # Get text size using textbbox
        text_width, text_height = draw.textbbox((0, 0), watermark_text, font=font)[2:4]

        # Position the text at the bottom right corner
        x = watermark_img.width - text_width - 10
        y = watermark_img.height - text_height - 10

        # Draw the watermark text
        draw.text((x, y), watermark_text, font=font, fill=(24, 24, 24, 22))

        # Save the new image
        watermark_img.save('watermarked_image.png')
        print("Watermarked image saved as watermarked_image.png")  # Output: Watermarked image saved as watermarked_image.png
    except Exception as e:
        print(f"Error adding watermark: {e}") 