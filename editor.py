from PIL import Image
from pathlib import Path

class Editor:
    def __init__(self, image_path):
        self.image_path = image_path

    def open_image(self):
        image = Image.open(self.image_path)

        return image

    def get_image_size(self):
        image = self.open_image()

        width = image.size[0]
        height = image.size[1]

        print(f"Largura: {width}px")
        print(f"Altura: {height}px")
    
    def get_image_width(self):
        image = self.open_image()

        width = image.size[0]

        return width

    def get_image_height(self):
        image = self.open_image()

        height = image.size[0]

        return height

    def get_pixels(self):
        image = self.open_image()

        pixels = list(image.getdata())

        return pixels
    
    def get_pixels_amount(self):
        pixels = self.get_pixels()

        pixels_amount = len(pixels)

        print(f"Quantidade de Pixels na foto: {pixels_amount}")

    def get_color_per_pixel(self):
        image = self.open_image()
        image_RGB = image.convert("RGB")
        
        width = self.get_image_width()
        height = self.get_image_height()

        for x in range(width):
            for y in range(height):
                r, g, b = image_RGB.getpixel((x, y))

                color = (r, g, b)

                # print(f"Posição do Pixel => X: {x} | Y: {y} e Cor: {color}")

                return color
    
    def convert_to_grayscale(self):
        image = self.open_image()

        pixels = self.get_pixels()

        grey_pixels = []
        
        for pixel in pixels:
            r, g, b = pixel
            grey = int(0.299*r + 0.587*g + 0.114*b)

            grey_pixels.append((grey, grey, grey))
        
        image_grayscale = Image.new("RGB", image.size)
        image_grayscale.putdata(grey_pixels)
        image_grayscale.save("./modified_images/photo_1_grayscale.jpg")

