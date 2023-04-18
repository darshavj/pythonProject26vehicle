from django.db import models
class About(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    place=models.CharField(max_length=250)
class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)
    type = models.IntegerField()
class Enter(models.Model):
    model = models.CharField(max_length=200)
    image = models.FileField()
    number = models.IntegerField(max_length=25)
    wheels = models.CharField(max_length=50)
    description = models.CharField(max_length=250)


# Create your models here.
