import pandas as pd
import numpy as np

"""
INPUT
    # 1 dictionary with Municipalities and their Municipality key
    # 2 Dataframes with existing stock of technologies from open-mastr
"""
# 1

gemeindeschluessel = {
    "Rüdersdorf bei Berlin": "12064428",
    "Strausberg": "12064472",
    "Erkner": "12067124",
    "Grünheide (Mark)": "12067201",
    "Ingolstadt": "09161000",
    "Kassel": "06611000",
    "Bocholt": "05554008",
    "Kiel": "01002000",
    "Zwickau": "14524330",
}

"""
import pickle

# dict gemeindeschluessel save as file
with open(r"functions\gemeindeschluessel.pkl", "wb") as datei:
    pickle.dump(gemeindeschluessel, datei)
"""

# 2

# Read Data from open-mastr

combustion = pd.read_csv("csv/bnetza_mastr_combustion_raw.csv",
                        sep=",")
biomass = pd.read_csv("csv/bnetza_mastr_biomass_raw.csv",
                        sep=",")
gsgk = pd.read_csv("csv/bnetza_mastr_gsgk_raw.csv",
                        sep=",")

# --------------------------------------------------------------------------------------------------------------------->
# filter raw data by Municipalities


regions = gemeindeschluessel.keys()



