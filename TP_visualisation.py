import os
import sys
import shutil
import pandas as pd
from dateutil import parser
import traceback
import zipfile

#from joblib.memory import Memory

import load_data as ld

velo_filename = ld.get_files_list()[1]
names_velo = ['date','Station','Status','Nombre de vélos disponibles','Nombre d\'emplacements disponibles']
df_velo = ld.read_csv_from_zip(filename=velo_filename,names=names_velo)
print((df_velo.date == None).value_counts())


meteo_filename = ld.get_files_list()[2]
names_meteo = ['Timestamp','Status','Clouds','Humidity','Pressure','Rain','WindGust','WindVarEnd','WindVarBeg','WindDeg','WindSpeed','Snow','TemperatureMax','TemperatureMin','TemperatureTemp']
df_meteo = ld.read_csv_from_zip(filename=meteo_filename,names=names_meteo)
print((df_meteo.Timestamp == None).value_counts())

def sampling(dataframe, time='10min', name='Timestamp'):
    dataframe = dataframe.set_index('Timestamp').resample(time).last().dropna().reset_index()
    return dataframe

print(df_meteo.iloc[1:50,:])
df_meteo = sampling(df_meteo)
print(df_meteo.iloc[1:50,:])