from django.shortcuts import render

from vehicle.models import Bikes,Cars,Trucks

# Create your views here.


def homePage(request):
    return render(request, 'home.html')


def search(request):
    get_method = request.GET.copy()
    keywords = get_method.get('keywords') or None
    bike = Bikes.objects.all()
    car=Cars.objects.all()
    truck=Trucks.objects.all()
   
    if keywords:
        keyword = get_method['keywords']
        bike_list = bike.filter(mode_name__icontains=keyword)
        car_list = car.filter(mode_name__icontains=keyword)
        truck_list=truck.filter(mode_name__icontains=keyword)
       


    # print("bike list: ",bike_list)
    # print("car list: ",car_list)
    # print("Truck list: ",truck_list)
   
   
    context = {
        'bike_list':bike_list,
        'car_list':car_list,
        'truck_list':truck_list
    }
   
    return render(request,'search/search_result.html',context)