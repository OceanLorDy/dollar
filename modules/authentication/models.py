from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=250, blank=True, null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Last Name")
    username = models.CharField(max_length=99, verbose_name="Username")
    password = models.CharField(max_length=99, verbose_name="Password")
    status = models.BooleanField(default=False, verbose_name="status")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
