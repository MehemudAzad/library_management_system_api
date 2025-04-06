from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Member
from ..serializers.member_serializers import MemberSerializer



# Read All Members
class MemberListView(APIView):
    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(
            {
                "success": True,
                "status": status.HTTP_200_OK,
                "message": "Members retrieved successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


# Read Member by memberId
class MemberDetailView(APIView):
    def get(self, request, memberId):
        try:
            member = Member.objects.get(memberId=memberId)
            serializer = MemberSerializer(member)
            return Response(
                {
                    "success": True,
                    "status": status.HTTP_200_OK,
                    "message": "Member retrieved successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Member.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "Member not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# Update Member
class MemberUpdateView(APIView):
    def put(self, request, memberId):
        try:
            member = Member.objects.get(memberId=memberId)
            serializer = MemberSerializer(member, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "success": True,
                        "status": status.HTTP_200_OK,
                        "message": "Member updated successfully",
                        "data": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {
                    "success": False,
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Invalid data",
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Member.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "Member not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# Delete Member
class MemberDeleteView(APIView):
    def delete(self, request, memberId):
        try:
            member = Member.objects.get(memberId=memberId)
            member.delete()
            return Response(
                {
                    "success": True,
                    "status": status.HTTP_200_OK,
                    "message": "Member successfully deleted",
                },
                status=status.HTTP_200_OK,
            )
        except Member.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "Member not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
