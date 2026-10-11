from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Car


class CarAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.car = Car.objects.create(
            brand='TestBrand',
            model='TestModel',
            price=15000.00,
            year=2022
        )

    def test_car_list_api(self):
        response = self.client.get('/api/carmarket/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_car_detail_api(self):
        response = self.client.get(f'/api/carmarket/{self.car.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['brand'], 'TestBrand')
        self.assertEqual(response.data['model'], 'TestModel')
