from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import VariantForm, ImportCSV
from .models import Variant
import csv

# Create your views here.
def index(request):
        return render(request, 'welcome.html')



def search_variant(request):
    if request.method=="POST":
        form = VariantForm(request.POST)
        if form.is_valid():
            input_gene = form.cleaned_data['gene_name']
            input_cdna = form.cleaned_data['cdna_position']
            input_genomic = form.cleaned_data['genomic_position']
            print(input_gene)

            variant_data = Variant.objects.all() #filter(field_in_db_filtering_on = input_gene)
            # pass this within context to the rendered html
            # if multiple records, iterate over within template

        return render(request, 'view.html', {'variant_data': variant_data})
    else:
        form = VariantForm()
        return render(request, 'search.html', {'form': form})

def edit_variant(request):
    form = VariantForm()
    return render(request, 'edit.html', {'form': form})

def add_variant(request):
    form=VariantForm()
    return render(request, 'add.html', {'form': form})

def upload_file(request):
    if request.method=="POST":
        form = ImportCSV(request.POST, request.FILES)
        if form.is_valid():
            file_contents = request.FILES['upfile'].read().decode('UTF-8')
            lines = file_contents.split('\n')
            for line in lines:
                line = line.rstrip()
                field = line.split('\t')
                print("##", field[0])

                first_name = field[0].split(' ')[0]
                surname = field[0].split(' ')[1]
                age = field[1]
                proband = field[2]
                affected_relatives = field[3]
                stage = field[4]
                description = field[5]
                sequencer = field[6]
                cnda = field[7]
                protein = field[8]
                genome = field[9]
                pathogenicity = field[11]
                evidence_codes = field[12]

        return HttpResponse("File upload page")
    if request.method=="GET":
        form=ImportCSV()
        return render(request, 'upload.html', {'form': form})

