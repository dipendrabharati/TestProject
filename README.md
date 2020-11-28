# Full Stack position test project

A tiny project with a basic coding exercise. The project includes writing a simple web service using django on sqlite.
The web page will allow the user to run a blast search of a single sequence on a given bacterial genome (in the data folder).
Blast must run using docker!

## Requirements

The following tools are required to complete the task

1) python3 with the following requrements:
```
django
biopython
```
You may add packages as needed. Add a requirements.txt file including everything you use.
2) docker

## Tasks

1) Clone the project into a directory
2) Create a virtual environment and install neccesery dependecies (`python3 -m venv venv`)
3) Create a webpage that allows the user to enter a single DNA sequence containing only the letter A,G,C and T to a form. Web pages should be designed using bootstrap 4.
4) Use the BlastJob model (models.py) to create the job and run a search task (use the blast command from the Tools section). The search should run in an asynchronous manner (the page should not wait for the search to finish). <b>The results page should not fully refresh to check the status (js based solution)!</b>
5) A web page should present the job's results when the job if finished

Dont forget to run `python3 manage.py makemigrations blast_test` and `python3 manage.py migrate` before running the server

## Tools

Running blast should be done using the `ncbi/blast` image found in ducker hub.
The internal blast command:
`blastn -query <query_file> -subject genome/ecoli_k12_mg1655.fasta -outfmt "6 <required parameters based on BlastResult model>"`

You can read about the tabular format output 6 [here](http://www.metagenomics.wiki/tools/blast/blastn-output-format-6)
Note: sequence can be extracted using a function in utils.py

