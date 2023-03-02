from django.shortcuts import render

from .models import Trucks, Bikes, Cars
# Create your views here.


def trucks(request):
    truck = Trucks.objects.all()
    return render(request, 'trucks.html', context={"truck": truck})


def bikePage(request):
    bike = Bikes.objects.all()
    return render(request, 'bike.html', context={'bikes': bike})


def carPage(request):
    car = Cars.objects.all()
    return render(request, 'car.html', context={'cars': car})
