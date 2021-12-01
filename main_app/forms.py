from django.forms import ModelForm
from django import forms
from .models import STATUS, Vitals, Patient

class VitalsForm(forms.ModelForm):
    status = forms.ChoiceField(label='Status:', choices=STATUS,
                            widget=forms.RadioSelect
                            (attrs={'class':'status',
                                    'id':'status-radio'}))
    class Meta:
        model = Vitals
        fields = [
            'vitals_date',
            'respiration',
            'pulse',
            'systolic',
            'diastolic',
            'gcs',
            'pupils',
            'skin',
            'consciousness',
            'status'
        ]
        