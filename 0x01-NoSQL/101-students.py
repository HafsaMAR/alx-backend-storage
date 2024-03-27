#!/usr/bin/env python3


from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    
    Args:
        mongo_collection : pymongo collection object.
    
    Returns:
        list of dictionaries"""
    pipeline = [
        {"$unwind": "$scores"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$scores.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]

    return list(mongo_collection.aggregate(pipeline))
