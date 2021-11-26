import requests
import json

URL = 'http://127.0.0.1:8000/gview/generic/'


def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}
    r = requests.get(url=URL,headers=headers,data=json_data)


    data = r.json()
    print(data)
# get_data(1)


def post_data():
    data = {
        'name':'mehenaz janu',
        'email':'viva@gmail.com',
        'phone':'01745961351',
        'city':'pabna',
    }
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)


# post_data()

def update_data():
    data = {
        'id':11,
        'name':'parvez love so much mehenaz viva',
        'email':'viva@gmail.com',
        'phone':'01745961351',
         'city':'Bhangura,pabna',
    }
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)
update_data()

def delete_data():
    data = {
        'id': 7,
    }
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.delete(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)
# delete_data()
