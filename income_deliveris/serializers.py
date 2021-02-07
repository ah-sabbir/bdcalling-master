from rest_framework import serializers
from income_deliveris.models import incDelivery
from django import forms

class incommingSerializer(serializers.ModelSerializer):
    class Meta:
        model = incDelivery
        fields = '__all__'


class entryForm(forms.ModelForm):
    class Meta:
        model = incDelivery
        fields = [
            'order_recieve_person',
            'order_recieve_fiverr_account',
            'order_amount',
            'order_amount_minus_percentage',
            'order_charges_for_fiverr',
            'client_fiverr_id',
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
        ]
        # widgets = {
        #     'accountFiverr': forms.TextInput(attrs={
        #         'type':'text',
        #         'placeholder':'Fiverr Account',
        #         }),
        #     'amount': forms.TextInput(attrs={
        #         'type':'number',
        #         'placeholder':'Amount of This order',
        #         'alt':'amount',
        #     }),
        #     'spreadsheetLink':forms.TextInput(attrs={
        #         "placeholder":"SpreadSheet URL"
        #     }),
        #     'orderPageURL':forms.TextInput(attrs={
        #         "placeholder":"Order Page URL"
        #     }),
        #     'fiverrId':forms.TextInput(attrs={
        #         "placeholder":"Client Fiverr ID"
        #     }),
        #     'remarks':forms.TextInput(attrs={
        #         "placeholder":"Remarks"
        #     }),
        #     'clientName':forms.TextInput(attrs={
        #         "placeholder":"Client Name"
        #     }),
        #     'emailAddress':forms.TextInput(attrs={
        #         "placeholder":"Client Email Address"
        #     }),
        #     'allocationTeamName':forms.TextInput(attrs={
        #         "placeholder":"Team or Employee Name"
        #     }),
        #     'deliveredDate':forms.TextInput(attrs={
        #         "placeholder":"Delivered Date"
                
        #     }),
        # }
        labels = {
            'order_recieve_person': "who recieve the order ? ",
            'order_recieve_fiverr_account': "Fiverr Account ",
            'order_amount': "Order's Total Amount",
            'order_amount_minus_percentage': "Percentage",
            'order_charges_for_fiverr': "Fiverr Charge",
            'client_fiverr_id': "Client's Fiverr Id",
            'client_name': "Client Name",
            'client_email_address': "Client Email",
            'order_page_url': "Order Page's Url",
            'order_spreadsheet_url': "Spread Sheet Url",
            'order_remarks': "Remarks",
            'order_working_team_or_person_name': "Team or Leader's Name", 
            'order_status': "Order Status",
            'order_delivery_person': "Who delivery the order ?",
            'order_delivery_date': "Delivery Date",
            'order_delivery_amount': "Delivery Amount"
        }
            # 'percentage': forms.
            # 'chargesFiverr': forms.
            # 'fiverrId': forms.
            # 'clientName': forms.
            # 'emailAddress': forms.
            # 'orderPageURL': forms.
            # 'spreadsheetLink': forms.
            # 'remarks': forms.
            # 'allocationTeamName': forms.
            # 'orderStatus': forms.
            # 'deliveredBy': forms.
            # 'deliveredDate': forms.
            # 'deliveredAmount': forms.
            # : forms.