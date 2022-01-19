from PIL import Image
import PIL.ImageOps

image = Image.open('rubiks.jpeg')
image.show()

inverted_image = PIL.ImageOps.grayscale(image)
inverted_image.show()
