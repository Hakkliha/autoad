from django.shortcuts import render
from django.views.generic.base import View

from .forms import VehicleModelForm


# Create your views here.
class ModelChoiceView(View):
    template_name = 'vehicle_models.html'

    def get(self, request, *args, **kwargs):
        form = VehicleModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = VehicleModelForm(request.POST)
        if form.is_valid():
            buy_sell = form.cleaned_data['buy_sell']
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            submodel = form.cleaned_data['submodel']
