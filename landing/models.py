from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)
