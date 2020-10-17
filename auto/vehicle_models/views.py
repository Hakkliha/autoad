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
