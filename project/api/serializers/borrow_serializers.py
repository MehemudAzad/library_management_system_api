# serializers/borrow_serializers.py

from rest_framework import serializers
from ..models import BorrowRecord, Book, Member
from django.utils import timezone

class BorrowBookSerializer(serializers.ModelSerializer):
    bookId = serializers.UUIDField(write_only=True)
    memberId = serializers.UUIDField(write_only=True)

    class Meta:
        model = BorrowRecord
        fields = ['borrowId', 'bookId', 'memberId', 'borrowDate']
        read_only_fields = ['borrowId', 'borrowDate']

    def validate(self, data):
        try:
            book = Book.objects.get(pk=data['bookId'])
        except Book.DoesNotExist:
            raise serializers.ValidationError("Book not found.")

        if book.availableCopies < 1:
            raise serializers.ValidationError("No available copies for this book.")

        try:
            Member.objects.get(pk=data['memberId'])
        except Member.DoesNotExist:
            raise serializers.ValidationError("Member not found.")

        return data

    def create(self, validated_data):
        book = Book.objects.get(pk=validated_data['bookId'])
        member = Member.objects.get(pk=validated_data['memberId'])

        book.availableCopies -= 1
        book.save()

        borrow = BorrowRecord.objects.create(book=book, member=member)
        return borrow


class ReturnBookSerializer(serializers.Serializer):
    borrowId = serializers.UUIDField()

    def validate(self, data):
        try:
            borrow = BorrowRecord.objects.get(pk=data['borrowId'], returnDate__isnull=True)
        except BorrowRecord.DoesNotExist:
            raise serializers.ValidationError("Borrow record not found or already returned.")
        data['borrow'] = borrow
        return data

    def save(self, **kwargs):
        borrow = self.validated_data['borrow']
        borrow.returnDate = timezone.now()
        borrow.save()

        book = borrow.book
        book.availableCopies += 1
        book.save()
        return borrow
