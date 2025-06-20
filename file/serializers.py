from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['uid', 'name', 'description', 'file', 'file_type', 'file_size', 'uploaded_at', 'user']
        read_only_fields = ['uid', 'file_type', 'file_size', 'uploaded_at', 'user']


class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['name', 'description', 'file']
