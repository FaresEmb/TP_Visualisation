from zipfile import ZipFile
import pandas as pd

def get_files_list(zipfile = 'data/brut.zip'):
    with ZipFile(zipfile, 'r') as zipObj:
        listOfiles = zipObj.namelist()
        list_files = []
        for elem in listOfiles:
            if elem != 'brut/':
                list_files.append(elem)
    return list_files

def read_csv_from_zip(filename = None,zip_file='data/brut.zip'):
    if filename == None:
        list_files = get_files_list()
        filename = list_files[0]
    zf = ZipFile(zip_file)
    return pd.read_csv(zf.open(filename))

#filename = get_files_list()[0]
#df = read_csv_from_zip(filename=filename)
#print(df.head)

print('......__ loading load_data module __ ......')