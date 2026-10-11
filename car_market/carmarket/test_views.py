import pytest
from django.urls import reverse
from carmarket.models import Car


@pytest.mark.django_db
def test_car_list_view(client):
    # Ro'yxat ko'rsatuvchi view uchun test
    url = reverse('car_list_cbv')
    response = client.get(url)

    # status_code 200 ekanini tekshirish
    assert response.status_code == 200
