import requests
import namegenerator
import time

auth = ('user', 'p@ssw0rd!')
url  = 'https://localhost:8443/fingerprint'

for i in range(1000):
    data = dict()
    data['username'] = namegenerator.gen()
    data['time'] = time.time()
    data['password'] = namegenerator.gen()
    resp = requests.post(url, auth=auth, json=data, verify=False)
    print(i, resp.status_code, resp.text)
