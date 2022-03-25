from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    verbose_name = _('user')