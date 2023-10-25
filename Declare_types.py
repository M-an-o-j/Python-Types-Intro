# #standard python types str, int, float, bool, bytes
# def get_items(item_a:str, item_b:int, item_c:float,item_d:bool, item_e:bytes):
#     print( item_a, item_b, item_c,item_d, item_e)

# get_items(3, "manoj", 23, "nnn",23)

# #data structures that can contain other values, like dict, list, set and tuple

# #list
# def process_items(items: list[str]):
#     for item in items:
#         print(item)

# process_items(3)

# #tuple and set
# def process_items(items_t: tuple[int, int, str], items_s:set[bytes]):
#     print( items_t, items_s)

# process_items([3,4,"manoj"], [2,3,"manoj"])

# # dictionary
# def process_items(prices:dict[str,float]):
#     for item_name, item_price in prices.items():
#         print(f"{item_name} : {item_price}")

# items = {"phone": 39, "computer": 23}
# process_items(items)

# # union
# from typing import Union

# def process_items(item: Union[int, str]):
#     print(type(item), item)

# process_items(True)

# # Possibly None
# from typing import Optional

# def say_hi(name: Optional[str] = None):
#     if name is not None:
#         print(f"Hey {name}")
#     else:
#         print("There is no name")

# say_hi()

# # classes as types
# class Person:
#     def __init__(self, name: str):
#         self.name = name

# def get_person_name(one_person: Person):
#     return one_person.name

# name = Person("manoj")
# print(get_person_name(name))

from datetime import datetime
from typing import List, Union
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name : str = 'John Doe'
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 13:25",
    "friends":[1, "2", b"3"]
}

user = User(**external_data)
print(user)
print(user.id)