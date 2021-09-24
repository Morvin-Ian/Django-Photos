from django.apps import AppConfig


class AuthenticConfig(AppConfig):
    name = 'authentic'

    def ready(self):
        import authentic.signals
