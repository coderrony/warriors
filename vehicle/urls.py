from django.urls import path
from . import views

urlpatterns = [
    path('trucks/', views.trucks, name='trucks'),
    path('bikes/', views.bikePage, name='bikes'),
    path('cars/', views.carPage, name='cars'),
    path('cars_details/<str:pk>/', views.carDetails, name='carsDetails'),
    path('bike_details/<str:pk>/', views.bikeDetails, name='bikeDetails'),
    path('truck_details/<str:pk>/', views.truckDetails, name='TruckDetails'),

]
