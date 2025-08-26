import requests

#get all items
    #full dict and selection
print(requests.get("http://127.0.0.1:8000/items/").json())
    #full dict 
#print(requests.get("http://127.0.0.1:8000/").json())

#get item by params
#print(requests.get("http://127.0.0.1:8000/items?name=Nails").json())

#add an item 
# print("Adding an item:")
# print(
#     requests.post(
#         "http://127.0.0.1:8000/",
#         json={"name": "Screwdriver", "price": 3.99, "count": 10, "id": 4, "category": "tools"},
#     ).json()
# )
# print(requests.get("http://127.0.0.1:8000/").json())

#updating an item
# print("Updating an item:")
# print(requests.put("http://127.0.0.1:8000/update/0?count=9001").json())
# print(requests.get("http://127.0.0.1:8000/").json())

# print("Deleting an item:")
# print(requests.delete("http://127.0.0.1:8000/delete/0").json())
# print(requests.get("http://127.0.0.1:8000/").json())