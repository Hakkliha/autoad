from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from django.forms import modelformset_factory
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
import datetime, random, string, os
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
from django import forms
from .forms import VehicleForm, ActiveVehicleForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
		filtered_qs = VehicleFilter(self.request.GET, queryset=self.get_queryset())
		context['filter'] = filtered_qs
		paginator = Paginator(filtered_qs.qs, 10)
		page = self.request.GET.get('page')
		try:
			context['response'] = paginator.page(page)
		except PageNotAnInteger:
			context['response'] = paginator.page(1)
		except EmptyPage:
			context['response'] = paginator.page(paginator.num_pages)
		return context


class VehicleHomeView(ListView):
	template_name = 'autoad/vehicle_home.html'
	model = Vehicle
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = VehicleFilter(self.request.GET, queryset=self.get_queryset())
		return context

class VehicleDetailView(DetailView):
	template_name = 'autoad/vehicle_detail.html'
	queryset = Vehicle.objects.all()


class VehicleImagesView(DetailView):
	template_name = 'autoad/vehicle_images.html'
	queryset = Vehicle.objects.all()



class VehicleCreateView(View):
	template_name = 'autoad/vehicle_create.html'
	my_errors = []	


	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated == False:
			print('Not logged in')
			return redirect('../')
		form = VehicleForm()
		context = {
			'form': form,
			'my_errors': self.my_errors
		}
		return render(request, self.template_name, context)


	def post(self, request, *args, **kwargs):
		form = VehicleForm(request.POST, request.FILES)
		self.my_errors = []
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
				if f.size > 5242880:
					self.my_errors.append(f.name + ': File size cannot be larger than 5mb.')
				if (f.name[-3:] != "jpg") and (f.name[-3:] !="png") and (f.name[-3:] != "gif"):
					self.my_errors.append(f.name + ': File format nor allowed.')
				random_char1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
				random_char2 = ''.join(random.choices(string.digits, k=5))
				name = fs.save(random_char1 + str(int(str(f.size)[-3:]) * int(random_char2))[-4:]  + f.name, f)
				path = "/media/" + dt_path + "/"+random_char+"/"+name
				images_array.append(path)
			if len(images_array) > 15:
				self.my_errors.append('Upload a maximum of 15 images.')
			if images_array == []:
				self.my_errors.append('Images are required.')
			vehicle_type = form.cleaned_data['vehicle_type']
			new_used = form.cleaned_data['new_used']
			price = form.cleaned_data['price']
			reduced_price = form.cleaned_data['reduced_price']
			if reduced_price != None:
				if reduced_price > price:
					self.my_errors.append('The reduced price cannot be bigger than the regular price.')
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
				ad_type=ad_type, reduced_price=reduced_price
			)
			if self.my_errors:
				return render(request, self.template_name, {'form': form, 'my_errors': self.my_errors})
			else:	
				new_vehicle.save()
			return HttpResponseRedirect('/'+str(new_vehicle.id)+'/')
		else:
			return HttpResponseRedirect('Form not valid.')
		form = VehicleForm()
		context = {
			'form': form,
			'my_errors': self.my_errors
		}
		return render(request, self.template_name, context)


"""class VehicleUpdateView(UpdateView):
	template_name = 'autoad/vehicle_edit.html'
	form_class = VehicleForm
	queryset = Vehicle.objects.all()

	'''def get_object(self):
		id_ = self.kwargs.get('pk')
		return get_object_or_404(vehicle, id=id_)'''
	def form_valid(self, form):
		if self.request.user == self.object.user:
			return super().form_valid(form)
		return HttpResponseRedirect('You are not allowed to edit this vehicle.')"""


class VehicleUpdateView(View):
	template_name = "autoad/vehicle_edit.html"
	my_errors = []	

	def get_object(self):
		id = self.kwargs.get('pk')
		obj = None
		if id is not None:
			obj = get_object_or_404(Vehicle, id=id)
		return obj


	def get(self, request, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			if self.request.user == obj.user:
				form = VehicleForm(instance=obj)
				context['object'] = obj
				context['form'] = form
				context['my_errors'] = self.my_errors
		return render(request, self.template_name, context)
		

	def post(self, request, *args, **kwargs):
		context = {}
		self.my_errors = []
		obj = self.get_object()
		print(obj)
		if obj is not None:
			if self.request.user == obj.user:
				form = VehicleForm(request.POST, request.FILES, instance=obj)
				if form.is_valid():
					uploaded_files = request.FILES.getlist('pictures')
					images_source = request.POST.get('pictures_source')


					random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
					dt = datetime.datetime.today()
					if dt.month < 10:
						dt_path = str(dt.day) + "_0" + str(dt.month) + "_" + str(dt.year)
					else:
						dt_path = str(dt.day) + "_" + str(dt.month) + "_" + str(dt.year)

					
					images_array = images_source.replace('\'', '').replace('[', '').replace(']', '').replace(' ', '').split(',')
					print(images_array[0][1:28])

					if images_array == []:

						fs = FileSystemStorage("media/"+ dt_path + "/" + random_char + "/")
						for f in uploaded_files:
							print(f.name[-3:])
							if f.size > 5242880:
								self.my_errors.append(f.name + ': File size cannot be larger than 5mb.')
							if (f.name[-3:] != "jpg") and (f.name[-3:] !="png") and (f.name[-3:] != "gif"):
								self.my_errors.append(f.name + ': File format nor allowed.')
							
							name = fs.save(random_char + f.name, f)
							path = "/media/" + dt_path + "/"+random_char+"/"+name
							images_array.append(path)
					else:
						
						fs = FileSystemStorage(images_array[0][1:28])
						for f in uploaded_files:
							print(f.name[-3:])
							if f.size > 5242880:
								self.my_errors.append(f.name + ': File size cannot be larger than 5mb.')
							if (f.name[-3:] != "jpg") and (f.name[-3:] !="png") and (f.name[-3:] != "gif"):
								self.my_errors.append(f.name + ': File format nor allowed.')
							
							name = fs.save(images_array[0][17:27] + f.name, f)
							path = images_array[0][0:28] + name
							images_array.append(path)
					if len(images_array) > 15:
						self.my_errors.append('Upload a maximum of 15 images.')
					if images_array == []:
						self.my_errors.append('Images are required.')
					vehicle_type = form.cleaned_data['vehicle_type']
					new_used = form.cleaned_data['new_used']
					price = form.cleaned_data['price']
					reduced_price = form.cleaned_data['reduced_price']
					if reduced_price > price:
						self.my_errors.append('The reduced price cannot be bigger than or equal to the regular price.')
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
						ad_type=ad_type, id=obj.id, creation_datetime=obj.creation_datetime, reduced_price=reduced_price)
					if self.my_errors:
						return render(request, self.template_name, {'form': form, 'my_errors': self.my_errors, 'object': obj})
					else:
						new_vehicle.save()
					return HttpResponseRedirect('/'+str(obj.id)+'/')
				else:
					return HttpResponseRedirect('Form not valid.')
		context['object'] = obj
		context['form'] = VehicleForm(request.POST, request.FILES, instance=obj)
		context['my_errors'] = self.my_errors
		return render(request, self.template_name, context)





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

