#!/bin/bash
mongo < order_change.js
python3 main.py --source-uri "mongodb://localhost:27017" --target-uri "mongodb://localhost:27017" --source-namespace "dataDiffer_5.source" --target-namespace "dataDiffer_6.target" --percent 100
mongo < order_change_drop.js