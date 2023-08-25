from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    useremail = models.EmailField(max_length=50)
    userpassword = models.CharField(max_length=30)
    confirmpassword = models.CharField(max_length=30)
    userphone = models.CharField(max_length=10)
    useraddress = models.TextField(max_length=200)

    def __str__(self):
        return self.username
    





