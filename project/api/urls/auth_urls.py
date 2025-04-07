from django.urls import path
from api.views.auth_views import RegisterView, MyTokenObtainPairView
from api.views.auth_views import CreateAdminView  # Admin registration
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('create-member/', RegisterView.as_view(), name='create_member'),
    path('create-admin/', CreateAdminView.as_view(), name='create_admin'),  # Admin registration
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
