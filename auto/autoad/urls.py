from django.urls import path
from autoad.views import (
    VehicleListView,
    VehicleDetailView,
    VehicleCreateView,
    VehicleUpdateView,
    VehicleDeleteView
)

app_name = 'autoad'
urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle-list'),
    path('<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('create/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('<int:pk>/edit/', VehicleUpdateView.as_view(), name='vehicle-edit'),
    path('<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle-delete'),
]
