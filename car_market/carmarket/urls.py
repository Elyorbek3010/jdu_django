from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    car_list_fbv,
    CarListView,
    get_car_detail,
    car_create,
    register,
    CarViewSet,
)
from django.contrib.auth.views import LoginView, LogoutView

# DRF Router
router = DefaultRouter()
router.register('carmarket', CarViewSet, basename='carmarket')

urlpatterns = [
    path('cars/fbv/', car_list_fbv, name='car_list_fbv'),
    path('cars/cbv/', CarListView.as_view(), name='car_list_cbv'),

    path('cars/<int:id>', get_car_detail, name='car_detail'),
    path('cars/add/', car_create, name='car_create'),

    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='carmarket/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='carmarket/logout.html'), name='logout'),

    path('api/', include(router.urls)),
]
