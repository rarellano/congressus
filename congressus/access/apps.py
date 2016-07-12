from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AccessConfig(AppConfig):
    name = 'access'
    verbose_name = _('Access')
