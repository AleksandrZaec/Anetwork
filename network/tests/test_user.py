import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from users.models import User


@pytest.mark.django_db
def test_user_create():
    url = reverse('users:register')
    data = {
        "email": "users@gmail.com",
        "password": "qwertyui"
    }
    client = APIClient()
    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert User.objects.count() == 1
