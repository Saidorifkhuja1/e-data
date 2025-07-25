from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('uid', 'phone_number', 'name', 'email', 'is_active', 'is_admin')
    list_filter = ('is_admin', 'is_active')
    fieldsets = (
        ('Personal Info', {'fields': ('phone_number', 'name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'name', 'email', 'password1', 'password2', 'is_active', 'is_admin', 'is_superuser'),
        }),
    )
    search_fields = ('phone_number', 'email', 'name')
    ordering = ('phone_number',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
