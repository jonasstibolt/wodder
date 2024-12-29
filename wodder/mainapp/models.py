from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=18, null=False)
    bio = models.TextField(max_length=300)
    profile_pic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)


    def __str__(self):
        return self.name