## To Run DataDiffer Test Scripts
1. Assuming you have the prerequsities met from the general README, create an envrionment file(s) as needed based on your migration needs. The environment file should look something like this with each variable filled out for your needs:
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
