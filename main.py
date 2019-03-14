# noinspection PyInterpreter
import requests

from config import config
from contrl.hit_zanma import Zanma
from modal import account

if __name__ == '__main__':

    zanmaObj = Zanma()
    accountDba = account.Phone()

    phone_list = zanmaObj.get_phone_list()

    for phone in phone_list:
        accountDba.save_data({'phone': phone, 'platform': 'zanma'}, tags='bad')
