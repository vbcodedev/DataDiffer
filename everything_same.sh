#!/bin/bash
mongo < everything_same.js
python3 main.py --source-uri "mongodb://localhost:27017" --target-uri "mongodb://localhost:27017" --source-namespace "dataDiffer_1.source" --target-namespace "dataDiffer_2.target" --percent 100
mongo < everything_same_drop.js