from django.db import models


class FastFood(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    star = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.name
