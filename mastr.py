import pandas as pd
import numpy as np
from functions import filter_by_reg, topologie

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

regions = gemeindeschluessel.keys()

df_comb = filter_by_reg(combustion, regions)
df_biomass = filter_by_reg(biomass, regions)
df_gsgk = filter_by_reg(gsgk, regions) # --> only 2 power plants

# --------------------------------------------------------------------------------------------------------------------->
# summarize data by technologies with their fueltype

capacities_comb = df_comb.groupby(["Gemeinde", "Technologie", "Hauptbrennstoff"]).Bruttoleistung.sum()
capacities_biomass = df_biomass.groupby(["Gemeinde", "Technologie", "Hauptbrennstoff"]).Bruttoleistung.sum()

# filter dataframe "combustion" to create dataframe for every region

# combustion
df_comb_Strausberg = combustion.loc[combustion.Gemeinde == "Strausberg"]
df_comb_Erkner = combustion.loc[combustion.Gemeinde == "Erkner"]
df_comb_Ruedersdorf = combustion.loc[combustion.Gemeinde == "Rüdersdorf bei Berlin"]
df_comb_GruenH = combustion.loc[combustion.Gemeinde == "Grünheide (Mark)"]
df_comb_Bocholt = combustion.loc[combustion.Gemeinde == "Bocholt"]
df_comb_Zwickau = combustion.loc[combustion.Gemeinde == "Zwickau"]
df_comb_Ingolstadt = combustion.loc[combustion.Gemeinde == "Ingolstadt"]
df_comb_Kassel = combustion.loc[combustion.Gemeinde == "Kassel"]
df_comb_Kiel = combustion.loc[combustion.Gemeinde == "Kiel"]

# filter dataframe "biomass" to create dataframe for every region

# biomass

df_biomass_Strausberg = biomass.loc[biomass.Gemeinde == "Strausberg"]
df_biomass_Erkner = biomass.loc[biomass.Gemeinde == "Erkner"]
df_biomass_Ruedersdorf = biomass.loc[biomass.Gemeinde == "Rüdersdorf bei Berlin"]
df_biomass_GruenH = biomass.loc[biomass.Gemeinde == "Grünheide (Mark)"]
df_biomass_Bocholt = biomass.loc[biomass.Gemeinde == "Bocholt"]
df_biomass_Zwickau = biomass.loc[biomass.Gemeinde == "Zwickau"]
df_biomass_Ingolstadt = biomass.loc[biomass.Gemeinde == "Ingolstadt"]
df_biomass_Kassel = biomass.loc[biomass.Gemeinde == "Kassel"]
df_biomass_Kiel = biomass.loc[biomass.Gemeinde == "Kiel"]

# filter dataframes of regions by technologie with their capacities

# combustion

capacities_comb_Strausberg = topologie(df_comb_Strausberg)
capacities_comb_Erkner = topologie(df_comb_Erkner)
capacities_comb_Ruedersdorf = topologie(df_comb_Ruedersdorf)
capacities_comb_GruenH = topologie(df_comb_GruenH)
capacities_comb_Bocholt = topologie(df_comb_Bocholt)
capacities_comb_Zwickau = topologie(df_comb_Zwickau)
capacities_comb_Ingolstadt = topologie(df_comb_Ingolstadt)
capacities_comb_Kassel = topologie(df_comb_Kassel)
capacities_comb_Kiel = topologie(df_comb_Kiel)

# biomass

capacities_biomass_Strausberg = topologie(df_biomass_Strausberg)
capacities_biomass_Erkner = topologie(df_biomass_Erkner)
capacities_biomass_Ruedersdorf = topologie(df_biomass_Ruedersdorf)
capacities_biomass_GruenH = topologie(df_biomass_GruenH)
capacities_biomass_Bocholt = topologie(df_biomass_Bocholt)
capacities_biomass_Zwickau = topologie(df_biomass_Zwickau)
capacities_biomass_Ingolstadt = topologie(df_biomass_Ingolstadt)
capacities_biomass_Kassel = topologie(df_biomass_Kassel)
capacities_biomass_Kiel = topologie(df_biomass_Kiel)

# --------------------------------------------------------------------------------------------------------------------->
# Output

with pd.ExcelWriter("360_SLE_Topologie_Combustion.xlsx") as writer:
    capacities_comb_Strausberg.to_excel(writer, sheet_name="Strausberg", index=False)
    capacities_comb_Erkner.to_excel(writer, sheet_name="Erkner", index=False)
    capacities_comb_Ruedersdorf.to_excel(writer, sheet_name="Rüdersdorf bei Berlin", index=False)
    capacities_comb_GruenH.to_excel(writer, sheet_name="Grünheide (Mark)", index=False)
    capacities_comb_Bocholt.to_excel(writer, sheet_name="Bocholt", index=False)
    capacities_comb_Zwickau.to_excel(writer, sheet_name="Zwickau", index=False)
    capacities_comb_Ingolstadt.to_excel(writer, sheet_name="Ingolstadt", index=False)
    capacities_comb_Kassel.to_excel(writer, sheet_name="Kassel", index=False)
    capacities_comb_Kiel.to_excel(writer, sheet_name="Kiel", index=False)

with pd.ExcelWriter("360_SLE_Topologie_biomass.xlsx") as writer:
    capacities_biomass_Strausberg.to_excel(writer, sheet_name="Strausberg", index=False)
    capacities_biomass_Erkner.to_excel(writer, sheet_name="Erkner", index=False)
    capacities_biomass_Ruedersdorf.to_excel(writer, sheet_name="Rüdersdorf bei Berlin", index=False)
    capacities_biomass_GruenH.to_excel(writer, sheet_name="Grünheide (Mark)", index=False)
    capacities_biomass_Bocholt.to_excel(writer, sheet_name="Bocholt", index=False)
    capacities_biomass_Zwickau.to_excel(writer, sheet_name="Zwickau", index=False)
    capacities_biomass_Ingolstadt.to_excel(writer, sheet_name="Ingolstadt", index=False)
    capacities_biomass_Kassel.to_excel(writer, sheet_name="Kassel", index=False)
    capacities_biomass_Kiel.to_excel(writer, sheet_name="Kiel", index=False)
