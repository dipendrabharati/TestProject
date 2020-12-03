from django.shortcuts import render
from .models import BlastJob, BlastResult
from .utils import create_query_fasta, extract_sequence
import os.path
import subprocess


def home(request):
    return render(request, 'main.html')


def run_blast(request):
    dna_sequence = request.POST.get('dna')
    s = BlastJob(query=dna_sequence)
    s.save()
    query_file = './queries/python.fasta'
    # if os.path.isfile(query_file):
    #    os.remove(query_file)
    # else:
    #    create_query_fasta(query_file, dna_sequence)
    # ecoli_seq = extract_sequence()
    out_file = '/home/ubuntu/TestProject/results/sh_aws.out'

    if os.path.isfile(out_file):
        os.remove(out_file)
    p1 = subprocess.Popen(['/bin/bash', '/home/ubuntu/TestProject/subprocess_call/docker_run.sh'],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p1.stdout:
        try:
            with open('/home/ubuntu/TestProject/results/sh_aws.out', 'r') as a_file:
                i = 1
                new_list = []
                for line in a_file:
                    x = line.split()
                    q = BlastResult(id=None, blast_job=s, result_no=i,
                                    sstart=x[0], send=x[1], sstrand=x[2], evalue=x[3], pident=x[4], sequence=x[5])
                    q.save()
                    new_list.append(q)
                    i += 1
                a_file.close()
            return render(request, 'results.html', {'dna_sequence': dna_sequence, 'new_list': new_list})
        except IOError:
            no_result = " Sorry, The Blast Search was successful but the system cannot display the output"
            return render(request, 'no_results.html', {'no_result': no_result})
    elif p1.stderr:
        no_result = " Sorry, The Blast Search couldn't be completed. "
        return render(request, 'no_results.html', {'no_result': no_result})
