from django.db import models

from django.db import models

class Employee(models.Model):
    eno=models.IntegerField(unique=True)
    ename=models.CharField(max_length=50)
    esal=models.FloatField()
    ephno=models.CharField(max_length=100)
    eadd=models.CharField(max_length=100)



