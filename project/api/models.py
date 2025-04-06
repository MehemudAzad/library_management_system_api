from django.db import models

# Create your models here.
import uuid
from django.db import models

class Book(models.Model):
    bookId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publishedYear = models.IntegerField()
    totalCopies = models.PositiveIntegerField()
    availableCopies = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Member(models.Model):
    memberId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    membershipDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BorrowRecord(models.Model):
    borrowId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    borrowDate = models.DateTimeField(auto_now_add=True)
    returnDate = models.DateTimeField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"
