import sys
import pymongo
import math
from deepdiff import DeepDiff 
from tqdm import tqdm

conn_str = sys.argv[1]
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

def dataCompare(client, db1, db2, coll1, coll2, percent):
    first_database = client[db1]
    second_database = client[db2]

    first_collection = first_database[coll1]
    second_collection = second_database[coll2]

    #Checks if first collection is empty
    if first_collection.count_documents({}) == 0: 
        print("Your first collection is empty, please re-check you selected the right source collection")
        return False
    
    #Checks if second collection is empty 
    if second_collection.count_documents({}) == 0:
        print("Your second collection is empty, please re-check you selected the right target collection")
        return False

    #Checks to see if num of documents in both match up 
    if first_collection.count_documents({}) != second_collection.count_documents({}):
        print("Both collections do not have the same number of documents. " + "Source collection has " + str(first_collection.count_documents({})) + " documents. Target collection has " + str(second_collection.count_documents({})) + " documents.")
        return False

    #Convert from percent to a number of documents to sample from in the aggregation
    sample_size = math.ceil((percent/100) * first_collection.count_documents({}))

    #Checks for no documents to check scenario, Ex: 3 documents in collection put in 10% it would round to 0 
    if sample_size == 0:
        print("Given the collection size, your selected percentage value is too low, resulting in 0 documents to check, please increase the percent value")
        return False

    #Aggregate the random sample based on sample_size
    sampled_docs = list(first_collection.aggregate([
        {"$sample": {"size": sample_size}}
    ]))
 
    #Loop through all documents from sample
    for document in tqdm(sampled_docs): 
        #find that document from sample in the second_collection and store it as queried_doc
        #.find({"_id":document["_id"]})
        queried_doc = second_collection.find(document)
        #count num of docs in the second_collection that are the same as 'document' would be 0 or 1 
        num_queried_doc = second_collection.count_documents(document)
        if num_queried_doc == 0:
            print("The following document was not found in the target collection: " + str(document))
            return False
       #Only be 0 or 1 times
        for q_doc in queried_doc:
            if q_doc == document: 
                continue
            else: 
                diff = DeepDiff(q_doc, document)
                if diff == "":
                    print("The values are all there, order of values is different from source to target")
                    return False
                else:
                    print("Not a perfect match. These are the differences that were found: " + diff)
                    return False
    print("Data samples match!")
    return True

#Main method
if __name__ == "__main__":
    dataCompare(client, "sample_one", "sample_two", "sample_one", "sample_two", 100) 
