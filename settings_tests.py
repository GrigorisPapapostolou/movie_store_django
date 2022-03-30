
CACHES['default'] = {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.0.5:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
}
CELERY_BROKER_URL = "redis://192.168.0.5:6379"
CELERY_RESULT_BACKEND = "redis://192.168.0.5:6379"