import pandas as pd
import pickle

def filter_by_reg(df,regions):
    """
    :param df: pandas dataframe
    :param regions: dtype: string array
    :return: df_f: pandas dataframe
    """
    df = df.loc[df["EinheitBetriebsstatus"] == "In Betrieb"] # pick only plants which are currently running
    con = []
    for region in regions:
        con.append(df.loc[df.Gemeinde == region])
    df_f = pd.concat(con)
    return df_f

def topologie(df):
    """
    :param df: pandas dataframe
    :return capacities: pandas dataframe
    """
    capacities_t = df.groupby(["Technologie", "Hauptbrennstoff"]).ThermischeNutzleistung.agg(["sum", "count"]).reset_index()
    capacities_b = df.groupby(["Technologie", "Hauptbrennstoff"]).Bruttoleistung.sum().reset_index()
    capacities = pd.merge(capacities_b, capacities_t)
    capacities.rename(columns={"Bruttoleistung": "Bruttoleistung [kW]",
                               "sum": "Thermische Nutzleistung [kW]", "count": "Anzahl"}, inplace=True)
    return capacities

def select_columns(df):
    df = df.loc[:,["NameKraftwerk","NameStromerzeugungseinheit","Bruttoleistung_extended",
                   "ThermischeNutzleistung","ElektrischeKwkLeistung","Hauptbrennstoff",
                   "Technologie","Strasse","Hausnummer","Laengengrad",
                   "Breitengrad","Inbetriebnahmedatum"]]
    df = df.sort_values(by="ThermischeNutzleistung", ascending=False).reset_index(drop=True)
    return df

# Funktion zur Berechnung des Stilllegungsdatums
def berechne_stilllegung(row,betriebsdauer):
    technologie = row['Technologie']
    inbetriebnahmedatum = pd.to_datetime(row['Inbetriebnahmedatum'])

    if technologie in betriebsdauer:
        # Berechnung der Stilllegung
        jahre = betriebsdauer[technologie]
        stilllegungsdatum = inbetriebnahmedatum + pd.DateOffset(years=jahre)
        return stilllegungsdatum
    else:
        return None  # falls die Technologie nicht definiert ist

# Funktion für Ausgabe von Zeilen mit Kraftwerken, die noch nach cutoff_date in Betrieb sind
def kraftwerke_nach_cutoff(df,cutoff_date,betriebsdauer):
    df['Stilllegung'] = df.apply(berechne_stilllegung, axis=1, betriebsdauer=betriebsdauer)
    df_nach_cutoff =df[df['Stilllegung'] > cutoff_date]
    return df_nach_cutoff

# Funktion für Ausgabe von Zeilen mit Kraftwerken, die bis cutoff_date stillgelegt wurden
def kraftwerke_still(df1,df2):
    df_expired = pd.merge(df1, df2,
                          how="outer", indicator=True).query('_merge == "left_only" ').drop(columns=['_merge'])
    return df_expired



