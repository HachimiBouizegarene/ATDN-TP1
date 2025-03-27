import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

data = pd.read_csv("donnees_elevage_poulet.csv")

data_to_process = data[["Poids_poulet_g", "Nourriture_consommee_g_jour", "Temperature_enclos_C"]]

print(data_to_process.describe())
plt.figure(figsize=(15, 7))
for i in range(len(data_to_process.columns)):
    plt.subplot(1, 3, i+1)
    sns.histplot(data_to_process[data_to_process.columns[i]], bins=10)
    plt.title(data_to_process.columns[i])

plt.figure(figsize=(15, 7))
for i in range(len(data_to_process.columns)):
    plt.subplot(1, 3, i+1)
    sns.boxplot(y=data_to_process[data_to_process.columns[i]])
    plt.title(data_to_process.columns[i])

plt.show()