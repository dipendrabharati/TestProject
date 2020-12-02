from django.shortcuts import render
from .models import BlastJob, BlastResult
from .utils import create_query_fasta, extract_sequence
import os.path
import subprocess


def home(request):
    return render(request, 'main.html')


# def results(request):
#    return render(request, 'results.html')


def run_blast(request):
    dna_sequence = request.POST.get('dna')
    s = BlastJob(query=dna_sequence)
    s.save()
    # create_query_fasta('./queries/python.fasta', dna_sequence)
    # ecoli_seq = extract_sequence()
    # subprocess.call('/home/ubuntu/TestProject/subprocess_call/docker_run.sh')
    with open('/home/ubuntu/TestProject/results/sh_aws.out', 'r') as a_file:
        i = 0
        for line in a_file:
            x = line.split()
            q = BlastResult(id=None, blast_job=s, result_no=i,
                            sstart=x[0], send=x[1], sstrand=x[2], evalue=x[3], pident=x[4], sequence=x[5])
            q.save()
            i += 1
    return render(request, 'results.html', {'dna_sequence': dna_sequence, 'q': q})


