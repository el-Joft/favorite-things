from django.apps import AppConfig


class FavoriteConfig(AppConfig):
    name = 'favorite_things.apps.favorite'

    def ready(self):
        from . import signals  # noqa
