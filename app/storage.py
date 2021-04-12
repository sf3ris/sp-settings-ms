from redis import Redis
from os import environ


class Storage():
    redis: Redis

    def __init__(self):
        self.redis = Redis(host=environ.get('REDIS_HOST', 'redis'))
