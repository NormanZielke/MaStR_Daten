import pandas as pd
import numpy as np
from functions import filter_by_reg

"""
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
"""
# --------------------------------------------------------------------------------------------------------------------->
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
import pickle
# dict gemeindeschluessel save as file
with open("gemeindeschluessel.pkl", "wb") as datei:
    pickle.dump(gemeindeschluessel, datei)

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

df_comb = filter_by_reg(combustion)
df_biomass = filter_by_reg(biomass)
df_gsgk = filter_by_reg(gsgk) # --> only 2 powerplants

# --------------------------------------------------------------------------------------------------------------------->
# summarize data by technologies with their fueltype

capacities_comb = df_comb.groupby(["Gemeinde","Technologie","Hauptbrennstoff"]).Bruttoleistung.sum()
capacities_biomass = df_biomass.groupby(["Gemeinde","Technologie","Hauptbrennstoff"]).Bruttoleistung.sum()

# --------------------------------------------------------------------------------------------------------------------->
# show data

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print("bnetza_mastr_combustion_raw.csv")
print(capacities_comb)
print("bnetza_mastr_biomass_raw.csv")
print(capacities_biomass)

pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')

print("bnetza_mastr_gdgk_raw.csv")
print(df_gsgk.loc[:,["Gemeinde","Technologie","Bruttoleistung"]])