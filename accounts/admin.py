from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth import get_user_model
from django.contrib import admin

User = get_user_model()

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin




class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = "profile"
    verbose_name_plural = "profiles"


class ExtendedProfileAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, ExtendedProfileAdmin)
