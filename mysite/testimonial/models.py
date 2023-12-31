from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    images = models.ImageField(upload_to='testimonial')
    rating = models.IntegerField(max_length=1)


    def __str__(self):
        return self.name  
