import pytest
from carmarket.models import Car


@pytest.mark.django_db
def test_car_model():
    # 1. Bitta obyekt yaratish
    car = Car.objects.create(
        brand="BMW",
        model="M5",
        price=95000.00,
        year=2023,
    )

    # 2. Assert bilan maydonini tekshirish
    assert car.brand == "BMW"
    assert car.model == "M5"
    assert car.price == 95000.00
