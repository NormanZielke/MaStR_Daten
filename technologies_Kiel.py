import pandas as pd
import numpy as np

df_comb_Kiel = pd.read_csv("regions_csv/kiel_combustion.csv",
                        sep=",")

# distribution of technologies
technologie_counts = df_comb_Kiel['Technologie'].value_counts().reset_index()
#
technologies_Kiel = df_comb_Kiel.loc[:,["Technologie","NameKraftwerk","NameKraftwerksblock","NameStromerzeugungseinheit","Inbetriebnahmedatum"]]