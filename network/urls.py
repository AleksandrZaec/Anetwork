from network.apps import NetworkConfig
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkViewSet, ProductViewSet

app_name = NetworkConfig.name
router = DefaultRouter()
router.register(r'network', NetworkViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
] + router.urls