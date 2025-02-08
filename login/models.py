from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
import re
from django.core.exceptions import ValidationError


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





def validate_pan(value):
    pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
    if not re.match(pattern, value):
        raise ValidationError("Invalid PAN number format. Example: ABCDE1234F")

class Agent(models.Model):
    pan_number = models.CharField(max_length=10, unique=True, validators=[validate_pan])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
