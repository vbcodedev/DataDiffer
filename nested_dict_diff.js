//Susan in nested dict of pets of source has cat name "Al" instead of "Alex" which is what it is in target collection. Everything else is the same. 
use dataDiffer_9
db.source.insertMany([{"_id": 1.0, "name": "John", "age": 21.0, "siblings": 1.0, "pets":[{"cat": "Kitty", "hamster": "JJ"}]},{"_id": 2.0, "name": "Frank", "age": 22.0, "siblings": 14.0, "pets":[{"cat": "Sammy", "hamster": "Johnny"}]}, {"_id": 3.0, "name": "Susan", "age": 22.0, "siblings": 2.0, "pets":[{"cat": "Al", "hamster": "Max"}]}])
use dataDiffer_10
db.target.insertMany([{"_id": 1.0, "name": "John", "age": 21.0, "siblings": 1.0, "pets":[{"cat": "Kitty", "hamster": "JJ"}]},{"_id": 2.0, "name": "Frank", "age": 22.0, "siblings": 14.0, "pets":[{"cat": "Sammy", "hamster": "Johnny"}]}, {"_id": 3.0, "name": "Susan", "age": 22.0, "siblings": 2.0, "pets":[{"cat": "Alex", "hamster": "Max"}]}])
