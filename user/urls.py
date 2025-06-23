from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view()),
    path('all_users/', UserListAPIView.as_view()),
    path('profile/update/<uuid:uid>/', UpdateProfileView.as_view()),
    path('profile/delete/<uuid:uid>/', DeleteProfileAPIView.as_view()),
    path('profile/retrieve/', RetrieveProfileView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('reset_password/', PasswordResetView.as_view()),

]