#  train https://blog.csdn.net/cn_wk/article/details/52280567

# from PIL import Image

# $ pip install pillow
# $ pip install pytesseract
import pytesseract
import os
from PIL import Image

if __name__ == '__main__':
    rootdir = './ver/'
    listDir = os.listdir(rootdir)
    for i in range(0, len(listDir)):
        target = os.path.join(rootdir, listDir[i])
        if os.path.isfile(target) and target.split('.')[-1] == 'png':
            im = Image.open(target)
            im = im.convert('L')
            print(listDir[i].split('.')[0] + "," + pytesseract.image_to_string(im, lang='wchao'))
