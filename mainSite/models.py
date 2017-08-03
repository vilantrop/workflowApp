from django.db import models

# Create your models here.

class Shoe(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    photo = models.CharField(max_length=1000)

    def __str__(self):
        return self.brand + ' - ' + self.name

class User(models.Model):
    photo = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    nick = models.CharField(max_length=200)
