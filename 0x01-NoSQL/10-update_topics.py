#!/usr/bin/env python3
"""Update all documents in the mongo_collection based on a given name"""


def update_topics(mongo_collection, name, topics):
    """Update all documents in the mong_collection
    based on a given name.

    Args:
        mongo_collection: pymongo collection object.
        name: Name to match documents to be updated.
        topics: Dictionary containing the new attributes and their values.

    Returns:
        The result of the update operation.
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}})
