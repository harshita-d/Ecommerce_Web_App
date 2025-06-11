"""
Create Custom USer Model with email
"""

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    full_name = models.CharField(
        max_length=100, blank=True, null=True
    )  # optional field
    phone = models.CharField(max_length=100, null=True, blank=True)  # optional field

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        email_username, suffix = self.email.split("@")
        if self.full_name == "" or self.full_name == None:
            self.full_name = email_username
        if self.username == "" or self.username == None:
            self.username = email_username

        super().save(*args, **kwargs)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(
        upload_to="image", default="default/default-user.jpg", null=True, blank=True
    )  # optional
    full_name = models.CharField(max_length=100, blank=True, null=True)  # optional
    about = models.TextField(null=True, blank=True)  # optional
    gender = models.CharField(max_length=100, null=True, blank=True)  # optional
    country = models.CharField(max_length=100, null=True, blank=True)  # optional
    state = models.CharField(max_length=100, null=True, blank=True)  # optional
    city = models.CharField(max_length=100, null=True, blank=True)  # optional
    address = models.CharField(max_length=100, null=True, blank=True)  # optional
    date = models.DateTimeField(auto_now_add=True)  # automatic date
    pid = models.UUIDField(
        unique=True,
        max_length=20,
        default=uuid.uuid4,  # auto-generate a new UUID4
    )  # unique

    def __str__(self):
        return str(self.user.full_name)

    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name = self.user.full_name

        super().save(*args, **kwargs)
