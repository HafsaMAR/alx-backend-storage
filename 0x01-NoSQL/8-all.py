#!/usr/bin/env python3
"""Module for listing documents in a collection"""

from pymongo.collection import Collection
from typing import Iterator


def list_all(mongo_collection):
    """
    lists all the documents in the collection mongo_collection
    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection.

    Returns:
        Iterator[dict]: An iterator over all the
        documents in the collection.
    """
    return mongo_collection.find()
