from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(_("age"))
    avatar = models.ImageField(_("avatar"), blank=True, upload_to='avators')
    phone_number = models.PositiveSmallIntegerField(_("phone number"), unique=True)
    bio = models.TextField(_('bio'), blank=True)


    class Meta:
        verbose_name = _('profiles')
        verbose_name_plural = _('profiles')

    def __str__(self):
        return self.user
