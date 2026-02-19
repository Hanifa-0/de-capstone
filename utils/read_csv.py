import pandas as pd
def reading_file(csv_file):
    df = pd.read_csv(csv_file)
    return df
