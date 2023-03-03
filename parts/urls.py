from django.urls import path
from . import views

urlpatterns = [
    path('parts/', views.spareParts, name='parts'),
    path('partsDetails/<str:pk>/', views.PartDetails, name='partsDetails'),

]
