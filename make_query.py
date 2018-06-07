import random

# make fasta file with queries
f = open('query.fa','w')
fcsv = open('query.csv','w')
j = 0
while j < 1000000:
    x = ''
    for i in range(30):
        x += random.choice('atgc')
    if x.count('g')+x.count('c') >= 12 and x.count('g')+x.count('c') <= 18:
        f.write('>random' + str(j) + '\n' + x +'\n')
        fcsv.write('random' + str(j) + ',' + x +'\n')
        j += 1
        if j%100000 == 0:
	        print(str(j) + ' random primers generated.')
f.close()
fcsv.close()