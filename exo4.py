import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("donnees_elevage_poulet.csv")
data_normalized = (data - data.mean()) / data.std()
covariance = data_normalized.cov()

valeurs_propres, vecteurs_propres = np.linalg.eig(covariance)
sorted_indices = np.argsort(valeurs_propres)[::-1]
vecteurs_propres_sorted = vecteurs_propres[:, sorted_indices]
valeurs_propres_sorted = valeurs_propres[sorted_indices]
data_pca = np.dot(data_normalized, vecteurs_propres_sorted)

plt.figure(figsize=(8, 6))
plt.scatter(data_pca[:, 0], data_pca[:, 1])
plt.title("Projection des donnees sur les deux premieres composantes principales")
plt.xlabel("1 composante principale")
plt.ylabel("2 composante principale")

explained_variance_ratio = valeurs_propres_sorted / np.sum(valeurs_propres_sorted)
print(f"Proportion de la variance expliquée par chaque composante principale: {explained_variance_ratio}")
plt.show()