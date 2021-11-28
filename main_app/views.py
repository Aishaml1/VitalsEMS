from django.shortcuts import render
from .models import Patient
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def patients_index(request):
    patients = Patient.objects.all()
    return render(request, 'patients/index.html', { 'patients': patients })

def patients_detail(request, patient_id):
  patient = Patient.objects.get(id=patient_id)
  return render(request, 'patients/detail.html', { 'patient': patient })
