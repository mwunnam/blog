from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'first_name', 'last_name', 'email', 'created_at', 'updated_at', 'is_publisher', 'image']
        read_only_fields = ['id', 'created_at', 'updated_at']
        