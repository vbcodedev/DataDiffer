#!/bin/bash
mongo < nested_dict_diff.js
python3 main.py --source-uri "mongodb://localhost:27017" --target-uri "mongodb://localhost:27017" --source-namespace "dataDiffer_9.source" --target-namespace "dataDiffer_10.target" --percent 100
mongo < nested_dict_diff_drop.js