from network.serializers import NetworkSerializer, ProductSerializer
from network.models import Network, Product


def test_network_serializer():
    node = Network(
        name="Retailer",
        email="retailer@gmail.com",
        country="USA",
        city="New York",
        street="Wall Street",
        house_number="7",
        level=17
    )

    serializer = NetworkSerializer(instance=node)
    data = serializer.data

    assert data['name'] == "Retailer"
    assert data['email'] == "retailer@gmail.com"


def test_product_serializer():
    supplier = Network(
        name="Supplier",
        email="supplier@gmail.com",
        country="USA",
        city="New York",
        street="Wall Street",
        house_number="8",
        level=18
    )

    product = Product(name="Product", model="Model 5", supplier=supplier)
    serializer = ProductSerializer(instance=product)
    data = serializer.data

    assert data['name'] == "Product"
    assert data['model'] == "Model 5"
