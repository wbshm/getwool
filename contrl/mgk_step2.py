from io import BytesIO

import requests
from PIL import Image

from contrl import get_qrCode

defaultPassword = 'mgkGodlike'

cookie = {}


def send_change_password_msg(phone):
    """
    发送修改密码的短信验证码
    :param phone:
    :return:
    """
    requestUrl = 'http://app01.shdytx.com/index.php/Json/pwd1_sms'
    headers = {
        'User-Agent': ' Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/24.0)',
        'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': ' gzip, deflate',
        'Accept-Language': ' zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': ' aliyungf_tc=AQAAAA8FmCAyVA4AFQZo3x7KhhCa1P8u; acw_tc=792b121115526924089515459ec9af34a642a570962e13d7c4aa3fbee8b3fc; PHPSESSID=hg7j54990vm7factbv01ersd85',
    }
    params = {
        'Action': 'post',
        'mobile': phone
    }

    res = requests.post(requestUrl, params=params, headers=headers)
    return res.text
    pass


def change_password(phone, tel_code):
    """
    修改用户密码
    :param phone:
    """
    requestUrl = 'http://app01.shdytx.com/index.php/Forget/Forgetsave'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/24.0)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    params = {
        'username': phone,
        'upd1': defaultPassword,
        'rupd1': defaultPassword,
        'telcode': tel_code
    }
    res = requests.post(requestUrl, params=params)
    res = res.json()
    if res['status'] == 1:
        pass  # change password success
    else:
        pass  # log why failure


def get_code_for_login():
    """
    获取登陆的图形验证码
    :return:
    """
    requestUrl = 'http://app01.shdytx.com/index.php/login/verify'
    headers = {
        'User-Agent': ' Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/24.0)',
        'Accept': ' image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': ' gzip, deflate',
        'Accept-Language': ' zh-CN,en-US;q=0.9',
    }
    r = requests.get(requestUrl, headers=headers)
    a = Image.open(BytesIO(r.content))
    tmpDir = './qrCode/2.png'
    a.save(tmpDir)
    return get_qrCode.get_code_free(tmpDir)


def login(phone):
    requestUrl = 'http://app01.shdytx.com/index.php/Login/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/24.0)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.9',
    }
    params = {
        'username': phone,
        'password': defaultPassword,
        'zcode': get_code_for_login()
    }
    requests.get()
