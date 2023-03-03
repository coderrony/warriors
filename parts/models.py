from django.db import models
import uuid
# Create your models here.


class Parts(models.Model):
    part_num = models.CharField(max_length=200)
    year = models.IntegerField()
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    part_image = models.ImageField(
        null=True, blank=True, upload_to="parts_images/", default="coming-soon2.jpg")
    price = models.CharField(max_length=50)
    qty = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.model
