from rest_framework import serializers
from .models import Book, Member, BorrowRecord


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class BorrowRecordSerializer(serializers.ModelSerializer):
    # Nested serializers for optional detailed views (optional)
    book = BookSerializer(read_only=True)
    member = MemberSerializer(read_only=True)
    
    # IDs for creation
    bookId = serializers.UUIDField(write_only=True)
    memberId = serializers.UUIDField(write_only=True)

    class Meta:
        model = BorrowRecord
        fields = ['borrowId', 'borrowDate', 'returnDate', 'book', 'member', 'bookId', 'memberId']

    def create(self, validated_data):
        book_id = validated_data.pop('bookId')
        member_id = validated_data.pop('memberId')
        return BorrowRecord.objects.create(
            book_id=book_id,
            member_id=member_id,
            **validated_data
        )
