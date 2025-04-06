from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from ..models import Book
from ..serializers import BookSerializer
from django.shortcuts import get_object_or_404


class BookViewSet(viewsets.ViewSet):
    queryset = Book.objects.all()

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
        book = get_object_or_404(Book, bookId=pk)
        book.delete()
        return Response(
            {"success": True, "status": 200, "message": "Book successfully deleted"},
            status=status.HTTP_200_OK
        )

