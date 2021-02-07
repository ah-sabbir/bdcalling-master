from django.contrib import admin
from income_deliveris.models import incDelivery
# Register your models here.
class incDeliveryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in incDelivery._meta.get_fields()]

admin.site.register(incDelivery,incDeliveryAdmin)