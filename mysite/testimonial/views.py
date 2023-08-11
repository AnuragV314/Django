from django.shortcuts import render
from django.http import HttpResponse
from .models import Testimonial
# Create your views here.

def testimonial(request):
    testi = Testimonial.objects.all()
    # name = testi.name
    # tes = testi.testimonial
    # image = testi.images
    # rating = testi.rating
    return render(request, 'TestimonialApp/home.html', {
        'testi':testi
    })



