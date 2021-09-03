from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE,related_name='profile')
    age = models.PositiveSmallIntegerField(_("age"), null=True, blank=True)
    phone_number = models.PositiveSmallIntegerField(_("phone number"), unique=True, null=True, blank=True)
    bio = models.TextField(_('bio'), null=True, blank=True)

    class Meta:
        verbose_name = _('profiles')
        verbose_name_plural = _('profiles')

    def __str__(self):
        return self.user


def save_profile(sender, **kwargs):
    if kwargs['created']:
        p1 = Profile(user=kwargs['instance'])
        p1.save()


post_save.connect(save_profile, sender=User)