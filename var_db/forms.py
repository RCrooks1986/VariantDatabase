from django import forms

class Variant(forms.Form):
    gene_name = forms.CharField(max_length=30, required=True, label="Gene")
    cdna_position = forms.CharField(max_length=50, required=False, label="cDNA position")
    genomic_position = forms.CharField(max_length=50, required=False, label="Genomic position")
    variant_id = forms.HiddenInput()
    created_date = forms.DateTimeField()