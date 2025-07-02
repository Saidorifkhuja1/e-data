from rest_framework import serializers

from user.models import User
from .models import File
from rest_framework import serializers

class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'name']


class FileSerializer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)

    class Meta:
        model = File
        fields = ['uid', 'name', 'description', 'file', 'file_type', 'file_size', 'uploaded_at', 'user']
        read_only_fields = ['uid', 'file_type', 'file_size', 'uploaded_at', 'user']


class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['name', 'description', 'file']
