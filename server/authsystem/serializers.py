from rest_framework import serializers
from .models import User, Photos


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=256
    )
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'password', 'username', 'email', 'is_staff', 'token')
        read_only_fields = ['token']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=256
    )
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)