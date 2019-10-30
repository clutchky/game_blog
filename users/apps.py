from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): # https://docs.djangoproject.com/en/2.2/ref/applications/#django.apps.AppConfig.ready
        import users.signals 
