from PIL import ImageFilter, Image
import PIL.ImageOps

im = Image.open("rubiks.jpeg")
im.show()
PIL.ImageOps.grayscale(im).show()
