import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource1():
	resp=requests.get(BASE_URL+ENDPOINT)
	print(resp.status_code)
	print(resp.json())

def get_resource2(id):
	resp=requests.get(BASE_URL+ENDPOINT+id+'/')
	print(resp.status_code)
	print(resp.json())

def create_resource():
	new_emp={'eno':151,'ename':'Anu','esal':16000,'eaddr':'Delhi'}
	resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
	print(resp.status_code)
	print(resp.json())

def update_resource(id):
	new_emp={'esal':25000,'eaddr':'Bangalore'}
	resp=requests.put(BASE_URL+ENDPOINT+id+'/',data=json.dumps(new_emp))
	print(resp.status_code)
	print(resp.json())

def delete_resource(id):
	resp=requests.delete(BASE_URL+ENDPOINT+id+'/')
	print(resp.status_code)
	print(resp.json())

	print("Enter 1-->to display all records\n 2-->to display a particular record\n 3-->to create a new resource\n 4-->to update a resource\n 5-->to delete a resource")
	ch=int(input("Enter your choice"))
	if ch==1:
		get_resource1()
	if ch==2:
		id=input("Enter id")
		get_resource2(id)
	if ch==3:
		create_resource()
	if ch==4:
		id=input("enter id")
		update_resource(id)
	if ch==5:
		id=input("enter id")
		delete_resource(id)