from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
