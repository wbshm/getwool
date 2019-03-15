import datetime

import requests

from modal import account

apiConfig = {
    'zanma': {
        'office': 'http://47.107.130.26:9000/index.html',
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
    'getToken': {'name': 'getToken', 'url': 'http://120.79.206.192:9180/service.asmx/UserLoginStr',
                 'param': ['name', 'psw'], 'method': 'post'}
}


class Zanma(object):
    def __del__(self):
        pass

    def get_access_token(self):
        dba = account.Token()
        token = dba.get_data_by_key('zanma')
        token = token['token']
        if token is None or len(token) < 30 or 1:
            response = requests.get('http://120.79.206.192:9180/service.asmx/UserLoginStr',
                                    params=self.get_params(['name', 'psw']))
            token = response.text
            dba.save_data({'key': 'zanma', 'token': token, 'get_time': get_time()})
        return token

    def get_phone_list(self, num):
        request_url = 'http://120.79.206.192:9180/service.asmx/GetHM2Str'
        request_data = {
            'token': self.get_access_token(),  # (登陆令牌)
            'xmid': '300217',  # (项目编码) 项目ID
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
        request_url = 'http://120.79.206.192:9180/service.asmx/sfHmStr'
        request_data = {
            'token': self.get_access_token(),
            'hm': phone
        }
        res = requests.get(request_url, request_data)
        return res.text

    def release_all(self):
        res = requests.get('http://120.79.206.192:9180/service.asmx/sfAllStr', {'token': self.get_access_token()})
        return res.text

    def add_black_list(self, phone):
        data = {
            'token': self.get_access_token(),
            'xmid': 300217,
            'hm': phone,
            'sf': 1
        }
        requests.get('http://120.79.206.192:9180/service.asmx/Hmd2Str', data)

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
        print(response.text)
        return response


def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
