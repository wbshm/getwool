# from PIL import Image

# $ pip install pillow
# $ pip install pytesseract
import pytesseract
from PIL import Image

if __name__ == '__main__':
    target = "./test/1BB996B0056BD622889CC7C9DC0D3FA4.png"
    im = Image.open(target)
    im = im.convert('L')
    print(pytesseract.image_to_data(im))
