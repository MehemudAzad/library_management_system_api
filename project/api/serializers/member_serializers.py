from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from ..models import Member  # Adjusted the import path to use relative import
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AdminRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = Member
        fields = ("email", "name", "phone", "password")

    def create(self, validated_data):
        # Create an admin user
        user = Member.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            phone=validated_data["phone"],
            password=validated_data["password"],
        )

        # Set the user as admin
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = Member
        fields = ("email", "name", "phone", "password")

    def create(self, validated_data):
        user = Member.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            phone=validated_data["phone"],
            password=validated_data["password"],
        )
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"  # tell it we're using email

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"), email=email, password=password
            )

            if not user:
                raise serializers.ValidationError("Invalid email or password")

        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        refresh = self.get_token(user)

        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "name": user.name,
            "email": user.email,
        }

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["name"] = user.name
        token["email"] = user.email
        return token


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("id", "email", "name", "phone", "membershipDate")


class UpdateMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("name", "phone")

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.save()
        return instance
