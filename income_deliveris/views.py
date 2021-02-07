from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser


from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView

from income_deliveris.serializers import incommingSerializer
from income_deliveris.models import incDelivery
from income_deliveris.serializers import entryForm

from django.shortcuts import redirect


class home(TemplateView):
    def __init__(self, *args, **kwargs):
        self.template_name = ""
    def get(self,request):
        return HttpResponse("hello django")

class income(APIView):
    def get(self,request):
        if request.GET.get('getForm' or None) == 'True':
            return HttpResponse(entryForm())
        incomeReport = incDelivery.objects.all()
        serializer = incommingSerializer(incomeReport, many=True)
        return render(request,'index.html',context={"data":serializer.data,'form':entryForm()})
    def post(self,request):
        serialized_form_data = entryForm(data = request.data)
        data = {}
        if serialized_form_data.is_valid():
            instance = serialized_form_data.save()
            return redirect("incoming_report")
        print("errors: ",serialized_form_data.errors)
        return Response(serialized_form_data.errors)
            
    def put(self, request):
        return HttpResponse("api put method")
    def delete(self, request):
        return HttpResponse("api delete method")
