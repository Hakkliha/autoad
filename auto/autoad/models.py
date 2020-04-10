from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify
#from django.contrib.gis.utils import GeoIP
import datetime
import shutil
import os
from django.conf import settings

from .vehicledata import (BRAND_LIST, VEHICLE_TYPE_LIST, BODY_TYPE_CHOICES, NEW_USED_LIST, FUEL_TYPE, TRANSMISSION_TYPE, DRIVE_TYPE, STEERINGWHEEL_POSITION, COUNTRY_OF_ORIGIN_LIST,
	O_CONDITION_LIST,
	T_CONDITION_LIST,
	I_CONDITION_LIST,
	AD_TYPE_LIST
)


'''def get_location():
	g = GeoIP()
	ip = request.META.get('REMOTE_ADDR', None)
	if ip:
	   return city = g.city(ip)['city']
	else:
	   return city = 'Rome' # default city'''

def year_choices():
    return [(r,r) for r in range(1884, datetime.date.today().year+2)]


def current_year():
    return datetime.date.today().year

def current_today():
	return datetime.date.today().day

def current_month():
	month = datetime.date.today().month
	if month < 10:
		return f'0{month}'
	else:
		return month

# Create your models here.
class Vehicle(models.Model):
	pictures 			= models.CharField(max_length=1000, null=True, blank=True)
	vehicle_type		= models.CharField(max_length=60, blank=True, choices=VEHICLE_TYPE_LIST)
	price				= models.PositiveIntegerField(validators=[MaxValueValidator(100000000)], blank=True)
	reduced_price		= models.PositiveIntegerField(validators=[MaxValueValidator(100000000)], blank=True, null=True)
	value_added_tax		= models.BooleanField(blank=True)
	new_used			= models.CharField(max_length=60, blank=True, choices=NEW_USED_LIST)
	warranty_until		= models.DateField(auto_now=False, blank=True, null=True)
	insurance_until		= models.DateField(auto_now=False, blank=True, null=True)
	valid_mot_until		= models.DateField(auto_now=False, blank=True, null=True)
	service_history_bk	= models.BooleanField(blank=True, default=False)
	accident			= models.BooleanField(blank=True, default=False)
	damaged				= models.BooleanField(blank=True, default=False)
	vehicle_model_year	= models.IntegerField(choices=year_choices(), default=current_year())
	brand 				= models.CharField(max_length=60, blank=True, choices=BRAND_LIST)
	vehicle_model 		= models.CharField(max_length=60, blank=True)
	vehicle_model_other = models.CharField(max_length=60, blank=True, null=True)
	body_type			= models.CharField(max_length=60, blank=True, choices=BODY_TYPE_CHOICES)
	power_kw 			= models.PositiveIntegerField(blank=True, default=1, null=True)
	displacement_cm		= models.PositiveIntegerField(blank=True, default=1, null=True)
	cylinders			= models.PositiveIntegerField(blank=True, default=1, null=True)
	fuel				= models.CharField(max_length=60, blank=True, choices=FUEL_TYPE)
	fuel_tank_l			= models.DecimalField(max_digits=5, decimal_places=1, blank=True, default='', null=True)
	fuel_usage_city		= models.DecimalField(max_digits=5, decimal_places=1, blank=True, default='', null=True)
	fuel_usage_out		= models.DecimalField(max_digits=5, decimal_places=1, blank=True, default='', null=True)
	fuel_usage_average	= models.DecimalField(max_digits=5, decimal_places=1, blank=True, default='', null=True)
	mileage_km			= models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000000)])
	transmission		= models.CharField(max_length=60, blank=True, choices=TRANSMISSION_TYPE)
	drive				= models.CharField(max_length=60, blank=True, choices=DRIVE_TYPE)
	doors				= models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True, default=2, null=True)
	seats				= models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True, default=4, null=True)
	equipment			= models.TextField(blank=True, null=True)
	steeringwheel		= models.CharField(max_length=10, blank=True, choices=STEERINGWHEEL_POSITION)
	location			= models.CharField(max_length=140, blank=True, null=True)
	country_of_origin	= models.CharField(max_length=140, blank=True, choices=COUNTRY_OF_ORIGIN_LIST)
	date_of_import		= models.DateField(auto_now=False, blank=True, null=True)
	is_import			= models.BooleanField(blank=True, default=False)
	nr_owner			= models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, default=2)
	customisation		= models.BooleanField(blank=True, default=False)
	customisation_desc	= models.TextField(blank=True, null=True)
	vin_code			= models.CharField(max_length=50, blank=True)
	numberplate			= models.CharField(max_length=20, blank=True)
	optical_condition	= models.CharField(max_length=1400, blank=True, choices=O_CONDITION_LIST)
	technical_condition = models.CharField(max_length=1400, blank=True, choices=T_CONDITION_LIST)
	interior_condition 	= models.CharField(max_length=1400, blank=True, choices=I_CONDITION_LIST)
	last_service_date	= models.DateField(auto_now_add=False, blank=True, null=True)
	last_service_desc	= models.TextField(blank=True, null=True)
	vehicle_desc		= models.TextField(blank=True, null=True)
	ad_type				= models.CharField(max_length=30, blank=True, choices=AD_TYPE_LIST)
	creation_datetime	= models.DateTimeField(auto_now=True, blank=True)
	promoted			= models.DateTimeField(auto_now=True, blank=True)
	booked_until		= models.BooleanField(blank=True, default=False)
	active				= models.BooleanField(blank=True, default=True)
	user 				= models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True)

	def get_absolute_url(self):
		return reverse("autoad:vehicle-detail", kwargs={'pk': self.id})

	def __str__(self):
		if self.vehicle_model_other:
			return f"({self.id}) {self.vehicle_model_year} {self.brand} {self.vehicle_model} {self.vehicle_model_other} by {self.user} {self.creation_datetime}"
		else:
			return f"({self.id}) {self.vehicle_model_year} {self.brand} {self.vehicle_model} by {self.user} {self.creation_datetime}"

	class Meta:
		ordering = ('creation_datetime', 'price',)	

	def delete(self, *args, **kwargs):
		print(self.pictures[9:30])
		shutil.rmtree(os.path.join(settings.MEDIA_ROOT, self.pictures[9:30]), ignore_errors=True) 
		super().delete(*args, **kwargs)