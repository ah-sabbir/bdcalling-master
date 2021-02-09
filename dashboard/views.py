from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from income_deliveris.models import incDelivery
from django.views.generic import TemplateView

# Create your views here.

class home(TemplateView):
    def __init__(self):
        self.template_name = "dashboard_with_pivot.html"
        self.context = { "name":"sabbir ahmmed"}
    def get(self,request):
        return render(request,self.template_name,context=self.context)
    def post(self,request):
        pass


def ptable(request):
    dataset = incDelivery.objects.all()
    data = serializers.serialize('json',dataset)
    print(data)
    return JsonResponse(data,safe=False)
