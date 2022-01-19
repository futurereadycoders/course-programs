from PIL import Image
import PIL.ImageOps

image = Image.open('rubiks.jpeg')
image.show()

inverted_image = PIL.ImageOps.invert(image)
inverted_image.show()
