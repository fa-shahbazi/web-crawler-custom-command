from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import random
import os
import requests
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE, related_name='profile')
    age = models.PositiveSmallIntegerField(_("age"), null=True, blank=True)
    bio = models.TextField(_('bio'), null=True, blank=True)
    phone_number = models.PositiveBigIntegerField(_('phone number'), unique=True, null=True, blank=True)

    class Meta:
        db_table = 'profiles'
        verbose_name = _('profiles')
        verbose_name_plural = _('profiles')


def save_profile(sender, **kwargs):
    if kwargs['created']:
        p1 = Profile(user=kwargs['instance'])
        p1.save()

post_save.connect(save_profile, sender=User)
