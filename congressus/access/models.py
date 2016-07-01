from django.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField

from events.models import Event


class AccessControl(models.Model):
    event = models.ForeignKey(Event, related_name='access')

    name = models.CharField(_('name'), max_length=200)
    slug = AutoSlugField(populate_from='name')

    location = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


AC_TYPES = (
    ('ok', _('ok')),
    ('wrong', _('wrong')),
    ('used', _('used')),
    ('maybe', _('maybe')),
)

class LogAccessControl(models.Model):
    access_control = models.ForeignKey(AccessControl, related_name='log_access')
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=AC_TYPES, default="ok")
