from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from income_deliveris.models import incDelivery
from django.views.generic import TemplateView

# Create your views here.

fields = (
    'id',
    'order_recieve_person',
    'order_recieve_date',
    'marketplacename',
    'order_recieve_fiverr_account',
    'order_amount',
    'order_amount_minus_percentage',
    'order_charges_for_fiverr',
    'client_fiverr_id',
    'client_fiverr_profile',
    'client_name',
    'client_email_address',
    'order_page_url',
    'order_spreadsheet_url',
    'order_remarks',
    'order_working_team_or_person_name',
    'order_status',
    'order_delivery_person',
    'order_delivery_date',
    'order_delivery_amount',
)


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

    #print(data)
    return JsonResponse(data,safe=False)
