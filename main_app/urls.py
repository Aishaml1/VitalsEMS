from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('about/', views.about, name='about'),
    path('patients/', views.patients_index, name='patients_index'),
]