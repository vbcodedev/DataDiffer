#!/bin/bash
mongo < extra_target_field.js
python3 main.py --source-uri "mongodb://localhost:27017" --target-uri "mongodb://localhost:27017" --source-namespace "dataDiffer_3.source" --target-namespace "dataDiffer_4.target" --percent 100
mongo < extra_target_field_drop.js