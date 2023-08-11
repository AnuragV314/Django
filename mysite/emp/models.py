from django.db import models

# Create your models here.

class emp(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=55)
    empId = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=10)


    def __str__(self):
        return self.name

