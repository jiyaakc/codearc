from django.db import models

# Create your models here.

class UserDetail(models.Model):
    UserName=models.CharField(max_length=250,unique=True)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=10)