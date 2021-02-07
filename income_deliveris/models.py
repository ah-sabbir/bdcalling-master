from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

class incDelivery(models.Model):
    class whoIncome(models.TextChoices):
        shamim = "SM",_('Shamim Osman')
        sharif = "SF", _('Shariful Islam')
        mamun = "MN", _('Mamunur Rashid')
        tuhin = "TN", _('Tuhin Hossain')
        jabed = "JD", _('Jabed')
        amirul = "AL", _('Amirul Sohan')
        mehedi = "MI", _('Mehedi Hasan Moni')
        rony = "RY", _('Rony Hossen')

    order_status = (
        ("NRA","NRA"),
        ("WIP", "WIP"),
        ("NE", "NE"),
        ("Completed", "Completed"),
        ("Delivered", "Delivered"),
        ("Revision", "Revision"),
        ("Issues", "Issues"),
        ("Cancelled", "Cancelled"),
    )

    order_recieve_person = models.CharField(
        max_length = 2,
        choices=whoIncome.choices,
        default= "",
    )
    order_recieve_date = models.DateTimeField('date_published', auto_now=True)
    order_recieve_fiverr_account = models.CharField(max_length=20,blank=False)
    order_amount = models.FloatField(null=True, blank=True, default=0.0)
    order_amount_minus_percentage = models.FloatField(null=True, blank=True, default=0.0)
    order_charges_for_fiverr = models.FloatField(null=True, blank=True, default=0.0)
    client_fiverr_id = models.CharField(max_length=50, blank=False)
    client_name = models.CharField(max_length=20)
    client_email_address = models.EmailField()
    order_page_url = models.URLField(blank=False)
    order_spreadsheet_url = models.URLField(blank=False)
    order_remarks = models.CharField(max_length=50,blank=True)
    order_working_team_or_person_name = models.CharField(max_length=50,blank=True)
    order_status = models.CharField(
        max_length=15,
        choices = order_status,
        default = ""
        )
    order_delivery_person = models.CharField(
        max_length = 2,
        choices=whoIncome.choices,
        default= ""
    )
    order_delivery_date = models.DateField(default=datetime.date.today,blank=True)
    order_delivery_amount = models.FloatField(null=True, blank=False, default=0.0)
    

##    def save(self, *args, **kwargs):
##        
##        if name.endswith("S.L"):
##            self.country = 'Company country'
##            self.foundation_year = 'Company year'
##            
##        super().save(*args, **kwargs)

    # remarks
    # team_EmpName
    # def is_amount(self):
    #     zero = 0.0
    #     if self.percentage is not zero:
    #         return self.amount - (self.amount*(self.percentage/100))
    #     else:
    #         return self.amount
