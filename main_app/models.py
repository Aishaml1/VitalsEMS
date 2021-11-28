from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.urls import reverse
# Create your models here.
GENDERS = (
    (' ', 'Prefer Not to Say'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('X', 'X'),
)
class Patient(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    date = models.DateField('Date of Birth')
    gender = models.CharField(
        max_length=1,
		choices=GENDERS,
		default=GENDERS[0][0]
    )
    phone = PhoneNumberField()

def __str__(self):
    return self.name
    
def get_absolute_url(self):
    return reverse('patients_detail', kwargs={'patient_id': self.id})