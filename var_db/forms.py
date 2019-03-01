from django import forms
from django.forms import ModelForm
from var_db.models import VariantData

class VariantForm(forms.Form):
    cdna_position = forms.CharField(max_length=50, required=False, label="cDNA position")
    genomic_position = forms.CharField(max_length=50, required=False, label="Genomic position")

class PatientForm(forms.Form):
    name = forms.CharField(max_length=50, required=False, label='Patient Name')
    age = forms.IntegerField(required=False, label="Patient Age")
    proband = forms.CharField(max_length=1, required=False, label="Proband")
    affected_relatives = forms.CharField(max_length=1, required=False, label="Affected Relatives")
    stage = forms.IntegerField(required=False, label="Stage")
    description = forms.CharField(max_length=50, required=False, label="Stage")

class ImportCSV(forms.Form):
    upfile = forms.FileField(label = "Choose a file")

class VariantDataForm(ModelForm):
    class Meta:
        model = VariantData
        fields = ['cnda', 'protein', 'genome', 'pathogenicity', 'evidence_codes', 'name',
                  'age', 'proband', 'affected_relatives', 'description', 'stage', 'sequencer']
