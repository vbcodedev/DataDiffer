use s_one

db.s_one.insertMany([{"_id": 1.0, "name": "John", "age": 21.0, "siblings": 1.0}, {"_id": 2.0, "name": "Frank", "age": 22.0, "siblings": 14.0}, {"_id": 3.0, "name": "Susan", "age": 22.0, "siblings": 2.0}])

use s_two 

db.s_two.insertMany([{"_id": 1.0, "name": "John", "siblings": 1.0, "age": 21.0,}, {"_id": 2.0, "name": "Frank", "age": 22.0, "siblings": 14.0}, {"_id": 3.0, "name": "Susan", "age": 22.0, "siblings": 2.0}])