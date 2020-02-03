import sys, os, re, platform
import pandas as pd
import numpy as np

with open('/Users/shixinjin/Desktop/CNN/Lys/Supp-4-negative.fasta') as positive:
    records=positive.read()

AAindex=pd.read_csv('/Users/shixinjin/Desktop/AAidx.csv',index_col=0,header=0)

records=records.split('>')[1:]
myFasta=[]
namelist=[]
for fasta in records:
    array=fasta.split('\n')
    name=array[0].split()[0]
    sequence=''.join(array[1:])
    myFasta.append([name,sequence])
    namelist.append(name)

result=[]
for aa in myFasta:
    singalfasta=aa[1]
    for singalaa in singalfasta:
        aa[0]=AAindex[singalaa]
        result.append(aa[0])
result=pd.DataFrame(result)

indexsum=0
for i in range(len(myFasta)):
    locals()[namelist[i]]=(result[indexsum:indexsum+len(myFasta[i][1])]).T
    indexsum+=len(myFasta[i][1])
    locals()[namelist[i]].to_csv('/Users/shixinjin/Desktop/CNN/Lys/negative/%s.csv' %namelist[i])