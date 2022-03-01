from django.db import models

# Create your models here.

class sukku(models.Model):
    EMPNO=models.IntegerField()
    MGR=models.IntegerField()
    SAL=models.IntegerField()
    JOB=models.IntegerField()
    HIREDATE=models.DateField()
    LOC=models.CharField(max_length=50)
    class Meta:
        db_table='ramya'
    
