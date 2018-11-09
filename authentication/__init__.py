from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        import authentication.signals


# this is how we register custom app with django
default_app_config = 'authentication.AuthenticationConfig'
