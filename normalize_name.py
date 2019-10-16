import load_data as ld


df_summry = ld.read_csv_from_zip()
station_name = df_summry.station.unique()

def normalize_station(station):
    global station_name
    for s in station_name:
        if station in s:
            return s
    return station
def normalize(df=None):
    if df ==None:
        names = ['date','Station','Status','Nombre de vélos disponibles','Nombre d\'emplacements disponibles']
        list_files = ld.get_files_list()
        df = ld.read_csv_from_zip(filename=list_files[1],names=names)
    df.iloc[:,1] = df.iloc[:,1].apply(normalize_station)
    return df

print(normalize().head())