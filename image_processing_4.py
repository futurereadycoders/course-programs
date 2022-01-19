from PIL import Image
import PIL.ImageOps

image = Image.open('rubiks.jpeg')
image.show()

inverted_image = PIL.ImageOps.solarize(image, 25)
inverted_image.show()
