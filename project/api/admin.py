from django.contrib import admin
from .models import Book, Member, BorrowRecord

# Register your models here
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(BorrowRecord)
