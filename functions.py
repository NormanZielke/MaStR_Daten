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
    capacities.rename(columns={"Bruttoleistung": "Bruttoleistung [kW]", "sum": "Thermische Nutzleistung [kW]", "count": "Anzahl"}, inplace=True)
    return capacities

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
