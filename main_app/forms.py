from django import forms, ModelForm
from models import Vitals

class VitalsForm(ModelForm):
    class Meta:
        model = Vitals
        fields = ['__all__']


# Class Vitals(forms.ModelForm):

# choice = Vitals(label=("Selected your choice"), choices=Vitals.SKIN)


# consciousness = forms.ChoiceField(
#         'Level Of Consciousness',
#         widget=forms.RadioSelect, choices=LOC
#         )
# pupils = forms.ChoiceField(
#         'Pupils',
#         widget=forms.RadioSelect, choices=PUPILS
#         )
# skin = forms.ChoiceField(
#         'Skin',
#         max_length=1,
#         choices=SKIN,
#         default=SKIN[0][0]
#     )
# status = forms.ChoiceField(
#         'Status',
#         widget=forms.RadioSelect, choices=STATUS
#         )