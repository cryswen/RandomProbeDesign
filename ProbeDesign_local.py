import os
import pandas as pd


print('Blasting qurey sequences against c.elegans W265 transcriptome...')

command = 'blastn -query query.fa -db /Users/wenxu/blastdb/c_elegans.PRJNA13758.WS265.mRNA_transcripts.fa -task blastn -evalue 1000 -dust no -outfmt "10 qseqid sseqid qcovs pident" -max_target_seqs 100 >> elegans_blast.csv'

os.system(command)

print('Blasting qurey sequences against yeast S288C transcriptome...')

command = 'blastn -query query.fa -db /Users/wenxu/blastdb/yeast_S288C_rna_genomic_1000.fasta -task blastn -evalue 1000 -dust no -outfmt "10 qseqid sseqid qcovs pident" -max_target_seqs 100 >> yeast_blast.csv'

os.system(command)


query = pd.read_csv('query.csv',header=0)
query.columns = ['id','sequence']

elegans_blast = pd.read_csv('elegans_blast.csv',header=0)
yeast_blast = pd.read_csv('yeast_blast.csv',header=0)

elegans_blast.columns = ['id','seqid','qcoverage','pident']
max_qs1 = elegans_blast.groupby(elegans_blast['id'], as_index=False)['qcoverage'].max()
max_qs1.to_csv('elegans_blast_summary.csv')

yeast_blast.columns = ['id','seqid','qcoverage','pident']
max_qs2 = yeast_blast.groupby(yeast_blast['id'], as_index=False)['qcoverage'].max()
max_qs2.to_csv('yeast_blast_summary.csv')

max_qs = pd.merge(max_qs1,max_qs2, on='id')
max_qs.columns = ['id', 'elegans_q','yeast_q']
max_qs.to_csv('blast_summary.csv')

print('Filtering blast results based on query coverage less than 50%...')

filtered = max_qs[(max_qs['elegans_q']<=50)&(max_qs['yeast_q']<=50)]

blast_results = filtered.merge(query, on='id', how = 'left')
blast_results.to_csv('filtered_results.csv')

print('All done! Enjoy your results!!!')

