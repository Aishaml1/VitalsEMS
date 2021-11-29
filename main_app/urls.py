from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path ('about/', views.about, name='about'),
    path('patients/', views.patients_index, name='patients_index'),
    path('patients/<int:patient_id>/', views.patients_detail, name='patients_detail'),
    path('patients/create/', views.PatientCreate.as_view(), name='patients_create'),
    path('patients/<int:pk>/update/', views.PatientUpdate.as_view(), name='patients_update'),
    path('patients/<int:pk>/delete/', views.PatientDelete.as_view(), name='patients_delete'),
    path('patients/<int:patient_id>/add_vitals/', views.add_vitals, name='add_vitals'),
    
]