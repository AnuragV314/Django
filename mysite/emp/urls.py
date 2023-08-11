from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", emp_home),
    path('addEmp/', addEmp),
    path('deleteEmp/<int:empId>/',deleteEmp),
    path('updateEmp/<int:empId>/', updateEmp),
    path('do_update_emp/<int:emp_Id>/', do_update_emp),
    
]