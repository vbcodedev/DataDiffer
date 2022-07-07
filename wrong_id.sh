#!/bin/bash
mongo < wrong_id.js
python3 main.py --source-uri "mongodb://localhost:27017" --target-uri "mongodb://localhost:27017" --source-namespace "dataDiffer_7.source" --target-namespace "dataDiffer_8.target" --percent 100
mongo < wrong_id_drop.js