import requests
import json


#GET
user_input=input("Enter ID: ")
get_url=f"https://jsonplaceholder.typicode.com/todos/{user_input}"


get_response = requests.get(get_url)
print(get_response.json())


#POST
to_do_item={
    "userId": 1,
    "id": 201,
    "title": "New Task",
    "completed": False
}
post_url="https://jsonplaceholder.typicode.com/todos"
#optional_headers
headers={"Content-Type":"application/json"}
post_response=requests.post(post_url,data=json.dumps(to_do_item),headers=headers)
print(post_response.json())

