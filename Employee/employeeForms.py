from django import forms
from django.forms.formsets import formset_factory
from django.forms import inlineformset_factory

from .models import Attendance, Head_of_department, Employees

# class Attendanceform(forms.ModelForm):
#     class Meta:
#         model = Attendance
#         fields = ['head_of_department','employees','attendance']

# class employeeform(forms.ModelForm):
#     class Meta:
#         model = Employees
#         fields = '__all__'