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


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('memberId', 'email', 'name', 'phone', 'membershipDate')


class UpdateMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'phone')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance
