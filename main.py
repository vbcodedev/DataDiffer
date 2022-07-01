import pymongo
import math
import argparse
from bson.json_util import dumps
from deepdiff import DeepDiff 
from tqdm import tqdm

def dataCompare(source_uri, target_uri, db1, db2, coll1, coll2, percent):
    client1 = pymongo.MongoClient(source_uri, serverSelectionTimeoutMS=5000)
    client2 = pymongo.MongoClient(target_uri, serverSelectionTimeoutMS=5000)
    first_database = client1[db1]
    second_database = client2[db2]
    first_collection = first_database[coll1]
    second_collection = second_database[coll2]
    #get a random sample of documents from the source based on the percent the user inputs and store in sampled_docs
    sampled_docs = get_rand_sample_docs(first_collection, second_collection,percent)
    #Loop through all sampled_docs find_one based on matching ID in second collection and store the result of that find in queried_doc
    for document in tqdm(sampled_docs): 
        queried_doc = second_collection.find_one({"_id": document["_id"]})
        #If it cannot find any matching ID document in queried_doc then tell user the doc was not found in target from source 
        if queried_doc == None:
            str = "The following document based on it's ID was not found from teh source in the target:\n{0}"
            print(str.format(document))
            return False
        pretty_q_doc_str = dumps(queried_doc, indent = 4, separators =("", " = "))
        pretty_document_str = dumps(document, indent = 4, separators =("", " = "))
        #compare the strings of the documents to ensure they are equal for each document 
        if pretty_document_str == pretty_q_doc_str: 
            continue
        #if the dumps strings are not equal, it can be 2 cases: first case is that the right keys with the right values are there, just in the wrong order, 
        #or the second case is there is guranteed differences such as some portion missing/extra portion 
        else: 
            # DeepDiff is a package that compares 2 dictionaries, 2 iterables, 2 strings or 2 other objects and returns their differences as a deepdiff.diff
            # It is important to note however, that DeepDiff does not check for order of key/value pairs, so although our dumps strings earlier could have had 
            # a difference (due to order being different) DeepDiff would not return anything as a difference. So for combatting this issue, a check is required 
            # to see if the length of the result of that DeepDiff call = 0, then you know that the only difference was the orders from source to target. If that 
            # is not the case, and the length of the diff is greater than 0, then there are actual differences that you have to report those differences to the 
            # user.

            # To summarize, there are 3 paths when comparing documents: 
            #     1) the dump strings match each other in the document comparison and then we continue. If all the documents go down this path, at the end you print that it passed and return True.
            #     2) there is a difference with the dump strings, but the length of DeepDiff is 0, so then we know the only difference can be the order, so we print that to user and return False.
            #     3) there is a difference with the dump strings, but the length is anything else but 0, so we know there are actual differences, so we print to user and return False.

            diff = DeepDiff(document, queried_doc, verbose_level=2, report_repetition=True).pretty()
            if len(diff) == 0:
                str = "****Failed!**** The values are all there but the order of values is different from source to target. Source document looks like this:\n{0}\nTarget document looks like this:\n{1}"
                print(str.format(pretty_document_str, pretty_q_doc_str))
                return False
            else:
                diff_str = "****Failed!**** There are differences that were found in the target doc as seen here {0}\nfrom the source doc as seen here {1}\nTHE DIFFERENCES CONSIST SPECIFICALLY OF THE FOLLOWING:\n{2}"
                print(diff_str.format(pretty_document_str, pretty_q_doc_str, diff))
                return False
    #Checks to see if reverse 
    if reverse_check(first_collection, second_collection, percent) == True:
        print("****PASSED!**** All Chosen Data Samples Match Exactly from Source to Target!")
        

# get_rand_sample function description 
# 1. First this function does all the basic checks to see if either collection is empty or if one collection has more documents than the other.
# 2. Next, it gets a rounded sample_size from the percent value the user chose to compare. 
# 3. Lastly, it takes that sample size and via aggregation it gets a random sample of docs of that sample_size from the source and stores it into 
#    a list and returns that list 

def get_rand_sample_docs(first_coll, second_coll, percent):
    coll1_num_docs = first_coll.count_documents({})
    coll2_num_docs= second_coll.count_documents({})

    #Checks if first collection is empty
    if coll1_num_docs == 0: 
        print("Your first collection is empty, please re-check you selected the right source collection.")
        return False
    
    #Checks if second collection is empty 
    if coll2_num_docs == 0:
        print("Your second collection is empty, please re-check you selected the right target collection.")
        return False

    #Checks to see if number of documents in both are equal
    if coll1_num_docs != coll2_num_docs:
        str = "Both collections do not have the same number of documents. Source collection has {0} documents. Target collection has {1} documents." 
        print(str.format(coll1_num_docs, coll2_num_docs))
        return False

    #Convert from percent to a number of documents to sample from in the aggregation
    sample_size = math.ceil((percent/100) * coll1_num_docs)

    #Aggregate the random sample based on sample_size
    sampled_docs = list(first_coll.aggregate([
        {"$sample": {"size": sample_size}}
    ]))
    return sampled_docs

# reverse_check description
# This function creates a new random sample of documents based on the same percent the user chose, this time from the target instead of source. 
# For each document in the sample, it checks from target and compares it against the source (opposite case) to check if all documents in the sample
# exist in target. If a document doesn't exist, it will notify the user which document is not found in source and return False. Returns True if all 
# documents from sample in target exist in source. 

def reverse_check(coll1, coll2, percent):
    #inputting in reverse order for get_rand_sample_docs for getting a random sample of docs from coll2 this time
    sampled_docs = get_rand_sample_docs(coll2, coll1, percent)
    for document in sampled_docs:
        queried_doc = coll1.find_one({"_id": document["_id"]})
        #If it cannot find any matching ID document in queried_doc then tell user the doc was not found in target from source 
        if queried_doc == None:
            str = "The following document based on it's ID was not found from the target in the source:\n{0}"
            print(str.format(document))
            return False
    return True

#Main method
if __name__ == "__main__":
    #order diff, same content is "s_one", "s_two"
    #same everything is "sample_one", "sample_two"
    #same num of docs but one doc is missing id is wrong for one of them is "sa_one", "sa_two"
    #extra field in target than source is "sam_one", "sam_two"

    parser = argparse.ArgumentParser(description="DataDiffer Tool.")

    parser.add_argument("--source-uri", type=str, required=True, help="Source URI")
    parser.add_argument("--target-uri", type=str, required=True, help="Target URI")
    parser.add_argument("--source-namespace", type=str, required=True, help="Source Namespace as <database>.<collection>")
    parser.add_argument("--target-namespace", type=str, required=True, help="Target Namespace as <database>.<collection>")
    parser.add_argument("--source-collection", type=str, required=True, help="Source Collection")
    parser.add_argument("--target-collection", type=str, required=True, help="Target Collection")
    parser.add_argument("--percent", type=int, required=True, help="Percent of collection to compare")

    args = parser.parse_args()
    dataCompare(args.source_uri, args.target_uri, args.source_namespace, args.target_namespace, args.source_collection, args.target_collection, args.percent)