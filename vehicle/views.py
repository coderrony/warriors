from django.shortcuts import render
from .models import Trucks, Bikes, Cars

from .utils import paginationProject
# Create your views here.


def trucks(request):
    truck = Trucks.objects.all()
    custom_range, projects = paginationProject(request, truck, 1)

    return render(request, "trucks.html", context={'projects': projects, 'custom': custom_range})


def bikePage(request):

    bike = Bikes.objects.all()
    custom_range, projects = paginationProject(request, bike, 1)

    return render(request, "bike.html", context={'projects': projects, 'custom': custom_range})


def carPage(request):
    car = Cars.objects.all()
    custom_range, projects = paginationProject(request, car, 1)
    return render(request, 'car.html', context={'projects': projects, 'custom': custom_range})


def carDetails(request, pk):
    details = Cars.objects.get(id=pk)
    return render(request, 'carDetails.html', context={'details': details})


def truckDetails(request, pk):
    details = Trucks.objects.get(id=pk)
    return render(request, 'truckDetails.html', context={'details': details})


def bikeDetails(request, pk):
    details = Bikes.objects.get(id=pk)
    return render(request, 'bikeDetails.html', context={'details': details})
