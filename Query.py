from bson.json_util import dumps, loads
import pymongo, re


def get_connection_to_collection(user_id, password, database, collection):
    #mongodb://<dbuser>:<dbpassword>@ds019708.mlab.com:19708/recipes
    mongodb_url = "".join(["mongodb://", user_id, ":", password, "@ds019708.mlab.com:19708/", database])
    client = pymongo.MongoClient(mongodb_url)
    db = client[database]
    return db[collection]


def get_by_name(title):
    try:
        creds = get_mongo_creds()
        collection = get_connection_to_collection(*creds)
        return dumps(collection.find({"title": re.compile(title, re.IGNORECASE)}))
    except:
        return dumps({"ERROR": "QUERY FAILED"})



def get_by_ingredients(ingredients):
    try:
        collection = get_connection_to_collection(*get_mongo_creds())
        response = ''
        response = dumps(response)
    except:
        return dumps({"ERROR": "QUERY FAILED"})


def get_mongo_creds():
    creds = ""
    with open("./creds.json") as file:
        creds = file.read()
    creds = loads(creds)
    return [creds.get("username"), creds.get("password"), creds.get("db"), creds.get("collection")]
