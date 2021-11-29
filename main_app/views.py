from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient
from .forms import VitalsForm


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
  vitals_form = VitalsForm()
  return render(request, 'patients/detail.html', {
    'patient': patient, 'vitals_form': vitals_form
    })

class PatientCreate(CreateView):
  model = Patient
  fields = '__all__'
  success_url ='/patients/'
  
class PatientUpdate(UpdateView):
  model = Patient
  fields = ['date','gender','phone']
  success_url = '/patients/'
  
class PatientDelete(DeleteView):
  model = Patient
  success_url = '/patients/'

def add_vitals(request, patient_id):
    form = VitalsForm(request.POST)
    if form.is_valid():
        new_vitals = form.save(commit=False)
        new_vitals.patient_id = patient_id
        new_vitals.save()
        return redirect('patients_detail', patient_id=patient_id)