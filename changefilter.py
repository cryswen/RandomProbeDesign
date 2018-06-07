import pandas as pd

max_qs = pd.read_csv('blast_summary.csv')

filtered = max_qs[(max_qs['elegans_q']<=40)&(max_qs['yeast_q']<=40)]

blast_results = filtered.merge(query, on='id', how = 'left')
blast_results.to_csv('blast_results_40.csv')
