from django.db import models

# Create your models here.


class VehicleBrand(models.Model):
    brandName = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f"{self.brandName}"

class VehicleModel(models.Model):
    brand = models.ForeignKey('VehicleBrand', on_delete=models.CASCADE)
    modelName = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f"{self.modelName}"

class VehicleSubModel(models.Model):
    parentModel = models.ForeignKey('VehicleModel', on_delete=models.CASCADE)
    subModel = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f"{self.subModel}"