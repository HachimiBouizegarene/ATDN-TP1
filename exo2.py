import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

data = pd.read_csv("donnees_elevage_poulet.csv")

Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
lowerThreshold = Q1 - (1.5 * IQR) 
upperThreshold = Q3 + (1.5 * IQR) 
#pandas considere que les true sont egales à 1 donc count va aditionner le True
print(f"Nombre d'outliers par IQR : \n{(data < lowerThreshold).sum() + (data > upperThreshold).sum()}")

z_threshold = 3

z_scores = (data - data.mean()) / data.std()
print(f"Nombre d'outliers par zScore : \n{(z_scores > z_threshold ).sum() + (z_scores < -z_threshold ).sum()}")