from django.db import models

# Create your models here.

class UserDetail(models.Model):
    UserName=models.CharField(max_length=250,unique=True)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=10)


class ProductRegistration(models.Model):
    product_name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=50)
    purchase_date = models.DateField()
    
    WARRANTY_CHOICES = [
        ('Active', 'Active'),
        ('Expired', 'Expired'),
        ('Not Available', 'Not Available'),
    ]
    warranty_status = models.CharField(max_length=20, choices=WARRANTY_CHOICES)

    def __str__(self):
        return self.product_name
