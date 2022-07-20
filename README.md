# DataDiffer Overview
DataDiffer will compare a user defined percentage of random documents between two MongoDB/DocumentDB servers for a single collection in each. 

## Prerequisites that Must be Met for Running DataDiffer
1. Install pymongo, deepdiff, and tqdm software packages by running the following commands in the command line: 
```
    pip install pymongo
    pip install deepdiff
    pip install tqdm
```

2. Clone the repo to your machine where you want to run DataDiffer.
3. CD into DataDiffer

## To Run DataDiffer On Your Own Source/Target Collections
1. Assuming you have the prerequisites above met, run the main.py file in the command line with the proper arguments, such as the following: 
```
     python main.py --source-uri $SOURCE_URI --target-uri $TARGET_URI --source-namespace "$SOURCE_DB.$SOURCE_COLL" --target-namespace       
     "$TARGET_DB.$TARGET_COLL" --percent 100

```
Note: You can adjust the percent value as needed in the command above. 

2. See the ouput in the command line! 


## To Run DataDiffer Test Scripts
1. Assuming you have the prerequsities above met, create an envrionment file(s) as needed based on your migration needs. The environment file should look something like this with each variable filled out for your needs:
```
    export SOURCE_URI=""
    export SOURCE_DB=""
    export SOURCE_COLL=""
    export TARGET_URI=""
    export TARGET_DB=""
    export TARGET_COLL=""
```
2. Source the environment file you built in the command line with a command such as the following: 
```
    source <environment-file-name-here>.sh
```
3. Run the appropriate bash test script in the command line with a command such as the following: 
```
    bash <test-script-name-here>.sh
```
4. See the output in the command line!
