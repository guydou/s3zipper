from django.apps import AppConfig
from health_check.plugins import plugin_dir


class RedisHealthchecksConfig(AppConfig):
    name = 'redis_healthchecks'
    label = 'redis_healthchecks'
    verbose_name = 'redis_healthchecks'

    def ready(self):
        from .healthcheks import RedisHealthCheckBackend
        plugin_dir.register(RedisHealthCheckBackend)
