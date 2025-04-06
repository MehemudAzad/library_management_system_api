from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

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


class MemberManager(BaseUserManager):
    def create_user(self, email, name, phone, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, password):
        user = self.create_user(email, name, phone, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Member(AbstractBaseUser, PermissionsMixin):
    memberId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    membershipDate = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

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
