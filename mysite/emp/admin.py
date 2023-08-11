from django.contrib import admin

from .models import emp
# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'working', 'address', 'empId')
    list_editable = ('working',)
    search_fields = ('name',)
    list_filter = ('working',)

admin.site.register(emp, EmpAdmin)
