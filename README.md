# DataDiffer
DataDiffer will compare a user defined percentage of random documents between two MongoDB/DocumentDB servers for a single collection in each. 

To run DataDiffer on databases on your machine, just clone the github repo to a machine, and run the main.py file in your command line with the required command line arguments. That's it! The command line will return the output. 

If you want to run any of the test scripts, then create an envrionment file(s) as needed based on your migration needs. The environment file should look something like this.

    export SOURCE_URI=""
    export SOURCE_DB=""
    export SOURCE_COLL=""
    export TARGET_URI=""
    export TARGET_DB=""
    export TARGET_COLL=""

Aftert that, source the environment file, then run the appropriate bash test script.
