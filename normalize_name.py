import load_data as ld

df = ld.read_csv_from_zip(filename='brut/bicincitta_parma_summary.csv')

print(df)
