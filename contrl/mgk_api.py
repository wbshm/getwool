import requests
from PIL import Image
from io import BytesIO
from contrl import get_qrCode

cookie = {}


def get_qrcode():
    requestUrl = 'http://app01.shdytx.com/index.php/login/verify'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/24.0)',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.9',
        'X-Requested-With': 'io.dcloud.H52831D33',
    }

    r = requests.get(requestUrl, headers=headers)
    global cookie
    cookie = dict(r.cookies)
    a = Image.open(BytesIO(r.content))
    tmpDir = './qrCode/1.png'
    a.save(tmpDir)
    # return get_qrCode.get_code(open(tmpDir, 'rb'))
    return get_qrCode.get_code_free(tmpDir)


def register(phone):
    request_url = 'http://app01.shdytx.com/index.php/Login/login'
    code = get_qrcode()
    max_time = 50
    while code == 0:
        code = get_qrcode()
        if max_time == 0:
            exit(-10)
        max_time -= 1

    data = {
        'username': phone,
        'password': '123',
        'zcode': code
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/24.0)',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.9',
        'X-Requested-With': 'io.dcloud.H52831D33',
    }
    res = requests.post(request_url, data=data, headers=headers, cookies=cookie)
    return res.text


if __name__ == '__main__':
    get_qrCode()
    exit(0)
