from django.db import models

# Create your models here.
class Evidence(models.Model):
    VariantID = models.IntegerField()
    EvidenceCode = models.CharField(max_length=4)
    DateAssigned = model.DateTimeField(default = timezone.now)
    DateRetired = model.DateTimeField(blank = True, null = True)