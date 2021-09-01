from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    star = models.CharField(max_length=5)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.name
