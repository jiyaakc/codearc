from django.db import models

# Create your models here.

class UserDetail(models.Model):
    UserName=models.CharField(max_length=250,null=False,unique=True)
    Email=models.EmailField(null=False,unique=True)
    Password=models.CharField(null=False,max_length=10)