import os
import redis

class RedisCacheSystem:
    def __init__(self):
        redis_host = os.environ.get('REDIS_HOST', 'localhost') 
        self.cache = redis.Redis(host=redis_host, port=6379)
        print(f'redis is ready on {redis_host}:6379')

    def find(self, query):
        print(f"redis is searching for {query}")
        return self.cache.get(query)
        

    def add(self, query, value):
        print(f"redis is saving :{query}")
        self.cache.set(query, value)

    def clear(self):
        self.cache.flushdb()
        print("redis is empty")