from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient
from .forms import VitalsForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.


class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def patients_index(request):
    patients = request.user.patient_set.all()
    return render(request, 'patients/index.html', { 'patients': patients })

def patients_detail(request, patient_id):
  patient = Patient.objects.get(id=patient_id)
  vitals_form = VitalsForm()
  return render(request, 'patients/detail.html', {
    'patient': patient, 'vitals_form': vitals_form
    })

class PatientCreate(LoginRequiredMixin, CreateView):
  model = Patient
  fields = ['first', 'last', 'date', 'gender', 'phone']
  success_url ='/patients/'
   
  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
 
  
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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patients_index')
        else:
            error_message = 'Invalid sign up - try again'
            form = UserCreationForm()
            context = {'form': form, 'error_message': error_message}
            return render(request, 'signup.html', context)