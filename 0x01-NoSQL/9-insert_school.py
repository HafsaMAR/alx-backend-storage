#!/usr/bin/env python3
"insert new document"


def insert_school(mongo_collection, **kwargs):
    """Insert new document is the collection
    mongo_collection

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection.
        kwargs (dict): document to insert

    Returns:
        Id of the new element"""
    return mongo_collection.insert_one(kwargs).inserted_id
