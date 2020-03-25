from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

from .forms import VehicleForm

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


class VehicleCreateView(CreateView):
	template_name = 'autoad/vehicle_create.html'
	form_class = VehicleForm
	queryset = Vehicle.objects.all()

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class VehicleUpdateView(UpdateView):
	template_name = 'autoad/vehicle_create.html'
	form_class = VehicleForm
	queryset = Vehicle.objects.all()

	'''def get_object(self):
		id_ = self.kwargs.get('pk')
		return get_object_or_404(vehicle, id=id_)'''

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class VehicleDeleteView(DeleteView):
	template_name = 'autoad/vehicle_delete.html'
	queryset = Vehicle.objects.all()

	def get_success_url(self):
		return reverse('autoad:vehicle-list')