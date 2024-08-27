from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from users.apps import UserConfig
from django.urls import path
from users.views import UserCreateAPIView

app_name = UserConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
]