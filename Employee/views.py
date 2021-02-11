from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
# from .employeeForms import Attendanceform, employeeform
from .models import Attendance, Employees
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
# Create your views here.
# class home(TemplateView):
#     def __init__(self):
#         pass
#     def get(self,request):
#         return HTTPResponse("hello employee")
#     def post(self,request):
#         pass

template_row = """{% csrf_token %}
{{ formset.management_form }}
   {% for form in formset %}
      {{ form.employee.initial }} {{ form.employee}}  {{ form.attendance }}
<br><br>
   {% endfor %}"""

class Attendancecreate(FormView):
   def get(self, request):
      pass
# class Attendancecreate(FormView):
#     template_name = 'employee.html'
#     form_class = employeeform
#     success_url = '/dashboard/'

#     def form_valid(self,formset):
#         instance = formset.save(commit=False)
#         # for instance in instances:
#         #     instance.head_of_department = get_object_or_404(Head_of_department, email=self.request.user.email)
#         #     instance.save()
#         instance.save()
#         return HttpResponseRedirect('/dashboard/')