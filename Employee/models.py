from django.db import models
# Create your models here.

class clientManagement(models.Model):
    name = models.ForeignKey("Employees",on_delete=models.CASCADE,related_name="Employees_name")
    income = models.FloatField(default=0.0)
    outcome = models.FloatField(default=0.0)
    
    def __str__(self):
        return '{0}'.format(self.name)
    
    # def save(self, *args, **kwargs):
    #     total_amount = order.object.all()
    #     percentage = self.order_amount_minus_percentage
    #     if total_amount > 0:
    #         self.order_delivery_amount = round(total_amount-(total_amount*(percentage/100)),2)
    #         self.order_charges_for_fiverr = round(total_amount - self.order_delivery_amount,2)
    #     super().save(*args, **kwargs)

attendance_choices = (
    ('absent', 'Absent'),
    ('present', 'Present')
)

class Employees(models.Model):
    name = models.CharField(max_length = 100,blank=True)
    email = models.EmailField()
    phone = models.IntegerField(unique=True)
    emp_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    emp_id = models.ForeignKey("Employees",on_delete=models.CASCADE,related_name="Employees_emp_id", null=True)
    attendance = models.CharField(max_length=8, choices=attendance_choices, blank=False)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return '{0} : {1} : {2}'.format(self.emp_id, self.attendance, self.date)

    
