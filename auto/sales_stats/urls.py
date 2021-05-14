from django.urls import path

from .views import GenerateDataView, DataDisplayView

app_name = 'statics'
urlpatterns = [
    path('generator/', GenerateDataView.as_view(), name='statistics-generate'),
    path('', DataDisplayView.as_view(), name='statistics-display-view')
]
