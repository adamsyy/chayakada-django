from django.db import models
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Main(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='main/images/')
    price=models.CharField(max_length=30)



