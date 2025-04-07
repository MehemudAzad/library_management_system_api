# views/borrow_views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from ..serializers.borrow_serializers import BorrowBookSerializer, ReturnBookSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class BorrowBookView(APIView):
    authentication_classes = [JWTAuthentication]  # Enforce JWT authentication
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated
    
    def post(self, request):
        # Ensure the member is authenticated
        if not request.user.is_authenticated:
            return Response({
                "success": False,
                "status": 403,
                "message": "You must be logged in to borrow a book."
            }, status=status.HTTP_403_FORBIDDEN)
            
        serializer = BorrowBookSerializer(data=request.data)
        if serializer.is_valid():
            borrow = serializer.save()
            return Response({
                "success": True,
                "status": 200,
                "message": "Book borrowed successfully",
                "data": {
                    "borrowId": borrow.borrowId,
                    "bookId": str(borrow.book.bookId),
                    "memberId": str(borrow.member.id),  # Changed from borrow.member.memberId to borrow.member.id
                    "borrowDate": borrow.borrowDate
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReturnBookView(APIView):
    authentication_classes = [JWTAuthentication]  # Enforce JWT authentication
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated
    
    def post(self, request):
        # Ensure the member is authenticated
        if not request.user.is_authenticated:
            return Response({
                "success": False,
                "status": 403,
                "message": "You must be logged in to borrow a book."
            }, status=status.HTTP_403_FORBIDDEN)
            
        serializer = ReturnBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "status": 200,
                "message": "Book returned successfully"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
