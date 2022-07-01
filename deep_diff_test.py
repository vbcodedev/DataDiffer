from deepdiff import DeepDiff
import json
import math

dict1 = {"name": "Vanshaj", "age": 12}
dict2 = {"age": 12}


same_diff_order1 = {"name": "Vanshaj", "age": 12}
same_diff_order2 = {"age": 12, "name": "Vanshaj", "age": 12}

nested1 = {1: {"name": "John", "age": 27, "sex": "Male"},
         2: {"name": "Samantha", "age": 22, "sex": "Female"}}

nested2 = {1: {"name": "John", "age": 27, "sex": "Male"},
         2: {"name": "Samantha", "age": 22}}

val = DeepDiff(dict1, dict2)
val1 = DeepDiff(same_diff_order1, same_diff_order2).pretty()
val2 = DeepDiff(nested1, nested2).pretty()


# Dictionary ={'c':'Welcome', 'b':'to',
#             'a':'Geeks'}
 
# json_string = json.dumps(Dictionary, indent = 4, separators =("", " = "))
# print(json_string)
t1 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 2, 3]}}
t2 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 3, 2, 3]}}
ddiff = DeepDiff(same_diff_order1, same_diff_order2)
