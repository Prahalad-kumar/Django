from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=models.EmailField()
    dob=models.DateField()
    mobile_num=models.CharField(max_length=10)
    address=models.TextField()

class Doctor(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=models.EmailField()
    specialization=models.CharField(max_length=30)
    mobile_num=models.CharField(max_length=10)
    address=models.TextField()
    