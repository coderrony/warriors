from django.contrib import admin
from .models import Trucks, Cars, Bikes
# Register your models here.

admin.site.register(Trucks)
admin.site.register(Cars)
admin.site.register(Bikes)
