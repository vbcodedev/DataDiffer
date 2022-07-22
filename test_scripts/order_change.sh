#!/bin/bash
export myDB=$SOURCE_DB
export myColl=$SOURCE_COLL
mongo $SOURCE_URI order_change_source.js

export myDB=$TARGET_DB
export myColl=$TARGET_COLL
mongo $TARGET_URI order_change_target.js

python3 data-differ.py --source-uri $SOURCE_URI --target-uri $TARGET_URI --source-namespace "$SOURCE_DB.$SOURCE_COLL" --target-namespace "$TARGET_DB.$TARGET_COLL" --percent 100

export myDB=$SOURCE_DB
export myColl=$SOURCE_COLL
mongo $SOURCE_URI drop_coll.js

export myDB=$TARGET_DB
export myColl=$TARGET_COLL
mongo $TARGET_URI drop_coll.js