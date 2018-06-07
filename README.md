# RandomProbeDesign
Design a oligo that is unique enough for c.elegans and yeast for smFISH experiment

## Install Blast+ by following the NCBI guideline: https://www.ncbi.nlm.nih.gov/books/NBK279671/

run make_query.py file to make 1000000 random 30bp sequences 

run ProbeDesign_local.py to blast random sequences against c.elegans transcriptome and yeast transcriptome

run changefilter.py to change the selection parameter qcover and output new filtered file

## To make new database for blast, refer to: https://www.ncbi.nlm.nih.gov/books/NBK279688/

### use 'blastn -help' to see available functions
