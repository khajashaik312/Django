import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id=none):
	data={} #you need all records
	if id is not None:
		data={id:id} # a record with a particular id
	    response=requests.get(BASE_URL+ENDPOINT)
	    print(response.status_code)
	    print(response.json())

def create_resource():
	stud_data={'name':'Anand','rollno':201,'marks':88,'address':'Delhi'}
	response=requests.post(BASE_URL+ENDPOINT,data=json.dumps(stud_data))
	print(response.status_code)
	print(response.json())

def update_resource(id):
	new_emp={'id':'id','name':'New user','marks':88,'address':'Unknown place'}
	response=requests.put(BASE_URL+ENDPOINT+id+'/',data=json.dumps(stud_data))
	print(response.status_code)
	print(response.json())

def delete_resource(id):
	data={'id':id}
	response=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
	print(response.status_code)
	print(response.json())

	print("Enter 1-->to retrive the records \n 2-->to create a new record \n 3-->to update a record\n 4-->to delete a record\n")
	print("Enter your choice")
	ch=int(input())
	if ch==1:
		get_resource()
	elif ch==2:
		create_resource()
	elif ch==3:
		id=input("enter id")
		update_resource(id)
	if ch==4:
		id=input("enter id")
		delete_resource(id)