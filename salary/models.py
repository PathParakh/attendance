from django.db import models

# Create your models here.

class staff(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    salary = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    date = models.DateField()