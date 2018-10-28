from django.apps import AppConfig


class PostsAppConfig(AppConfig):
    name = 'post'
    label = 'post'
    verbose_name = 'Posts'

    def ready(self):
        import post.signals


default_app_config = 'post.PostsAppConfig'
