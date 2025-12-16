import pandas as pd

def merge_multiple_datasets(files, key='id'):
    if not files:
        return pd.DataFrame()
    df = pd.read_csv(files[0])
    for file in files[1:]:
        df_temp = pd.read_csv(file)
        df = df.merge(
            df_temp,
            on=key,
            how='left'
        )
    return df

file_list = [
    'lis_titoli.csv', 
    'lis_autori.csv', 
    'lis_date.csv',
    'lis_argomenti.csv', 
    'lis_basidati.csv', 
    'lis_doi.csv',
    'lis_editori.csv', 
    'lis_licenze.csv',
    'lis_riviste.csv',
    'lis_edizione.csv',
    'lis_volume.csv', 
    'lis_pagine.csv', 
    'lis_url.csv'
    ]
df = merge_multiple_datasets(file_list, key='id')

df.to_csv("data.csv", index=False)