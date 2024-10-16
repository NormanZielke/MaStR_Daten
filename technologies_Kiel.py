import pandas as pd
import numpy as np

from functions import select_columns, berechne_stilllegung, kraftwerke_nach_cutoff, kraftwerke_still

# runtime of technologies
betriebsdauer = {
    'Verbrennungsmotor': 30,
    'Gasturbinen mit Abhitzekessel': 40,
    'Stirlingmotor': 25,
    'Brennstoffzelle': 15,
    'Gegendruckmaschine mit Entnahme': 50,
    'Gasturbinen ohne Abhitzekessel': 30,
    'Kondensationsmaschine mit Entnahme':60
}

cutoff_date = pd.to_datetime('2045-01-01')

#---------------------------------------------------------------------------------------------------------------------->

# Kiel

df_comb_Kiel = pd.read_csv("regions_csv/kiel_combustion.csv",
                        sep=",")
# filter MaStR by selected columns
Kiel_combustion = select_columns(df_comb_Kiel)
# calculate expire date by "betriebsdauer" and gives power plants, which are still in progress
Kiel_combustion_nach_2045 = kraftwerke_nach_cutoff(Kiel_combustion,cutoff_date,betriebsdauer)
# gives power plants, which are expired until cutoff_date
Kiel_combustion_bis_2045_sill = kraftwerke_still(Kiel_combustion,Kiel_combustion_nach_2045)

"""
df = Kiel_combustion[Kiel_combustion["Strasse"] == "Am Kiel-Kanal 2"]

df = Kiel_combustion[Kiel_combustion["Postleitzahl"] == 24106]

df = Kiel_combustion[Kiel_combustion["ThermischeNutzleistung"] == 390]
df = Kiel_combustion[Kiel_combustion["ElektrischeKwkLeistung"] == 330]
"""

#---------------------------------------------------------------------------------------------------------------------->
#Rüdersdorf bei Berlin

df_comb_Ruedersdorf = pd.read_csv("regions_csv/Ruedersdorf_combustion.csv",
                        sep=",")



