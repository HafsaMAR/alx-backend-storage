#!/usr/bin/env python3
"""Writing strings to Redis"""


import redis
import uuid
from typing import Union

class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Initialize Redis client and flush the db"""
        self._Redis_client = redis.Redis()
        self._Redis_client.flushdb()

    def store(self, data: Union[bytes, str, int, float]) -> str:
        """Generate a random key"""
        key = str(uuid.uuid4())

        self._Redis_client.set(key, data)

        return key

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))