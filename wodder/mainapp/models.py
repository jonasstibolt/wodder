from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=18, null=False)
    bio = models.TextField(max_length=300)
    profile_pic = models.URLField(max_length=4096, blank=True, null=True)


    def __str__(self):
        return f"{self.username} - {self.name}"
    
class WorkoutListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=4096, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')

    def __str__(self):
        return self.title