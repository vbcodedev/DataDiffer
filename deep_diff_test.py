from pickle import FALSE, TRUE
from deepdiff import DeepDiff
import json
import math

dict1 = {"name": "Vanshaj", "age": 12}
dict2 = {"age": 12, "name": "Vanshaj",}

same_diff_order1 = {"name": "Vanshaj", "age": 12}
same_diff_order2 = {"age": 12, "name": "Vanshaj"}

nested1 = {1: {"name": "John", "age": 27, "sex": "Male"},
         2: {"name": "Samantha", "age": 22, "sex": "Female"}}

nested2 = {1: {"name": "John", "age": 27, "sex": "Male"},
         2: {"name": "Samantha", "age": 22}}

val = DeepDiff(dict1, dict2).pretty()
val1 = DeepDiff(same_diff_order1, same_diff_order2).pretty()
val2 = DeepDiff(nested1, nested2).pretty()

# if val == "":
#     print("no differences were found")
# else:
#     print(val)


# if json.dumps(dict1) == json.dumps(dict2):
#     print("They are the same")
# else:
#     print("There is a difference")
#     print(json.dumps(dict1))
#     print(json.dumps(dict2))

num = 40
size = 10

print(math.ceil(1))

