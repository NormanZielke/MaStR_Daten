import pandas as pd
import pickle

# import dictionary for ags_id's

def filter_by_reg(df):
    with open("gemeindeschluessel.pkl", "rb") as datei:
        gemeindeschluessel = pickle.load(datei)
        regions = gemeindeschluessel.keys()
    con = []
    for region in regions:
        con.append(df.loc[df.Gemeinde == region])
    df_f = pd.concat(con)
    return df_f
