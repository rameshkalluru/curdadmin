from django.db import models

# Create your models here.

class n1(models.Model):
    name=models.CharField(max_length=50)
    pan=models.IntegerField()

class n2(n1):
    age=models.IntegerField()
    adhar=models.IntegerField()

class n3(n2):
    salary=models.IntegerField()