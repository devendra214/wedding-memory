from django.db import models
from cloudinary.models import CloudinaryField

class Memory(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    message = models.TextField()
    photo = CloudinaryField('image')

class GallerySettings(models.Model):
    is_public = models.BooleanField(default=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "Gallery Settings"