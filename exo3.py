import scipy.stats as stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("donnees_elevage_poulet.csv")
variables = ['Poids_poulet_g', 'Nourriture_consommee_g_jour', 'Temperature_enclos_C']
for var in variables:
    stat, p_value = stats.shapiro(data[var]) 
    print(f"Test pour {var}: p-value : {p_value}")
