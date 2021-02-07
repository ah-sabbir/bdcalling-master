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
            'incomingBy',
            'accountFiverr',
            'amount',
            'percentage',
            'chargesFiverr',
            'fiverrId',
            'clientName',
            'emailAddress',
            'orderPageURL',
            'spreadsheetLink',
            'remarks',
            'allocationTeamName',
            'orderStatus',
            'deliveredBy',
            'deliveredDate',
            'deliveredAmount',
        ]
        widgets = {
            'accountFiverr': forms.TextInput(attrs={
                'type':'text',
                'placeholder':'Fiverr Account',
                }),
            'amount': forms.TextInput(attrs={
                'type':'number',
                'placeholder':'Amount of This order',
                'alt':'amount',
            }),
            'spreadsheetLink':forms.TextInput(attrs={
                "placeholder":"SpreadSheet URL"
            }),
            'orderPageURL':forms.TextInput(attrs={
                "placeholder":"Order Page URL"
            }),
            'fiverrId':forms.TextInput(attrs={
                "placeholder":"Client Fiverr ID"
            }),
            'orderStatus':forms.TextInput(attrs={
                "placeholder":"Order Status"
            }),
            'remarks':forms.TextInput(attrs={
                "placeholder":"Remarks"
            }),
            'clientName':forms.TextInput(attrs={
                "placeholder":"Client Name"
            }),
            'emailAddress':forms.TextInput(attrs={
                "placeholder":"Client Email Address"
            }),
            'allocationTeamName':forms.TextInput(attrs={
                "placeholder":"Team or Employee Name"
            }),
            'deliveredDate':forms.TextInput(attrs={
                "placeholder":"Delivered Date"
            }),
        }
        labels = {
            'amount':"Amount"
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