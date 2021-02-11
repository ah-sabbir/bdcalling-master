from django.contrib import admin
from .models import  Employees, Attendance, clientManagement
# Register your models here.
admin.site.register(Employees)
admin.site.register(Attendance)
admin.site.register(clientManagement)