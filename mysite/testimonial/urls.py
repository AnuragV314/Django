from django.urls import path
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', testimonial)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)