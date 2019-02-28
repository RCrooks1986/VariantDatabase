from django.db import models
from django.utils import timezone


class Patient(models.Model):
    PatientID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    Age = models.IntegerField()
    Proband = models.CharField(max_length=1)
    Relatives = models.CharField(max_length=1)
    Stage = models.IntegerField()
    Description = models.CharField(max_length=20)

    def __str__(self):

        return self.PatientID


class Variant(models.Model):
    VariantID = models.AutoField(primary_key=True)
    Gene = models.CharField(max_length = 20)
    cDNA = models.CharField(max_length = 50)
    Protein = models.CharField(max_length=50)
    Genome = models.CharField(max_length=50)

    def __str__(self):

        return self.VariantID

class Patient_Variant(models.Model):
    ObservationID = models.AutoField(primary_key=True)
    PatientID = models.IntegerField()
    VariantID = models.IntegerField()
    Sequencer = models.CharField(max_length=50)
    Pathogenicity = models.IntegerField()
    DateObserved = models.DateTimeField(default=timezone.now)

class Evidence(models.Model):
    EvidenceID = models.AutoField(primary_key=True)
    VariantID = models.IntegerField()
    EvidenceCode = models.CharField(max_length=4)
    DateAssigned = models.DateTimeField(default=timezone.now)
    DateRetired = models.DateTimeField(blank=True, null=True)
