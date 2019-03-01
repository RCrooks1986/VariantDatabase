from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import VariantForm, ImportCSV, VariantDataForm
from .models import VariantData



import csv

# Create your views here.
def index(request):
        return render(request, 'welcome.html')


def search_variant(request):
    if request.method=="POST":
        form = VariantForm(request.POST)
        if form.is_valid():
            input_cdna = form.cleaned_data['cdna_position']
            input_genomic = form.cleaned_data['genomic_position']

            if not input_cdna and not input_genomic:
                variant_data = VariantData.objects.all()
            elif input_cdna:
                variant_data = VariantData.objects.filter(cnda=input_cdna)
            elif input_genomic:
                variant_data = VariantData.objects.filter(genome=input_genomic)
            else:
                variant_data = VariantData.objects.all()

        return render(request, 'view.html', {'variant_data': variant_data})
    else:
        form = VariantForm()
        return render(request, 'search.html', {'form': form})


def edit_variant(request, pk):
    variant_instance = VariantData.objects.filter(id=pk).first()
    form = VariantDataForm(instance=variant_instance)
    if request.method == "POST":
        form = VariantDataForm(request.POST, instance=variant_instance)
        if form.is_valid():
            form.save()

    return render(request, 'edit.html', {'form': form, 'pk': pk})

def add_variant(request):
    if request.method=="POST":
        form = VariantDataForm(request.POST)
        if form.is_valid():
            input_cdna = form.cleaned_data['cnda']
            input_protein = form.cleaned_data['protein']
            input_genomic = form.cleaned_data['genome']
            input_pathogenicity = form.cleaned_data['pathogenicity']
            input_evidence_codes = form.cleaned_data['evidence_codes']
            input_name = form.cleaned_data['name']
            input_age = form.cleaned_data['age']
            input_proband = form.cleaned_data['proband']
            input_stage = form.cleaned_data['stage']
            input_affected_relatives = form.cleaned_data['affected_relatives']
            input_description = form.cleaned_data['description']
            input_sequencer = form.cleaned_data['sequencer']

            data = VariantData(name=input_name, age=input_age, proband=input_proband,
                               affected_relatives=input_affected_relatives, stage=input_stage, description=input_description,
                               sequencer=input_sequencer, cnda=input_cdna, protein=input_protein, genome=input_genomic,
                               pathogenicity=input_pathogenicity, evidence_codes=input_evidence_codes)
            try:
                data.save()
                message = "Success! Variant added to database"
            except:
                message = "Fail! There has been a problem"

            form = VariantDataForm()

            return render(request, 'add.html', {'form': form, 'message': message})

    else:
        form = VariantDataForm()

        return render(request, 'add.html', {'form': form})


def upload_file(request):
    if request.method=="POST":
        form = ImportCSV(request.POST, request.FILES)
        if form.is_valid():
            file_contents = request.FILES['upfile'].read().decode('UTF-8')
            lines = file_contents.rstrip().split('\n')
            for i, line in enumerate(lines):
                if line.startswith("Name"):
                    pass
                else:
                    #print(i)
                    line = line.rstrip()
                    field = line.split('\t')

                    name = field[0]
                    age = field[1]
                    proband = field[2]
                    affected_relatives = field[3]
                    stage = field[4]
                    description = field[5]
                    sequencer = field[6]
                    cdna = field[7]
                    protein = field[8]
                    genome = field[9]
                    pathogenicity = field[11]
                    if len(field) == 13:
                        evidence_codes = field[12]
                    else:
                        evidence_codes = 'NA'


                    data = VariantData(name=name, age=age, proband=proband,
                                       affected_relatives=affected_relatives, stage=stage, description=description,
                                       sequencer=sequencer, cnda=cdna, protein=protein,genome=genome,
                                       pathogenicity=pathogenicity, evidence_codes=evidence_codes )
                    data.save()
        return HttpResponse("File upload page")
    if request.method=="GET":
        form=ImportCSV()
        return render(request, 'upload.html', {'form': form})

