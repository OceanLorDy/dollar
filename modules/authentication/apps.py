from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.authentication'

    def ready(self):
        import modules.authentication.signals
