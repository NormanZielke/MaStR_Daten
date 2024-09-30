import pandas as pd
import numpy as np

from functions import berechne_stilllegung

df_comb_Kiel = pd.read_csv("regions_csv/kiel_combustion.csv",
                        sep=",")

# distribution of technologies
technologie_counts = df_comb_Kiel['Technologie'].value_counts().reset_index()
#
technologies_Kiel = df_comb_Kiel.loc[:,["NameKraftwerk","NameStromerzeugungseinheit","ThermischeNutzleistung",
                                        "ElektrischeKwkLeistung","Technologie","Inbetriebnahmedatum"]]
# runtime of technologies
betriebsdauer = {
    'Verbrennungsmotor': 30,
    'Gasturbinen mit Abhitzekessel': 40,
    'Stirlingmotor': 25,
    'Brennstoffzelle': 15,
    'Gegendruckmaschine mit Entnahme': 50,
    'Gasturbinen ohne Abhitzekessel': 30
}

technologies_Kiel['Stilllegung'] = technologies_Kiel.apply(berechne_stilllegung, axis=1, betriebsdauer=betriebsdauer)

# Filter für Kraftwerke, die nach 2045 stillgelegt werden
cutoff_date = pd.to_datetime('2045-01-01')
kraftwerke_nach_2045 = technologies_Kiel[technologies_Kiel['Stilllegung'] > cutoff_date]
"""
df_comb_Kiel[df_comb_Kiel["Strasse"] == "Am Kiel-Kanal 2"]

df = df_comb_Kiel[df_comb_Kiel["Postleitzahl"] == 24106]
"""