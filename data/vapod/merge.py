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
    'va_titoli.csv', 
    'va_artisti.csv', 
    'va_date.csv',
    'va_generi.csv', 
    'va_luoghi.csv', 
    'va_collezioni.csv',
    'va_contenuti.csv', 
    'va_movimenti.csv',
    'va_soggetti.csv',
    'va_altezze.csv',
    'va_larghezze.csv'
    ]
df = merge_multiple_datasets(file_list, key='id')

df.to_csv("data.csv", index=False)