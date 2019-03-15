import datetime
import json

from contrl import mgk_api
from contrl.hit_fy import fy
from modal import account


def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在


if __name__ == '__main__':
    hitBoj = fy()
    accountDba = account.Phone()
    while True:
        hitBoj.release_all()
        phone_list = hitBoj.get_phone_list(30)
        print(phone_list)
        platform = 'fy'
        for phone in phone_list:
            if accountDba.get_index_by_phone(phone) == -1:
                res = mgk_api.register(phone)
                jsonData = json.loads(res)
                print(phone + '：' + str(jsonData))
                if jsonData['info'] == '帐号或密码错误':
                    with open('access.txt', 'a') as f:
                        f.write(phone + ':' + platform+'\n')
                accountDba.save_data({'phone': phone, 'platform': platform, 'update_time': get_time(), 'info': res})
            hitBoj.add_black_list(phone)
