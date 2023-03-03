
from django.db import models
import uuid
# Create your models here.


class Trucks(models.Model):
    mode_name = models.CharField(max_length=150)
    colors = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.CharField(max_length=50)
    mpg = models.CharField(max_length=200)
    radio = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    qty = models.CharField(max_length=200)
    truck_image = models.ImageField(
        null=True, blank=True, upload_to="truck_images/", default="933_ps.jpg")
    truck_image2 = models.ImageField(
        null=True, blank=True, upload_to="truck_images/", default="933_ps.jpg")
    truck_image3 = models.ImageField(
        null=True, blank=True, upload_to="truck_images/", default="933_ps.jpg")
    truck_image4 = models.ImageField(
        null=True, blank=True, upload_to="truck_images/", default="933_ps.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.mode_name


class Cars(models.Model):
    mode_name = models.CharField(max_length=150)
    colors = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.CharField(max_length=50)
    mpg = models.CharField(max_length=200)
    radio = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    qty = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    car_image = models.ImageField(
        null=True, blank=True, upload_to="car_images/", default="coming-soon2.jpg")
    car_image2 = models.ImageField(
        null=True, blank=True, upload_to="car_images/", default="coming-soon2.jpg")
    car_image3 = models.ImageField(
        null=True, blank=True, upload_to="car_images/", default="coming-soon2.jpg")
    car_image4 = models.ImageField(
        null=True, blank=True, upload_to="car_images/", default="coming-soon2.jpg")

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.mode_name


class Bikes(models.Model):
    mode_name = models.CharField(max_length=150)
    colors = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.CharField(max_length=50)
    mpg = models.CharField(max_length=200)
    radio = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    qty = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    bike_image = models.ImageField(
        null=True, blank=True, upload_to="bike_images/", default="coming-soon2.jpg")
    bike_image2 = models.ImageField(
        null=True, blank=True, upload_to="bike_images/", default="coming-soon2.jpg")
    bike_image3 = models.ImageField(
        null=True, blank=True, upload_to="bike_images/", default="coming-soon2.jpg")
    bike_image4 = models.ImageField(
        null=True, blank=True, upload_to="bike_images/", default="coming-soon2.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.mode_name
