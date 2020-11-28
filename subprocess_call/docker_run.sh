#!/bin/sh
cd C:/Users/Dibs/Desktop/FullStackTestProject

docker run --rm -v C:/Users/Dibs/Desktop/FullStackTestProject/genome:/blast/genome:ro -v C:/Users/Dibs/Desktop/FullStackTestProject/queries:/blast/queries:ro -v C:/Users/Dibs/Desktop/FullStackTestProject/results:/blast/results:rw ncbi/blast blastn -query /blast/queries/ecoli_k12_mg1655.fasta -subject /blast/genome/ecoli_k12_mg1655.fasta -out /blast/results/shell.outfmt6 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"
