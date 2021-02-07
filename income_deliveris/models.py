from django.db import models
from django.utils.translation import gettext_lazy as _

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

    incomingBy = models.CharField(
        max_length = 2,
        choices=whoIncome.choices,
        default= ""
    )
    date = models.DateTimeField('date_published', auto_now=True)
    accountFiverr = models.CharField(max_length=20,blank=False)
    amount = models.FloatField(null=True, blank=True, default=0.0)
    percentage = models.FloatField(null=True, blank=True, default=0.0)
    chargesFiverr = models.FloatField(null=True, blank=True, default=0.0)
    fiverrId = models.CharField(max_length=50, blank=False)
    clientName = models.CharField(max_length=20)
    emailAddress = models.EmailField()
    orderPageURL = models.URLField(blank=False)
    spreadsheetLink = models.URLField(blank=False)
    remarks = models.CharField(max_length=50,blank=True)
    allocationTeamName = models.CharField(max_length=50,blank=True)
    orderStatus = models.CharField(
        max_length=15,
        choices = order_status,
        default = ""
        )
    deliveredBy = models.CharField(
        max_length = 2,
        choices=whoIncome.choices,
        default= ""
    )
    deliveredDate = models.DateField(auto_now=False, auto_now_add=False,null=True, blank = False)
    deliveredAmount = models.FloatField(null=True, blank=False, default=0.0)
    
    # remarks
    # team_EmpName
    # def is_amount(self):
    #     zero = 0.0
    #     if self.percentage is not zero:
    #         return self.amount - (self.amount*(self.percentage/100))
    #     else:
    #         return self.amount