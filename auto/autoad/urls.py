from django.urls import path
from autoad.views import (
    VehicleListView,
    VehicleDetailView,
    VehicleCreateView,
    VehicleUpdateView,
    VehicleDeleteView,
    VehicleChangeActiveView
)

app_name = 'autoad'
urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle-list'),
    path('<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('create/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('<int:pk>/active/', VehicleChangeActiveView.as_view(), name='vehicle-active'),
    path('<int:pk>/edit/', VehicleUpdateView.as_view(), name='vehicle-edit'),
    path('<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle-delete'),
]
