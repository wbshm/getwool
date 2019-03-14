from _md5 import md5

import requests

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
                 'param': {'name', 'psw'}, 'method': 'post'}
}


def get_access_token():
    pass


def get_token():
    """
    字符长度32	登陆token	调用接口成功，返回登陆token
    空值	调用接口超时异常

    0	帐户处于禁止使用状态
    -1	调用接口失败
    -2	帐户信息错误	调用的参数有为空值
    -3	用户或密码错误	用户名或密码错误
    -4	不是普通帐户
    该帐户不能用于Web Service或HTTP 等API接口模式(如：代理帐户,软件作者，客服，技术员，系统管理员等)

    注：只有普通用户才能使用Web Service 或http接口
    -30	非绑定IP	访问IP非法
    :return:
    """
    return ""


def get_params():
    dict = {}
    dict['name'] = 'lucky'
    dict['psw'] = md5('a6823192')

    pass


def request_api(config):
    if get_token():
        return get_token()

    request_url = config['url']

    if config['method'] == 'get':
        responce = requests.get(request_url, params=get_params())
    elif config['method'] == 'post':
        responce = requests.post(request_url, params=get_params())
