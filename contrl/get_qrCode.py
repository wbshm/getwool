import json
import base64
import requests


# http://www.woniudati.com

def get_code(file):
    body = {
        'UserName': 'hello123',
        'PassWord': 'hello123',
        'SoftID': 8,
    }
    files = {
        'Image': file
    }
    res = requests.post('http://api.woniudama.com/ApiWeb/Create', data=body, files=files)
    return res.text.split("|")[0]


def get_code_free(path):
    data = {}
    with open(path, "rb") as f:
        data0 = f.read()
        data['image_base64'] = str(base64.b64encode(data0), 'utf-8')
        data['app_id'] = '98709484'
        data['ocr_code'] = '0000'
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url='https://nmd-ai.juxinli.com/ocr_captcha', headers=headers, data=json.dumps(data))
    res = res.json()
    if res['string'].isdigit():
        return res['string']
    return 0

