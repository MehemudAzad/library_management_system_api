# from django.urls import path
# from . import views

# urlpatterns = [
#     # Book CRUD endpoints
#     path("books/", views.BookListCreateView.as_view(), name="book_list_create"),            # GET all books, POST create book
#     path("books/<uuid:bookId>/", views.BookRetrieveUpdateDeleteView.as_view(), name="book_detail"),  # GET, PUT, DELETE by ID

#     # Member endpoints (optional expansion)
#     path("members/", views.MemberListCreateView.as_view(), name="member_list_create"),
#     path("members/<uuid:memberId>/", views.MemberRetrieveUpdateDeleteView.as_view(), name="member_detail"),

#     # BorrowRecord endpoints (optional expansion)
#     path("borrow-records/", views.BorrowRecordListCreateView.as_view(), name="borrow_record_list_create"),
#     path("borrow-records/<uuid:borrowId>/", views.BorrowRecordRetrieveUpdateDeleteView.as_view(), name="borrow_record_detail"),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views.book_views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
