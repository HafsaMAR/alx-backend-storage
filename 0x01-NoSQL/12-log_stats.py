#!/usr/bin/env python3
"""log stats"""


from pymongo import MongoClient


def log_stats():
    "Stats on the logs database"
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    collection = db['nginx']

    num_document = collection.count_documents({})

    print(f"{num_document} logs")
    print("Methods:")

    get = collection.count_documents({"method": "GET"})
    post = collection.count_documents({"method": "POST"})
    put = collection.count_documents({"method": "PUT"})
    patch = collection.count_documents({"method": "PATCH"})
    delete = collection.count_documents({"method": "DELETE"})

    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")

    num_document = collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{num_document} status check")


if __name__ == "__main__":
    log_stats()
