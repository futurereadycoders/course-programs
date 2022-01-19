from PIL import ImageFilter, Image
import os

im = Image.open("rubiks.jpeg")
im.show()
im.filter(ImageFilter.BoxBlur(20)).show()
