//The id of Susan in target is 10.0 when in source it is 3.0. Everything else is the same. 
use dataDiffer_7
db.source.insertMany([{"_id": 1.0, "name": "John", "age": 21.0, "siblings": 1.0}, {"_id": 2.0, "name": "Frank", "age": 22.0, "siblings": 14.0}, {"_id": 3.0, "name": "Susan", "age": 22.0, "siblings": 2.0}])
use dataDiffer_8
db.target.insertMany([{"_id": 1.0, "name": "John", "age": 21.0, "siblings": 1.0}, {"_id": 2.0, "name": "Frank", "age": 22.0, "siblings": 14.0}, {"_id": 10.0, "name": "Susan", "age": 22.0, "siblings": 2.0}])