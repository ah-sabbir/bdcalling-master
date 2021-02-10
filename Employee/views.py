from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class home(TemplateView):
    def __init__(self):
        pass
    def get(self,request):
        return HTTPResponse("hello employee")
    def post(self,request):
        pass