from bson.json_util import dumps
import pymongo

def get_connection_to_collection(self, user_id, password, database, collection):
    mongodb_url = "mongodb://" + user_id + ":" + password + "@ds019708.mlab.com:19708/" + database
    client = pymongo.MongoClient(mongodb_url)
    db = client[database]
    return db[collection]

def get_by_nmae(title):
    try:
        collection = get_connection_to_collection(*get_mongo_creds())
        response = collection.find({"title": title})
        return dumps(response)
    except:
        return dumps({"ERROR": "QUERY FAILED"})

def get_by_ingredients(self, param):
    try:
        collection = get_connection_to_collection(*get_mongo_creds())
        response = ''
        return dumps(response)
    except:
        return dumps({"ERROR": "QUERY FAILED"})

def get_mongo_creds():
    #This needs to reach out to S3 for credentials that will be stored there
    return ["hiEntropy","S~lm*n376~Atomic360!","recipes","drinks"]