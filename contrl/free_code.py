# coding:utf-8
import json
import base64
import requests

if __name__ == '__main__':

    data = {}
    path = "../qrCode/ver/"
    file_name = "6359.png"
    print(file_name)
    with open(path + file_name, "rb") as f:
        data0 = f.read()
        data['image_base64'] = str(base64.b64encode(data0), 'utf-8')
        data['app_id'] = '98709484'
        data['ocr_code'] = '0000'
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url='https://nmd-ai.juxinli.com/ocr_captcha', headers=headers, data=json.dumps(data))
    res = res.json()
    print(res)
