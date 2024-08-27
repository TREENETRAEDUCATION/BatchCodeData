from django.db import models

# Create your models here.

# print(dir(models))
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=24)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=48)

    def __str__(self):
        return self.ename