from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from ..models import Member  # Adjusted the import path to use relative import

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = Member
        fields = ('email', 'name', 'phone', 'password')

    def create(self, validated_data):
        user = Member.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            phone=validated_data['phone'],
            password=validated_data['password'],
        )
        return user
