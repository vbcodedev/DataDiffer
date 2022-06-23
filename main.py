import sys
import pymongo
#from collections import OrderedDict

conn_str = sys.argv[1]
#client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000, document_Class=OrderedDict)
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

first_database = client["sample_one"]
second_database = client["sample_two"]

first_collection = first_database["sample_one"]
second_collection = second_database["sample_two"]

def dataCompare(client, db1, db2, coll1, coll2, sample_size):
    #Sample from source collection to check in the target collection 
    sampled_docs = first_collection.aggregate([
        {"$sample": {"size": sample_size}}
    ])
    #holds those in target that are finally found 
    queried_docs = []
    for doc in sampled_docs: 
        #holds all potential mataches, get results plus more
        query_docs = list(second_collection.find(doc))
        #loop through the potential results and check for exact match 
        for queried_document in query_docs:
            if queried_document == doc:
                continue
            else: 
                return False
        #add the final correct matches to the array 
        queried_docs.extend(query_docs)
        
    if(len(queried_docs) == sample_size):
        print(queried_docs)
        print("Yes, they are identical")
        return True
    else: 
        return False

if __name__ == "__main__":
    dataCompare(client, "sample_one", "sample_two", "sample_one", "sample_two", 2)
