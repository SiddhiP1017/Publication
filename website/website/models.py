# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields here if needed
    role = models.CharField(max_length=50, choices=[('faculty', 'Faculty'), ('organization', 'Organization')])
