from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['uid', 'name', 'phone_number', 'email', 'password', 'confirm_password', 'is_admin']
        read_only_fields = ['uid']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Passwords do not match')
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email']
        read_only_fields = ['phone_number']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'phone_number', 'name', 'email']


class PasswordResetSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['old_password'] == data['new_password']:
            raise serializers.ValidationError("The new password cannot be the same as the old password.")
        return data
