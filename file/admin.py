from django.contrib import admin
from .models import File

@admin.register(File)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']

