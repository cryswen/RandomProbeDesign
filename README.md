# RandomProbeDesign
Design a 30bp long oligo that is unique enough for c.elegans and yeast for smFISH experiment. This oligo will serve as the complimentary sequence for a dye-carrier probe to recognize.

## Probe screening through blast

Goal: select a random 30bp sequence that is relatively unique to c.elegans and yeast.

#### Install Blast+ by following the NCBI guideline: https://www.ncbi.nlm.nih.gov/books/NBK279671/

run make_query.py file to make 1000000 random 30bp sequences.

run ProbeDesign_local.py to blast random sequences against c.elegans transcriptome and yeast transcriptome.
#### This code ouputs the sequences with less or equal than 50% maximum query cover to elegans and yeast transcriptome.

run changefilter.py to change the selection parameter qcover and output new filtered file.

#### To make new database for blast, refer to: https://www.ncbi.nlm.nih.gov/books/NBK279688/

#### use 'blastn -help' to see available functions

## filtering through melting temperature
Goal: select a probe with melting temperature at 60-70dC (70dC preferred).
#### Select parameters
Adjust IDT parameters to:\\
  choose 'RNA'
  oligo 0.5
  Na+ 330
  Mg2+ 0

run idtAnalyzer.py to take the output of blasted sequence and calculate the melting temperature.

## filtering through mfold
Goal: check the structure of designed probe (87bp long), sequences provided by Gable. We want to find the ones have at least 7nt exposed of range 40-50, and at least 7nt exposed for sequence range 50-80 (according to Gable).

run mfold.py to get output pdf of the first outputed structure from mfold.

## combine all results and find the best desgin!!!!
