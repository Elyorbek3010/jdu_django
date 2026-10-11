from django.template import context
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from django.views.generic import ListView
from .forms import CarForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


@login_required
def car_list_fbv(request):
    cars = Car.objects.select_related('category').all()
    context = {
        'cars': cars,
    }
    return render(request, 'carmarket/car_list.html', context)


class CarListView(ListView):
    model = Car
    template_name = 'carmarket/car_list.html'
    context_object_name = 'cars'


def get_car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    context = {
        'car': car,
    }
    return render(request, 'carmarket/car_detail.html', context)


@login_required
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list_fbv')
    else:
        form = CarForm()  


    context = {
        'form': form,
    }
    return render(request, 'carmarket/car_form.html', context)


@login_required
def car_update(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_detail', id=car.id)
    else:
        form = CarForm(instance=car)
    return render(request, 'carmarket/car_form.html', {'form': form, 'car': car, 'is_edit': True})


@login_required
def car_delete(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list_fbv')
    return render(request, 'carmarket/car_confirm_delete.html', {'car': car})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('car_list_fbv')
    else:
        form = UserCreationForm()
    return render(request, 'carmarket/register.html', {'form': form})


from rest_framework import viewsets
from .serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
