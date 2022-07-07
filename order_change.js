//John in target has order of fields differently than John in source. Everything else is the same. 
use dataDiffer_5
db.source.insertMany([{"_id": 1.0, "name": "John", "age": 21.0, "siblings": 1.0}, {"_id": 2.0, "name": "Frank", "age": 22.0, "siblings": 14.0}, {"_id": 3.0, "name": "Susan", "age": 22.0, "siblings": 2.0}])
use dataDiffer_6
db.target.insertMany([{"_id": 1.0, "name": "John", "siblings": 1.0, "age": 21.0,}, {"_id": 2.0, "name": "Frank", "age": 22.0, "siblings": 14.0}, {"_id": 3.0, "name": "Susan", "age": 22.0, "siblings": 2.0}])