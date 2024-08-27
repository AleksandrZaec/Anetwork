from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Network, Product
from .permissions import IsActiveEmployee
from .serializers import NetworkSerializer, ProductSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    """
    Эндпоинт звена сети
    """
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['country']
    search_fields = ['city']
    permission_classes = [IsActiveEmployee]

    def perform_update(self, serializer):
        serializer.save(debt=self.get_object().debt)


class ProductViewSet(viewsets.ModelViewSet):
    """
    Эндпоинт продукта
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]
