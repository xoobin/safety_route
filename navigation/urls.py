from django.urls import path
from . import views
from .views import streetlight_data

urlpatterns = [
    path('', views.map_view, name='map_view'),
    path('data/streetlight/', streetlight_data, name='streetlight_data'),
]



