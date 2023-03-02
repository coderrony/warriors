from django.urls import path
from . import views

urlpatterns = [
    path('trucks/', views.trucks, name='trucks'),
    path('bikes/', views.bikePage, name='bikes'),
    path('cars/', views.carPage, name='cars'),

]
