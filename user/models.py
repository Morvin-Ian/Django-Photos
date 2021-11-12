from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(max_length=200, null=True,blank=True)
    time = models.DateTimeField(default=timezone.now())
    image = models.ImageField(upload_to='Posted_Pictures', null=True,blank=True)

    def __str__(self):
        return f"{self.user.username}'s Post"

    def get_absolute_url(self):
        return reverse('details', kwargs = {'pk':self.pk})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg',upload_to='Profiles')

    def __str__(self):
        return f"{self.user.username}'s Profile"