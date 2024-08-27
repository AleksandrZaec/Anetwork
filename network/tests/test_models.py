import pytest
from network.models import Network, Product


@pytest.mark.django_db
def test_create_network():
    supplier = Network.objects.create(
        name="Supplier",
        email="supplier@gmail.com",
        country="USA",
        city="New York",
        street="Wall Street",
        house_number="99",
        level=35
    )

    node = Network.objects.create(
        name="Retailer",
        email="retailer@gmail.com",
        country="USA",
        city="New York",
        street="Wall Street",
        house_number="77",
        supplier=supplier,
        level=33
    )

    assert node.name == "Retailer"
    assert node.supplier.name == "Supplier"


@pytest.mark.django_db
def test_create_product():
    supplier = Network.objects.create(
        name="Supplier",
        email="supplier@gmail.com",
        country="USA",
        city="New York",
        street="Wall Street",
        house_number="66",
        level=21
    )

    product = Product.objects.create(
        name="Product",
        model="Model 1",
        supplier=supplier
    )

    assert product.name == "Product"
    assert product.supplier == supplier
