import os
import create_folder as cf

def sampling(dataframe, time='10min', name='Timestamp'):
    dataframe = dataframe.set_index(name).resample(time).last()#.dropna().reset_index()
    return dataframe

def samplestation(dataframe, namestation = 'Station', name_date='date'):
    station_name = dataframe[namestation].unique()
    count = 0;
    for s in station_name:
        df = sampling(dataframe.loc[(dataframe['Station'] == s)],name='date')
        #cf.create_folder(df.Station.unique())
        os.mkdir('stations' + "/" + s)
        path = 'stations' + "/" + s + '/output.xlsx'
        df.to_excel(path)
        df.head()
        if count == 0:
            return True
        count += 1

    return True
