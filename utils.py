
import pandas as pd

def clean_csv(file_stream):
    df = pd.read_csv(file_stream)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    df.drop_duplicates(inplace=True)
    df.fillna('', inplace=True)
    return df
