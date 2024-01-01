from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"

    # NEEDED FOR SIGNALS MODULE :
    def ready(self):
        import user.signals
