from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
import PIL

from .managers import UserManager

def profilePath(instance, filename):
    return f"profile_pics/{instance.username}/{filename}"

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, blank=True)
    is_public = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to=profilePath, null=True, blank=True)
    profile_url = models.URLField(null=True, blank=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name


    def __str__(self):
        return self.username