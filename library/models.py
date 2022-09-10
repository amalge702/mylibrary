from django.db import models
from django.utils import timezone

# Create your models here.

class admin_user(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)
    emailid=models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class books(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True)
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Pages = models.IntegerField(max_length=3)
    language=models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)