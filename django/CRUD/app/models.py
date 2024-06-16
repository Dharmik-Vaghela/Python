from django.db import models

# Create your models here.
class Teacher(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    Salary = models.CharField(max_length=6)
    Email = models.EmailField(max_length=50)
    Contact = models.BigIntegerField()