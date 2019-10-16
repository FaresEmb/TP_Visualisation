from zipfile import ZipFile
import pandas as pd


list_files = []

# Load brut.zip


with ZipFile('data/brut.zip', 'r') as zipObj:
   listOfiles = zipObj.namelist()
   for elem in listOfiles:
       if elem != 'brut/':
        list_files.append(elem)

zf = ZipFile('data/brut.zip')
df = pd.read_csv(zf.open(list_files[0]))

print(df.head)


