from django.db import models
from django.utils import timezone




# class Patient(models.Model):
#     PatientID = models.IntegerField(null=True)
#     FirstName = models.CharField(max_length=100)
#     Surname = models.CharField(max_length=100, null=True)
#     Age = models.IntegerField()
#     Proband = models.CharField(max_length=1, default="?")
#     Relatives = models.CharField(max_length=1, default="?")
#     Stage = models.IntegerField()
#     Description = models.CharField(max_length=20)
#
#     def __str__(self):
#
#         return self.PatientID
#
# class Variant(models.Model):
#     VariantID = models.IntegerField(null=True)
#     Gene = models.CharField(max_length = 20)
#     cDNA = models.CharField(max_length = 50)
#     Protein = models.CharField(max_length=50)
#     Genome = models.CharField(max_length=50)
#
#     def __str__(self):
#
#         return self.VariantID
#
# class Patient_Variant(models.Model):
#     ObservationID = models.IntegerField(null=True)
#     PatientID = models.IntegerField()
#     VariantID = models.IntegerField()
#     Sequencer = models.CharField(max_length=50)
#     Pathogenicity = models.IntegerField()
#     DateObserved = models.DateTimeField(default=timezone.now)
#
# class Evidence(models.Model):
#     EvidenceID = models.IntegerField(null=True)
#     VariantID = models.IntegerField()
#     EvidenceCode = models.CharField(max_length=4)
#     DateAssigned = models.DateTimeField(default=timezone.now)
#     DateRetired = models.DateTimeField(blank=True, null=True)


class VariantData(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField()
    proband = models.CharField(max_length=20)
    affected_relatives = models.CharField(max_length=20)
    stage = models.IntegerField()
    description = models.CharField(max_length=50)
    sequencer = models.CharField(max_length=20)
    cnda = models.CharField(max_length=20)
    protein = models.CharField(max_length=20)
    genome = models.CharField(max_length=20)
    pathogenicity = models.IntegerField()
    evidence_codes = models.CharField(max_length=50)
