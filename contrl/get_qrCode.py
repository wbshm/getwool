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
