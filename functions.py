import pandas as pd
import pickle

# import dictionary for ags_id's

def filter_by_reg(df):
    with open("gemeindeschluessel.pkl", "rb") as datei:
        gemeindeschluessel = pickle.load(datei)
        regions = gemeindeschluessel.keys()
    df = df.loc[df["EinheitBetriebsstatus"] == "In Betrieb"] # pick only plants which are currently running
    con = []
    for region in regions:
        con.append(df.loc[df.Gemeinde == region])
    df_f = pd.concat(con)
    return df_f


