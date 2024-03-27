#!/usr/bin/env python3
"""Writing strings to Redis"""


import redis
import uuid
import functools
from typing import Union, Callable, Optional, Any


def count_calls(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """construct key for input and output lists"""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        # Append input arguments to the input list
        self._redis.rpush(input_key, str(args))

        # Execute the wrapper func to retrieve the output
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)

        return output
    return wrapper

def replay(method: Callable) -> None:
    method_name = method.__qualname__
    input_key = method_name + ":inputs"
    ouput_key = method_name + ":outputs"

    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(ouput_key, 0, -1)


    print(f"{method_name} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        input = inp.decode('utf-8')
        output = out.decode('utf-8')
        print(f"{method_name}{input} -> {output}")

class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Initialize Redis client and flush the db"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()
    
    @call_history
    @count_calls
    def store(self, data: Union[bytes, str, int, float]) -> str:
        """Generate a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[Any],Any]] = None) -> Any:
        """Retrieve data from Redis using the provided key"""
        data = self._redis.get(key)

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
