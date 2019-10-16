from zipfile import ZipFile
import pandas as pd

def get_files_list(zipfile = 'data/brut.zip'):
    with ZipFile(zipfile, 'r') as zip_obj:
        list_o_files = zip_obj.namelist()
        list_files = []
        for elem in list_o_files:
            if elem != 'brut/':
                list_files.append(elem)
    return list_files


def read_csv_from_zip(filename = None,zip_file='data/brut.zip'):
    if filename == None:
        list_files = get_files_list()
        filename = list_files[0]
    zf = ZipFile(zip_file)
    return pd.read_csv(zf.open(filename),sep=';')

def read_csv_from_zip_date(filename = None,zip_file='data/brut.zip'):
    if filename == None:
        list_files = get_files_list()
        filename = list_files[0]
    zf = ZipFile(zip_file)
    dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
    data = pd.read_csv(zf.open(filename), sep=';',parse_dates=[1])
    return data.take([0], axis=1)


filename = get_files_list()[1]
df = read_csv_from_zip_date(filename=filename)
print(df.shape)

print('......__ loading load_data module __ ......')