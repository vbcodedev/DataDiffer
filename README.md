# DataDiffer Overview
DataDiffer will compare a user defined percentage of random documents between two MongoDB/DocumentDB servers for a single collection in each. 

To run DataDiffer on databases on your machine, just clone the github repo to a machine, and run the main.py file in your command line with the required command line arguments. That's it! The command line will return the output. 

# Running DataDiffer On Your Own Source/Target Collections
1. Install pymongo, deepdiff, and tqdm as follows: 

    pip install pymongo
    pip install tqdm
    pip install deepdiff

2. Clone the repo to your machine where you want to run DataDiffer.
3. Run the main.py file with the proper command line arguments.
4. See the ouput in the command line!


# Running Test Scripts
If you want to run any of the test scripts, then create an envrionment file(s) as needed based on your migration needs. The environment file should look something like this:

    export SOURCE_URI=""
    export SOURCE_DB=""
    export SOURCE_COLL=""
    export TARGET_URI=""
    export TARGET_DB=""
    export TARGET_COLL=""

Aftert that, source the environment file, then run the appropriate bash test script.
