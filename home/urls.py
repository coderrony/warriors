
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('search', views.search, name='search'),

]
