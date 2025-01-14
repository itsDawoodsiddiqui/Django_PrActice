from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Removed trailing comma
    email_token = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)    

    def __str__(self):
        return f"Profile of {self.user.username}"


class Customer(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Auto-generated unique ID
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=128) 


    def __str__(self) -> str:
        return f"{self.username} - {self.email}"
