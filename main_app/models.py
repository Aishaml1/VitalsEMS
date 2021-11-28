from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
GENDERS = (
    ('Z', 'Prefer Not to Say'),
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
    