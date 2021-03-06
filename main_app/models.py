from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
STATUS = [
    ('C', 'Critical'),
    ('U', 'Unstable'),
    ('P', 'Potentially Unstable'),
    ('S', 'Stable'),
]

SKIN = [
    ('unremarkable', 'Unremarkable'),
    ('cool', 'cool'),
    ('moist', 'Moist'),
    ('warm', 'Warm'),
    ('dry', 'dry'),
    ('pale', 'Pale'),
    ('cyanotic', 'Cyanotic'),
    ('flushed', 'Flushed'),
    ('juandiced', 'Juandiced'),
]

PUPILS = [
    ('normal', 'Normal'),
    ('dilated', 'Dilated'),
    ('Constricted', 'Constricted'),
    ('sluggish', 'sluggish'),
    ('no reaction', 'No Reaction'),
]

LOC = [
    ('alert', 'Alert'),
    ('voice', 'Voice'),
    ('pain', 'Pain'),
    ('unresponsive', 'Unresponsive'),
]

GENDERS = (
    (' ', 'Unknown'),
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
            return self.first

    def get_absolute_url(self):
        return reverse('patients_detail', kwargs={'patient_id': self.id})


class Vitals(models.Model):
    vitals_date = models.DateField('Date')
    respiration = models.IntegerField()
    pulse = models.IntegerField()
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    consciousness = models.CharField( 
        'Level Of Consciousness',
        max_length=20,
        choices=LOC,
        default=LOC[0][0]
    )
    gcs = models.IntegerField(
        'Glasgow Coma Scale', 
        default=15,
    )
    pupils = models.CharField( 
        'pupils',
        max_length=20,
        choices=PUPILS,
        default=PUPILS[0][0]
    )
    skin =  models.CharField( 
        'Skin',
        max_length=20,
        choices=SKIN,
        default=SKIN[0][0]
    )
    status =  models.CharField( 
        'Status',
        max_length=20,
        choices=STATUS,
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.status} on {self.vitals_date}"

    def vitals_for_today(self):
        return self.vitals_set.filter(vitals_date=date.today()).count()
