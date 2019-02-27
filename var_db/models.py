from django.db import models
from django.utils import timezone


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    proband = models.BooleanField()
    affected = models.BooleanField()
    relatives = models.BooleanField()
    stage = models.IntegerField()
    description = models.CharField(max_length=20)
    patient_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (self.patient_id)


class Variant(models.Model):
    sequencer = models.CharField(max_length=15)
    variant_cnda = models.CharField(max_length = 50)
    variant_protein = models.CharField(max_length=50)
    variant_genome = models.CharField(max_length=50)
    variant_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (self.variant_id)

class Patient_Variant(models.Model):
    patient = models.IntegerField()
    variant = models.IntegerField()
    date_created = models.DateTimeField(default = timezone.now)
    classification = models.IntegerField()