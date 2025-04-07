from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from api.models import Member
from api.serializers.member_serializers import RegisterSerializer
from ..serializers.member_serializers import AdminRegisterSerializer, MyTokenObtainPairSerializer


# JWT Token Serializer with extra payload (optional)
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token["name"] = user.name
#         token["email"] = user.email
#         return token


# Custom login view
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Registration view
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "status": 200,
                    "message": "User registration successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateAdminView(generics.CreateAPIView):
    serializer_class = AdminRegisterSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Only allow admins to create other admins
        # if not request.user.is_staff:
        #     return Response(
        #         {
        #             "success": False,
        #             "status": 403,
        #             "message": "You must be an admin to create another admin.",
        #         },
        #         status=status.HTTP_403_FORBIDDEN,
        #     )

        # Proceed with admin creation
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                "success": True,
                "status": status.HTTP_201_CREATED,
                "message": "Admin user created successfully",
                "data": response.data,
            }
        )
