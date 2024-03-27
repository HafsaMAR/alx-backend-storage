#!/usr/bin/env python3
"""Writing strings to Redis"""


import redis
import uuid
from typing import Union, Callable, Optional, Any

class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Initialize Redis client and flush the db"""
        self._Redis_client = redis.Redis(host='localhost', port=6379, db=0)
        self._Redis_client.flushdb()

    def store(self, data: Union[bytes, str, int, float]) -> str:
        """Generate a random key"""
        key = str(uuid.uuid4())
        self._Redis_client.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[Any],Any]] = None) -> Any:
        """Retrieve data from Redis using the provided key"""
        data = self._Redis_client.get(key)

        if data is None:
            return None

        if fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str) -> str:
        """Returns the value stored in the redis store as str"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Returns the value stored in the redis store as int"""
        return self.get(key,int)
