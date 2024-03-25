#!/usr/bin/env python3


from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')

db = client['logs']
collection = db['nginx']

num_document = collection.count_documents({})

print(f"{num_document} logs")

pipeline = [
    # Stage 1: Group by method and count occurrences
    {"$group": {"_id": "$method", "count": {"$sum": 1}}},

    {"$sort": {"count": -1}}
]

# Create a set of all possible methods
all_methods = {"GET", "POST", "PUT", "PATCH", "DELETE"}

result = collection.aggregate(pipeline)

print("Methods:")
for method in all_methods:
    count = 0
    for document in result:
        if document["_id"] == method:
            count = document["count"]
            break
    print(f"\tmethod {method}: {count}")

for document in result:
    print(f"\tmethod {document['_id']}: {document['count']}")

num_document = collection.count_documents({"method": "GET", "path": "/status"})

print(f"{num_document} status check")
