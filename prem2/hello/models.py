from django.db import models

# Create your models here.

class nav(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()

class naa(nav):
    empno=models.IntegerField()