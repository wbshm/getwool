# noinspection PyInterpreter

from contrl.hit_zanma import Zanma
from modal import account
from contrl import mgk_api
import datetime
import json


def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在


if __name__ == '__main__':

    # a = json.loads('{"status":0,"info":"\u5e10\u53f7\u4e0d\u5b58\u5728","complain":0}')
    # print(a)
    # exit()

    zanmaObj = Zanma()
    accountDba = account.Phone()

    # print(zanmaObj.release_all())
    while True:
        zanmaObj.release_all()
        phone_list = zanmaObj.get_phone_list(30)
        print(phone_list)
        platform = 'zanma'
        for phone in phone_list:
            if len(phone) != 11:
                continue
            if accountDba.get_index_by_phone(phone) == -1:
                res = mgk_api.register(phone)
                jsonData = json.loads(res)
                print(phone + '：' + str(jsonData))
                if jsonData['info'] == '帐号或密码错误':
                    with open('access.txt', 'a') as f:
                        f.write(phone + ':' + platform+'\n')
                accountDba.save_data({'phone': phone, 'platform': platform, 'update_time': get_time(), 'info': res})
            zanmaObj.add_black_list(phone)
