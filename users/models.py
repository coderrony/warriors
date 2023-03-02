from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to="profiles/", default="profiles/defaulImg.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
