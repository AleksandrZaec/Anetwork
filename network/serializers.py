from rest_framework import serializers
from network.models import Network, Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор продукта
    """

    class Meta:
        model = Product
        fields = '__all__'


class NetworkSerializer(serializers.ModelSerializer):
    """
    Сериализатор звена сети
    """

    products = ProductSerializer(many=True, read_only=True)
    level = serializers.ChoiceField(choices=Network.LEVEL)

    class Meta:
        model = Network
        fields = ['id', 'name', 'email', 'country', 'city', 'street',
                  'house_number', 'supplier', 'debt', 'created_at', 'products', 'level']
        read_only_fields = ['debt']

    def update(self, instance, validated_data):
        validated_data.pop('debt', None)
        return super().update(instance, validated_data)
