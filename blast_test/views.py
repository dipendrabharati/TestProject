from django.shortcuts import render
from .models import BlastJob, BlastResult
from .utils import create_query_fasta, extract_sequence
import os.path


def home(request):
    return render(request, 'main.html')


def results(request):
    return render(request, 'results.html')


def run_blast(request):
    dna_sequence = request.POST.get('dna')
    s = BlastJob(query=dna_sequence)
    s.save()
    create_query_fasta('./queries/python.fasta', dna_sequence)
    # ecoli_seq = extract_sequence()
    return render(request, 'results.html', {'dna_sequence': dna_sequence})

