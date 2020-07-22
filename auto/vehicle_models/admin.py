from django.contrib import admin

from .models import VehicleBrand, VehicleModel, VehicleSubModel
# Register your models here.
admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)
admin.site.register(VehicleSubModel)