use sam_one

db.sam_one.insertMany([{"_id": 1.0, "name": "John", "age": 21.0, "siblings": 1.0}, {"_id": 2.0, "name": "Frank", "age": 22.0, "siblings": 14.0}, {"_id": 3.0, "name": "Susan", "age": 22.0, "siblings": 2.0}])

use sam_two 

db.sam_two.insertMany([{"_id": 1.0, "name": "John", "age": 21.0, "siblings": 1.0}, {"_id": 2.0, "name": "Frank", "age": 22.0, "siblings": 14.0, "pets": 12}, {"_id": 3.0, "name": "Susan", "age": 22.0, "siblings": 2.0}])