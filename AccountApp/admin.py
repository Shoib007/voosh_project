from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.admin import SimpleListFilter

class UserFilter(SimpleListFilter):
    title = 'is_public'
    parameter_name = 'is_public'

    def lookups(self, request, model_admin):
        return (
            ('public', 'Public'),
            ('private', 'Private'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'public':
            return queryset.filter(is_public=True)
        if self.value() == 'private':
            return queryset.filter(is_public=False)

admin.site.register(User)
