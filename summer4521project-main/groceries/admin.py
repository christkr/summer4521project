from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Role
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Role)