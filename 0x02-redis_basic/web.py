#!/usr/bin/env python3

import requests
import redis
import time

# Initialize Redis client
redis_client = redis.Redis()

def get_page(url: str) -> str:
    # Increment the count of the URL accessed
    url_count_key = f"count:{url}"
    redis_client.incr(url_count_key)
    
    # Check if the page is cached
    cached_html = redis_client.get(url)
    if cached_html:
        return cached_html.decode('utf-8')
    
    # Fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.text
    
    # Cache the HTML content with expiration time of 10 seconds
    redis_client.setex(url, 10, html_content)
    
    return html_content
