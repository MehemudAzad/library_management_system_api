from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from ..models import Book
from ..serializers.book_serializers import BookSerializer
from django.shortcuts import get_object_or_404


class BookViewSet(viewsets.ViewSet):
    queryset = Book.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]  # Require login for all actions
    print(authentication_classes)

    def check_admin_permission(self, request):
        """Helper function to check if the user is an admin."""
        if not request.user.is_staff:
            return Response(
                {
                    "success": False,
                    "status": 403,
                    "message": "Only admin users can perform this action.",
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        return None  # Return None if the user is an admin

    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(
            {
                "success": True,
                "status": 200,
                "message": "Books retrieved successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def create(self, request):
        # Only admin can create books
        permission_response = self.check_admin_permission(request)
        if permission_response:
            return permission_response

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "status": 201,
                    "message": "Book created successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "status": 400,
                "message": "Invalid data",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def retrieve(self, request, pk=None):
        book = get_object_or_404(Book, bookId=pk)
        serializer = BookSerializer(book)
        return Response(
            {
                "success": True,
                "status": 200,
                "message": "Book retrieved successfully",
                "data": serializer.data,
            }
        )

    def update(self, request, pk=None):
        permission_response = self.check_admin_permission(request)
        if permission_response:
            return permission_response
        # PUT request: Only admins can update books
        book = get_object_or_404(Book, bookId=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "status": 200,
                    "message": "Book updated successfully",
                    "data": serializer.data,
                }
            )
        return Response(
            {
                "success": False,
                "status": 400,
                "message": "Invalid data",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def destroy(self, request, pk=None):
        # DELETE request: Only admins can delete books
        permission_response = self.check_admin_permission(request)
        if permission_response:
            return permission_response

        book = get_object_or_404(Book, bookId=pk)
        book.delete()
        return Response(
            {"success": True, "status": 200, "message": "Book successfully deleted"},
            status=status.HTTP_200_OK,
        )
