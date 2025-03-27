import scipy.stats as stats

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("donnees_elevage_poulet.csv")
variables = ['Poids_poulet_g', 'Nourriture_consommee_g_jour', 'Temperature_enclos_C']
for var in variables:
    stat, p_value = stats.shapiro(data[var]) 
    print(f"Test pour {var}: p-value : {p_value}")

mediane_poid = data["Poids_poulet_g"].median()
group_1 = data[data["Poids_poulet_g"] < mediane_poid]
group_2 = data[data["Poids_poulet_g"] > mediane_poid]

t_stat, p_values = stats.ttest_ind(group_1, group_2)
for i, p_value in enumerate(p_values):
    print(f"Variable {data.columns[i]}: {p_value:.4f} {'< 0.05' if p_value < 0.05 else '>= 0.05'}")
