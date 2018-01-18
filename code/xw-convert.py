import pandas as pd
import os



files_dict = {
    'Carrier': 'carrierxw.txt',
    'Inpatient': 'ipxw.txt',
    'MedPAR': 'medparxw.txt',
    'Outpatient': 'opxw.txt'}

for name, txtpath in files_dict.items():
    print(key)
    print(val)

name = 'Carrier'
txtpath = 'carrierxw.txt'

name = 'Outpatient'
txtpath = 'opxw.txt'

path = os.path.join('..', 'data', 'nber', 'claim_xw', txtpath)
df = pd.read_table(path)


df.fillna('').stack()
df2 = df.stack()

fnalvar              bene_id
key                  bene_id
label         beneficiary id
2006                 bene_id
2007                 bene_id
2008                 bene_id
2009                 bene_id
2010                 bene_id
2011                 bene_id
2012                 bene_id
2013                 bene_id
lengthvar                 15
character                  1
filevarind              both
generated                  0

df2[0]

df.stack()







