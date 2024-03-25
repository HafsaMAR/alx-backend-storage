#!/usr/bin/env python3
"""Return cursor instance of documents"""


def schools_by_topic(mongo_collection, topic):
    """finds a list of documents of mongo_collection
    that have topic as a topic attribute

    Args:
        mongo_collection: pymongo collection object.
        topics: Dictionary containing the new attributes and their values.

    Returns:
        cursor instance of document tha have topic
    """
    return mongo_collection.find({"topics": topic})
