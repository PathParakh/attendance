from django.db import models

# Create your models here.

class staff(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=250, null=True)
    role = models.CharField(max_length=250, null=True)
    salary = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=250, null=True)
    number = models.CharField(max_length=250, null=True)
    date = models.DateField()
    
class attendance(models.Model):
    id = models.AutoField
    staff_id = models.CharField(max_length=250, null=True)
    attendance = models.CharField(max_length=250, null=True)
    date = models.DateField()

class amount(models.Model):
    id = models.AutoField
    staff_id = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)