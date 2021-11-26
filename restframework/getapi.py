# import requests
# import json
# URL = 'http://127.0.0.1:8000/studentapi/'
# headers = {'Authorization': 'Token 06072bdf25376d0e8710c85fca234b5ed50b4854'}
#
# r = requests.get(url=URL, headers=headers)
# data=r.json()
# print(r)

import requests

url = 'http://127.0.0.1:8000/studentapi/'
headers = {'Authorization': 'Token ef40d57a67dbef79e61eeec57d5b2e393d1dbf6f'}
r = requests.get(url, headers=headers)