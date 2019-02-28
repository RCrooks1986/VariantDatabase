from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import Variant

# Create your views here.
def index(request):
        return render(request, 'welcome.html')



def search(request):
    if request.method=="POST":
        form = Variant(request.POST)
        if form.is_valid():
            input_gene = form.cleaned_data['gene_name']
            input_cdna = form.cleaned_data['cdna_position']
            input_genomic = form.cleaned_data['genomic_position']

            # variant_data = Variant.objects.filter(field_in_db_filtering_on = input_text)
            # pass this within context to the rendered html
            # if multiple records, iterate over within template

        return render(request, 'search.html', {'form': form}) # changed starter to index
    else:
        form = Variant()
        return render(request, 'search.html', {'form': form})

def edit(request):
    form = Variant()
    return render(request, 'edit.html', {'form': form})

def add(request):
    form=Variant()
    return render(request, 'add.html', {'form': form})