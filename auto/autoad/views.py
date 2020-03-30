from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from django.forms import modelformset_factory
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
import datetime, random, string, os
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError

from .forms import VehicleForm, ActiveVehicleForm

from .models import Vehicle

from .filters import VehicleFilter

from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)


# Create your views here.
class VehicleListView(ListView):
	template_name = 'autoad/vehicle_list.html'
	model = Vehicle
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = VehicleFilter(self.request.GET, queryset=self.get_queryset())
		return context

class VehicleDetailView(DetailView):
	template_name = 'autoad/vehicle_detail.html'
	queryset = Vehicle.objects.all()



class VehicleCreateView(View):
	template_name = 'autoad/vehicle_create.html'
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated == False:
			print('Not logged in')
			return redirect('../')
		form = VehicleForm()
		context = {
			'form': form
		}
		return render(request, self.template_name, context)
	def post(self, request, *args, **kwargs):
		form = VehicleForm(request.POST, request.FILES)
		if form.is_valid():
			uploaded_files = request.FILES.getlist('pictures')
			images_array = []
			random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
			dt = datetime.datetime.today()
			if dt.month < 10:
				dt_path = str(dt.day) + "_0" + str(dt.month) + "_" + str(dt.year)
			else:
				dt_path = str(dt.day) + "_" + str(dt.month) + "_" + str(dt.year)
			fs = FileSystemStorage("media/"+ dt_path + "/" + random_char + "/")
			for f in uploaded_files:
				print(f.name[-3:])
				if f.size > 5242880:
					raise ValidationError(f.name + ': File size cannot larger than 5mb.')
				if (f.name[-3:] != "jpg") and (f.name[-3:] !="png") and (f.name[-3:] != "gif"):
						raise ValidationError(f.name + ': File format nor allowed.')
				
				name = fs.save(random_char + f.name, f)
				path = "/media/" + dt_path + "/"+random_char+"/"+name
				images_array.append(path)
			if len(images_array) > 15:
				raise ValidationError('Upload a maximum of 15 files.')
			vehicle_type = form.cleaned_data['vehicle_type']
			new_used = form.cleaned_data['new_used']
			price = form.cleaned_data['price']
			value_added_tax = form.cleaned_data['value_added_tax']
			warranty_until = form.cleaned_data['warranty_until']
			insurance_until = form.cleaned_data['insurance_until']
			valid_mot_until = form.cleaned_data['valid_mot_until']
			service_history_bk = form.cleaned_data['service_history_bk']
			accident = form.cleaned_data['accident']
			damaged = form.cleaned_data['damaged']
			vehicle_model_year = form.cleaned_data['vehicle_model_year']
			brand = form.cleaned_data['brand']
			vehicle_model = form.cleaned_data['vehicle_model'] 
			vehicle_model_other = form.cleaned_data['vehicle_model_other']
			body_type = form.cleaned_data['body_type']
			power_kw = form.cleaned_data['power_kw']
			displacement_cm = form.cleaned_data['displacement_cm']
			cylinders = form.cleaned_data['cylinders']
			fuel = form.cleaned_data['fuel']
			fuel_tank_l = form.cleaned_data['fuel_tank_l']
			fuel_usage_city = form.cleaned_data['fuel_usage_city']
			fuel_usage_out = form.cleaned_data['fuel_usage_out']
			fuel_usage_average = form.cleaned_data['fuel_usage_average']
			mileage_km = form.cleaned_data['mileage_km']
			transmission = form.cleaned_data['transmission']
			drive = form.cleaned_data['drive']
			doors = form.cleaned_data['doors']
			seats = form.cleaned_data['seats']
			equipment = form.cleaned_data['equipment']
			steeringwheel = form.cleaned_data['steeringwheel']
			location = form.cleaned_data['location']
			country_of_origin = form.cleaned_data['country_of_origin']
			is_import = form.cleaned_data['is_import']
			date_of_import = form.cleaned_data['date_of_import']
			nr_owner = form.cleaned_data['nr_owner']
			customisation = form.cleaned_data['customisation']
			customisation_desc = form.cleaned_data['customisation_desc']
			vin_code = form.cleaned_data['vin_code']
			numberplate = form.cleaned_data['numberplate']
			optical_condition = form.cleaned_data['optical_condition']
			technical_condition = form.cleaned_data['technical_condition']
			interior_condition = form.cleaned_data['interior_condition']
			last_service_date = form.cleaned_data['last_service_date']
			last_service_desc = form.cleaned_data['last_service_desc']
			vehicle_desc = form.cleaned_data['vehicle_desc']
			ad_type = form.cleaned_data['ad_type']
			new_vehicle = Vehicle(user=request.user, pictures=images_array, vehicle_type=vehicle_type, new_used=new_used, price=price, value_added_tax=value_added_tax, warranty_until=warranty_until,
				insurance_until=insurance_until, valid_mot_until=valid_mot_until, service_history_bk=service_history_bk, accident=accident,
				damaged=damaged, vehicle_model_year=vehicle_model_year, brand=brand, vehicle_model=vehicle_model, vehicle_model_other=vehicle_model_other,
				body_type=body_type, power_kw=power_kw, displacement_cm=displacement_cm, cylinders=cylinders, fuel=fuel, fuel_tank_l=fuel_tank_l,
				fuel_usage_city=fuel_usage_city, fuel_usage_out=fuel_usage_out, fuel_usage_average=fuel_usage_average, mileage_km=mileage_km,
				transmission=transmission, drive=drive, doors=doors, seats=seats, equipment=equipment, steeringwheel=steeringwheel, location=location,
				country_of_origin=country_of_origin, is_import=is_import, date_of_import=date_of_import, nr_owner=nr_owner, customisation=customisation,
				customisation_desc=customisation_desc, vin_code=vin_code, numberplate=numberplate, optical_condition=optical_condition, technical_condition=technical_condition,
				interior_condition=interior_condition, last_service_date=last_service_date, last_service_desc=last_service_desc, vehicle_desc=vehicle_desc,
				ad_type=ad_type
			)
			new_vehicle.save()
			return HttpResponseRedirect('../')
		else:
			return HttpResponseRedirect('Form not valid.')
		form = VehicleForm()
		context = {
			'form': form
		}
		return render(request, self.template_name, context)


class VehicleUpdateView(UpdateView):
	template_name = 'autoad/vehicle_edit.html'
	form_class = VehicleForm
	queryset = Vehicle.objects.all()

	'''def get_object(self):
		id_ = self.kwargs.get('pk')
		return get_object_or_404(vehicle, id=id_)'''
	def form_valid(self, form):
		if self.request.user == self.object.user:
			return super().form_valid(form)
		return HttpResponseRedirect('You are not allowed to edit this vehicle.')

class VehicleChangeActiveView(UpdateView):
	template_name = 'autoad/vehicle_active.html'
	form_class = ActiveVehicleForm
	queryset = Vehicle.objects.all()

	'''def get_object(self):
		id_ = self.kwargs.get('pk')
		return get_object_or_404(vehicle, id=id_)'''
	def form_valid(self, form):
		if self.request.user == self.object.user:
			return super().form_valid(form)
		return HttpResponseRedirect('You are not allowed to edit this vehicle.')

class VehicleDeleteView(DeleteView):
	template_name = 'autoad/vehicle_delete.html'
	queryset = Vehicle.objects.all()
	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		if self.object.user == request.user:
			self.object.delete()
			return HttpResponseRedirect(self.get_success_url())
		else:
			raise Http404
	def get_success_url(self):
		return reverse('autoad:vehicle-list')

