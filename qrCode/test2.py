from PIL import Image
from pytesseract import *


if __name__ == '__main__':

    im = Image.open('./test/0088.png')  # 用pil打开这个图片

    im = im.convert('L')
    im = im.point(lambda x: 0 if x < 100 else x >= 100, '1')  # 二值化 100为分割灰度的点（阀值），二值化就是将图片的颜色转换成非黑即白的图片
    im.show()  # 查看图片
