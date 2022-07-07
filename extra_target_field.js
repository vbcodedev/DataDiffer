//Frank in the target collection has an additional field of pets with a value which does not exist in the source. Everything else is the same.
use dataDiffer_3
db.source.insertMany([{"_id": 1.0, "name": "John", "age": 21.0, "siblings": 1.0}, {"_id": 2.0, "name": "Frank", "age": 22.0, "siblings": 14.0}, {"_id": 3.0, "name": "Susan", "age": 22.0, "siblings": 2.0}])
use dataDiffer_4 
db.target.insertMany([{"_id": 1.0, "name": "John", "age": 21.0, "siblings": 1.0}, {"_id": 2.0, "name": "Frank", "age": 22.0, "siblings": 14.0, "pets": 12}, {"_id": 3.0, "name": "Susan", "age": 22.0, "siblings": 2.0}])