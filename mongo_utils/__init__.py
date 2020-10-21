from pymongo import MongoClient
import ssl
from datetime import datetime
import os
import re

MONGO_URL = os.environ.get(
    'MONGO_URL',
    'Specified environment variable is not set.'
)


client = MongoClient(MONGO_URL, ssl_cert_reqs=ssl.CERT_NONE)
db = client['api-wtr']


def update_one_mongo(post):
    # print(post)
    document_id = post['_id']
    post['updatedAt'] = datetime.utcnow()
    db.stations.update_one({'_id': document_id}, {"$set": post}, upsert=False)
    print('Updated: ', post)
    return post


def create_one_mongo(post, collection):
    post_id = db[collection].insert_one(post).inserted_id
    print(post_id)
    # print('Created: ', post)
    return post


# create_one_mongo({"stationID": "test"}, 'stations')
