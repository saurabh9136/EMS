from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=250)
    age = models.IntegerField(max_length=10)    
    is_active = models.BooleanField(default=False)