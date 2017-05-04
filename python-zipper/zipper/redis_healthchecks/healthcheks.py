from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException
import redis

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)


class RedisHealthCheckBackend(BaseHealthCheckBackend):
    def check_status(self):
        info = redis_client.info()
        if not(info):
            raise HealthCheckException("redis")
        # The test code goes here.
        # You can use `self.add_error` or
        # raise a `HealthCheckException`,
        # similar to Django's form validation.
        pass

    def identifier(self):
        return self.__class__.__name__  # Display name on the endpoint.
