from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_type = models.CharField(max_length=50, choices=[('Customer', 'Customer'), ('Agent', 'Agent')])
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class AgentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    pan_number = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=50, choices=[('company', 'Company'), ('local', 'Local Repair Center')])
    company_name = models.CharField(max_length=255, blank=True, null=True)


class Product(models.Model):
    user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, blank=True, null=True)  # Link product to user
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    purchase_date = models.DateField()
    warranty_period = models.IntegerField(help_text="Warranty in months")

    def __str__(self):
        return f"{self.product_name} - {self.user.email}"

