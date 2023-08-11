from django.contrib import admin
from .models import Testimonial
# Register your models here.

class TestiAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'testimonial', 'images')


admin.site.register(Testimonial, TestiAdmin)
