from editor import Editor

from pathlib import Path

image_path = Path("./images/image_1.jpg")
image_editor = Editor(image_path)

# image_editor.get_image_size()
# image_editor.get_pixels_amount()
# image_editor.get_color_per_pixel()
image_editor.convert_to_grayscale()