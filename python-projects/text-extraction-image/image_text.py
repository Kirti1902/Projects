from PIL import Image
import pytesseract


image_path = 'C:/Users/kirti/OneDrive/Desktop/College Essentials/Computer Language Folders/Python projects/text-extraction-image/image1.jpeg'
img = Image.open(image_path)

text = pytesseract.image_to_string(img)

print(text[:-1])
   