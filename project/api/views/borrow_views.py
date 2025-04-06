# views/borrow_views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from ..serializers.borrow_serializers import BorrowBookSerializer, ReturnBookSerializer

class BorrowBookView(APIView):
    def post(self, request):
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
                    "memberId": str(borrow.member.memberId),
                    "borrowDate": borrow.borrowDate
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReturnBookView(APIView):
    def post(self, request):
        serializer = ReturnBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "status": 200,
                "message": "Book returned successfully"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
