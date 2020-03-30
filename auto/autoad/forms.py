from django import forms

from .models import Vehicle, year_choices, current_year, current_today, current_month
from django.core import validators
from django.core.exceptions import ValidationError

from .vehicledata import (BRAND_LIST, VEHICLE_TYPE_LIST, BODY_TYPE_CHOICES, NEW_USED_LIST, FUEL_TYPE, TRANSMISSION_TYPE, DRIVE_TYPE, STEERINGWHEEL_POSITION, COUNTRY_OF_ORIGIN_LIST,
	O_CONDITION_LIST,
	T_CONDITION_LIST,
	I_CONDITION_LIST,
	AD_TYPE_LIST
)

from django.conf import settings



class VehicleForm(forms.ModelForm):
	pictures = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	vehicle_type = forms.ChoiceField(choices=VEHICLE_TYPE_LIST)
	new_used = forms.ChoiceField(choices=NEW_USED_LIST)
	price = forms.DecimalField(max_value=100000000, min_value=0, decimal_places=2)
	value_added_tax = forms.BooleanField(required=False, label='VAT included in price 20%', initial=False)
	warranty_until = forms.DateField(required=False, widget=forms.TextInput(attrs={
		"placeholder": 'DD-MM-YYYY'
		}))
	insurance_until = forms.DateField(required=False, widget=forms.TextInput(attrs={
		"placeholder": 'DD-MM-YYYY'
		}))
	valid_mot_until = forms.DateField(required=False, widget=forms.TextInput(attrs={
		"placeholder": 'DD-MM-YYYY'
		}))
	service_history_bk = forms.BooleanField(required=False, initial=False)
	accident = forms.BooleanField(required=False, initial=False)
	damaged = forms.BooleanField(required=False, initial=False)
	vehicle_model_year = forms.ChoiceField(choices=year_choices(), initial=current_year())
	brand = forms.ChoiceField(choices=BRAND_LIST)
	vehicle_model = forms.TextInput() # FRONT END JS MUUTUS !important lmao
	vehicle_model_other = forms.CharField(required=False)
	body_type = forms.ChoiceField(choices=BODY_TYPE_CHOICES)
	power_kw = forms.IntegerField(min_value=0, max_value=20000, required=False)
	displacement_cm = forms.IntegerField(min_value=0, required=False)
	cylinders = forms.IntegerField(min_value=0, max_value=32, required=False)
	fuel = forms.ChoiceField(choices=FUEL_TYPE)
	fuel_tank_l = forms.IntegerField(min_value=0, max_value=2000, required=False)
	fuel_usage_city = forms.DecimalField(max_value=1000, min_value=0, decimal_places=1, required=False)
	fuel_usage_out = forms.DecimalField(max_value=1000, min_value=0, decimal_places=1, required=False)
	fuel_usage_average = forms.DecimalField(max_value=1000, min_value=0, decimal_places=1, required=False)
	mileage_km = forms.IntegerField(min_value=0, required=False)
	transmission = forms.ChoiceField(choices=TRANSMISSION_TYPE, required=False)
	drive = forms.ChoiceField(choices=DRIVE_TYPE, required=False)
	doors = forms.IntegerField(min_value=0, max_value=20, required=False)
	seats = forms.IntegerField(min_value=0, max_value=100, required=False)
	equipment = forms.TextInput()
	steeringwheel = forms.ChoiceField(choices=STEERINGWHEEL_POSITION)
	location = forms.TextInput()
	country_of_origin = forms.ChoiceField(choices=COUNTRY_OF_ORIGIN_LIST, required=False, initial="-")
	is_import = forms.BooleanField(required=False, initial=False)
	date_of_import = forms.DateField(required=False, widget=forms.TextInput(attrs={
		"placeholder": 'DD-MM-YYYY'
		}))
	nr_owner = forms.IntegerField(min_value=0, max_value=10, required=False, initial=1)
	customisation = forms.BooleanField(required=False, initial=False)
	customisation_desc = forms.TextInput()
	vin_code = forms.TextInput()
	numberplate = forms.TextInput()
	optical_condition = forms.ChoiceField(choices=O_CONDITION_LIST, required=False)
	technical_condition = forms.ChoiceField(choices=T_CONDITION_LIST, required=False)
	interior_condition = forms.ChoiceField(choices=I_CONDITION_LIST, required=False)
	last_service_date = forms.DateField(required=False, widget=forms.TextInput(attrs={
		"placeholder": 'DD-MM-YYYY'
		}))
	last_service_desc = forms.TextInput()
	vehicle_desc = forms.TextInput()
	ad_type = forms.ChoiceField(choices=AD_TYPE_LIST)
	class Meta:
		model = Vehicle
		fields = [
			'pictures',
			'vehicle_type',
			'price',
			'value_added_tax',
			'new_used',
			'warranty_until',
			'insurance_until',
			'valid_mot_until',
			'service_history_bk',
			'accident',
			'damaged',
			'vehicle_model_year',
			'brand',
			'vehicle_model',
			'vehicle_model_other',
			'body_type',
			'power_kw',
			'displacement_cm',
			'cylinders',
			'fuel',
			'fuel_tank_l',
			'fuel_usage_city',
			'fuel_usage_out',
			'fuel_usage_average',
			'mileage_km',
			'transmission',
			'drive',
			'doors',
			'seats',
			'equipment',
			'steeringwheel',
			'location',
			'country_of_origin',
			'date_of_import',
			'is_import',
			'nr_owner',
			'customisation',
			'customisation_desc',
			'vin_code',
			'numberplate',
			'optical_condition',
			'technical_condition',
			'interior_condition',
			'last_service_date',
			'last_service_desc',
			'vehicle_desc',
			'ad_type'
		]



class ActiveVehicleForm(forms.ModelForm):
	class Meta:
		model = Vehicle
		fields = [
		'active'
		]