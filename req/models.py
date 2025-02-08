from django.db import models

class RepairRequest(models.Model):
    product_name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=50, blank=True, null=True)  # Optional
    problem_description = models.TextField()
    photo = models.ImageField(upload_to='repair_photos/')
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.product_name} - {self.model_number or 'No Model'}"
