import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("donnees_elevage_poulet.csv")

print(data)

data_to_process = data[["Poids_poulet_g", "Nourriture_consommee_g_jour", "Temperature_enclos_C"]]

moyennes = data_to_process.mean()
ecart_type = data_to_process.std()
variance = data_to_process.var()
mediane = data_to_process.median()
quartiles = data_to_process.quantile([0.25, 0.5, 0.75])

for i in range(len(data_to_process.columns)):
    plt.figure(figsize=(8,6))
    sns.histplot(data_to_process[data_to_process.columns[i]], bins=20)
    plt.title(data_to_process.columns[i])

for i in range(len(data_to_process.columns)):
    plt.figure(figsize=(8,6))
    sns.boxplot(y=data_to_process[data_to_process.columns[i]])
    plt.title(data_to_process.columns[i])

plt.show()