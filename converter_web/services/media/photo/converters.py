import os

from .abstract_photo_strategy import PhotoConverterStrategy
from PIL import Image


class JPEGConverter(PhotoConverterStrategy):

    def convert(self, input_file):
        name, extension = os.path.splitext(input_file)
        img = Image.open(input_file)
        if img.mode == "RGBA":
            img = img.convert("RGB")
            img.save(f"{name}_converted.jpg")
        else:
            img.save(f"{name}_converted.jpg")
        return f"{name}_converted.jpg"


class PNGConverter(PhotoConverterStrategy):

    def convert(self, input_file):
        name, extension = os.path.splitext(input_file)
        img = Image.open(input_file)
        img.save(f"{name}_converted.png")
        return f"{name}_converted.png"


class TIFFConverter(PhotoConverterStrategy):

    def convert(self, input_file):
        name, extension = os.path.splitext(input_file)
        img = Image.open(input_file)
        img.save(f"{name}_converted.tiff")
        return f"{name}_converted.tiff"


class BMPConverter(PhotoConverterStrategy):

    def convert(self, input_file):
        name, extension = os.path.splitext(input_file)
        img = Image.open(input_file)
        img.save(f"{name}_converted.bmp")
        return f"{name}_converted.bmp"