#!/bin/sh
cd ~/TestProject
sudo docker run --rm \
	 -v ~/TestProject/genome:/blast/genome:ro \
	 -v ~/TestProject/queries:/blast/queries:ro \
	 -v ~/TestProject/results:/blast/results:rw \
	 ncbi/blast \
	 blastn -query /blast/queries/ecoli_k12_mg1655.fasta -subject /blast/genome/ecoli_k12_mg1655.fasta \
        -out /blast/results/sh_aws.out -outfmt "6 sstart send sstrand evalue pident sseq" 
