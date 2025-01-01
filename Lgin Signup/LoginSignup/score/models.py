from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class Customer(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Auto-generated unique ID
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=128)  # Updated max_length to 128 to handle hashed passwords
    
    def __str__(self) -> str:
        return self.username + ' ' + self.email
