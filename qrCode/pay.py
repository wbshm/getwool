import requests

headers = {
    'Content-Type': 'multipart/form-data',
}
# http://www.woniudati.com/

file_path = './ver/ver___6.png'
body = {
    'UserName': 'hello123',
    'PassWord': 'hello123',
    'SoftID': 8,
}
files1 = {
    'Image': open(file_path, 'rb')
}

if __name__ == '__main__':
    res = requests.post('http://api.woniudama.com/ApiWeb/Create', data=body, files=files1)
    print(res.text.split("|")[0])
    exit(0)
