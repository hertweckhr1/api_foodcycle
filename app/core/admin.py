from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'company_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')} ),
        (_('Personal Info'), {'fields': ('point_of_contact', 'company_name', 'company_type', 'company_logo_image')}),
        (_('Permissions'), {'fields': ('is_donee', 'is_doner', 'is_active', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login')}),
        (_('Address'), {'fields': ('street_address', 'street_address2', 'city', 'state', 'zip')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(models.User, UserAdmin)
