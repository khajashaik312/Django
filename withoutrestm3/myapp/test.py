import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id=None):
    data={}
    if id is not None:
        data={'id':id}
    response=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(response.status_code)
    print(response.json())
def create_resource():
    new_emp={'eno':999,'ename':'abhi','esal':200,'eaddr':'Mumbai'}
    response=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(response.status_code)
    print(response.json())

def update_resource(id):
    new_data={'id':id,'esal':100000,'eaddr':'Mysore'}
    response=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(response.status_code)
    print(response.json())
def delete_resource(id):
    data={'id':id}
    response=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(response.status_code)
    print(response.json())
print("Enter 1--->get a resource\n 2--->create a resource 3-->update resource 4--->delete resource")
ch=int(input("Enter your option"))
if ch==1:
    get_resource()
if ch==2:
    create_resource()
if ch==3:
    id=int(input("Enter id"))
    update_resource(id)
if ch==4:
    id=int(input("Enter id"))
    delete_resource(id)
