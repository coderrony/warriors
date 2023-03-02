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


def carDetails(request, pk):
    details = Cars.objects.get(id=pk)
    return render(request, 'carDetails.html', context={'details': details})


def truckDetails(request, pk):
    details = Trucks.objects.get(id=pk)
    return render(request, 'truckDetails.html', context={'details': details})


def bikeDetails(request, pk):
    details = Bikes.objects.get(id=pk)
    return render(request, 'bikeDetails.html', context={'details': details})
