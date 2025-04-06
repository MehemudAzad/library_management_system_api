# urls/borrow_urls.py or directly inside your api/urls.py

from django.urls import path
from ..views.borrow_views import BorrowBookView, ReturnBookView

urlpatterns = [
    path('borrow/', BorrowBookView.as_view(), name='borrow_book'),
    path('return/', ReturnBookView.as_view(), name='return_book'),
]
