import sys
import pymongo
import math
from bson.json_util import dumps
from deepdiff import DeepDiff 
from tqdm import tqdm

conn_str = sys.argv[1]
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

def dataCompare(client, db1, db2, coll1, coll2, percent):
    first_database = client[db1]
    second_database = client[db2]

    first_collection = first_database[coll1]
    second_collection = second_database[coll2]

    coll1_num_docs = first_collection.count_documents({})
    coll2_num_docs= second_collection.count_documents({})

    #Checks if first collection is empty
    if coll1_num_docs == 0: 
        print("Your first collection is empty, please re-check you selected the right source collection.")
        return False
    
    #Checks if second collection is empty 
    if coll2_num_docs == 0:
        print("Your second collection is empty, please re-check you selected the right target collection.")
        return False

    #Checks to see if num of documents in both match up 
    if coll1_num_docs != coll2_num_docs:
        str = "Both collections do not have the same number of documents. Source collection has {0} documents. Target collection has {1} documents." 
        print(str.format(coll1_num_docs, coll2_num_docs))
        return False

    #Convert from percent to a number of documents to sample from in the aggregation
    sample_size = math.ceil((percent/100) * coll1_num_docs)

    #Aggregate the random sample based on sample_size
    sampled_docs = list(first_collection.aggregate([
        {"$sample": {"size": sample_size}}
    ]))
    
    #Loop through all sampled_docs, find each doc in the second_collection and store as queried_doc 
    for document in tqdm(sampled_docs): 
        queried_doc = second_collection.find_one({"_id": document["_id"]})
        if queried_doc == None:
            str = "The following document based on it's ID was not found in the target collection:\n{0}"
            print(str.format(document))
            return False
        pretty_q_doc_str = dumps(queried_doc, indent = 4, separators =("", " = "))
        pretty_document_str = dumps(document, indent = 4, separators =("", " = "))
        if pretty_document_str == pretty_q_doc_str: 
            continue
        else: 
            diff = DeepDiff(document, queried_doc, verbose_level=2, report_repetition=True).pretty()
            if len(diff) == 0:
                str = "****Failed!**** The values are all there but the order of values is different from source to target. Source document looks like this:\n{0}\nTarget document looks like this:\n{1}"
                print(str.format(pretty_document_str, pretty_q_doc_str))
                return False
            else:
                diff_str = "****Failed!**** There are differences that were found in the target doc as seen here {0}\nfrom the source doc as seen here {1}\nTHE DIFFERENCES CONSIST SPECIFICALLY OF THE FOLLOWING:\n{2}"
                print(diff_str.format(pretty_document_str, pretty_q_doc_str, diff))
                return False
    print("****PASSED!**** Data samples match exactly from source to target!")
    return True

#Main method
if __name__ == "__main__":
    #order diff, same content dataCompare(client, "s_one", "s_two", "s_one", "s_two", 100) 
    #same everything dataCompare(client, "sample_one", "sample_two", "sample_one", "sample_two", 100)
    #same num of docs but one doc is missing id is wrong for one of them dataCompare(client, "sa_one", "sa_two", "sa_one", "sa_two", 100)
    #extra field in target than source dataCompare(client, "sam_one", "sam_two", "sam_one", "sam_two", 100)

    dataCompare(client, "sample_one", "sample_two", "sample_one", "sample_two", 100)