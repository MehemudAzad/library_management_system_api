# api/auth/auth_urls.py or api/books/books_urls.py
from django.urls import path
from ..views.member_views import MemberListView, MemberDetailView, MemberUpdateView, MemberDeleteView

urlpatterns = [
    # Member-related URLs
    # path('members/', CreateMemberView.as_view(), name='create_member'),
    path('members/', MemberListView.as_view(), name='get_members'),
    path('members/<uuid:id>/', MemberDetailView.as_view(), name='get_member_by_id'),
    path('members/<uuid:id>/', MemberUpdateView.as_view(), name='update_member'),
    path('members/<uuid:id>/', MemberDeleteView.as_view(), name='delete_member'),
]
