import datetime
import time

import requests
from modal import account
from modal.log import LogData

apiConfig = {
    'fy': {
        'office': 'http://www.d1tm.com',
        'account': 'lucky',
        'password': 'a6823192'
    },
    'mifeng': {
        'office': 'http://bmyzm.cn:9000/index.html',
        'account': '6823192',
        'password': 'a6823192'
    },
}

apiUrl = {
    'getToken': {'name': 'getToken', 'url': 'http://dkh.d1tm.com/service.asmx/UserLoginStr',
                 'param': ['name', 'psw'], 'method': 'post'}
}
xmid = 300217


class fy(object):
    def __del__(self):
        pass

    def get_access_token(self):
        dba = account.Token()
        token = dba.get_data_by_key('fy')
        params = {
            'name': 'a6823192',
            'psw': '6823192'
        }
        if token is None or len(token) < 30 or 1:
            response = requests.get('http://dkh.d1tm.com/service.asmx/UserLoginStr',
                                    params=params)
            token = response.text
            dba.save_data({'key': 'fy', 'token': token, 'get_time': get_time()})
        else:
            token = token['token']
        return token

    def get_phone_list(self, num):
        request_url = 'http://dkh.d1tm.com/service.asmx/GetHM2Str'
        request_data = {
            'token': self.get_access_token(),  # (登陆令牌)
            'xmid': xmid,  # (项目编码) 项目ID
            'sl': num,  # (取号数量)
            'lx': 0,  # (号码类型)
            'a1': '',  # (省份)
            'a2': '',  # (城市)
            'pk': '',  # (专属对接Key)
            'ks': '0',  # (卡商id编号)
            'rj': '',  # (作者帐户名)
        }
        res = requests.get(request_url, params=request_data)
        if res.text[0:2] == 'hm':
            return res.text[3:].split(",")
        else:
            return res.text

    def release_phone(self, phone):
        request_url = 'http://dkh.d1tm.com/service.asmx/sfHmStr'
        request_data = {
            'token': self.get_access_token(),
            'hm': phone
        }
        res = requests.get(request_url, request_data)
        return res.text

    def release_all(self):
        res = requests.get('http://dkh.d1tm.com/service.asmx/sfAllStr', {'token': self.get_access_token()})
        return res.text

    def add_black_list(self, phone):
        data = {
            'token': self.get_access_token(),
            'xmid': xmid,
            'hm': phone,
            'sf': 1
        }
        requests.get('http://dkh.d1tm.com/service.asmx/Hmd2Str', data)

    def get_params(self, keys):
        params = {
            'name': 'lucky',
            'psw': 'a6823192'
        }
        return {keys[x]: params[keys[x]] for x in range(0, len(keys))}

    def request_api(self, config):

        request_url = config['url']

        if config['method'] == 'get':
            response = requests.get(request_url, params=self.get_params(config['param']))
        else:
            response = requests.post(request_url, params=self.get_params(config['param']))
        return response

    def lock_phone(self, phone):
        """
        指定号码
        :param phone:
        """
        data = {
            'token': self.get_access_token(),
            'xmid': xmid,
            'hm': phone,
            'op': 1,
            'pk': '',
            'rj': ''
        }
        request_url = 'http://dkh.d1tm.com/service.asmx/mkHM2Str'
        res = requests.get(request_url, params=data)
        print(data)
        print(res.text)
        return res.text

    def get_check_code(self, phone):
        self.lock_phone(phone)
        while True:
            request_url = 'http://dkh.d1tm.com/service.asmx/GetYzm2Str'
            data = {
                'token': self.get_access_token(),
                'xmid': xmid,
                'hm': phone,
                'sf': 0
            }
            res = requests.get(request_url, params=data)
            if len(res.text) != 1:
                LogData().save_data({'phone': phone, 'status': res.text, 'update_time': get_time()})
                exit(res.text)
            else:
                time.sleep(1)



def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
