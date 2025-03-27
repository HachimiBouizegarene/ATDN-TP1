
# Rapport TP ATDN 1 Bouizegarene Hachimi

### Exo 1 :

**Moyenne, médiane, écart-type, variance et les quartiles :**
|                         | Poids_poulet_g | Nourriture_consommee_g_jour | Temperature_enclos_C |
|-------------------------|----------------|-----------------------------|----------------------|
| **count**               | 200            | 200                         | 200                  |
| **mean**                | 2509.58        | 129.75                      | 28.39                |
| **std**                 | 898.44         | 44.01                       | 2.07                 |
| **min**                 | 821            | 51                          | 25                   |
| **25%**                 | 1810.75        | 95.75                       | 26.6                 |
| **50% (median)**        | 2481.5         | 135.5                       | 28.5                 |
| **75%**                 | 3356.5         | 165.25                      | 30.3                 |
| **max**                 | 3974           | 199                         | 31.9                 |


**Histogrammes :**\
*- Poids :*
![Histogramme poid](https://github.com/HachimiBouizegarene/ATDN-TP1/blob/master/assets/histogramme_poids.png?raw=true)

*- nourriture :*
![Histogramme nourriture](https://github.com/HachimiBouizegarene/ATDN-TP1/blob/master/assets/histogramme_nourriture.png?raw=true)

*- temperature :*
![Histogramme temperature](https://github.com/HachimiBouizegarene/ATDN-TP1/blob/master/assets/histogramme_temperature.png?raw=true)

**BoxPlots :**\
*- Poids :*
![boite_moustache poid](https://github.com/HachimiBouizegarene/ATDN-TP1/blob/master/assets/boite_moustache_poids.png?raw=true)

*- nourriture :*
![boite_moustache nourriture](https://github.com/HachimiBouizegarene/ATDN-TP1/blob/master/assets/boite_moustache_nourriture.png?raw=true)

*- temperature :*
![boite_moustache temperature](https://github.com/HachimiBouizegarene/ATDN-TP1/blob/master/assets/boite_moustache_temperature.png?raw=true)

**Interpretation des résultats:**
- Entre les variables nourriture et température, on peut observer une certaine similarité. À partir de cela, on peut supposer que ces deux variables sont corrélées.
- La distribution des poids est assez uniforme, on n'a pas de pic dominant ce qui signifie que le poids des poulet est trés variée


### Exo 2 :
En utilisant IQR avec ce code : 
```python
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
lowerThreshold = Q1 - (1.5 * IQR) 
upperThreshold = Q3 + (1.5 * IQR) 
print(f"Nombre d'outliers : \n{(data < lowerThreshold).sum() + (data > upperThreshold).sum()}")
```
On obtient 0 outliers.

En utilisant le Z-score avec ce code : 
```python
z_threshold = 3
z_scores = (data - data.mean()) / data.std()
print(f"Nombre d'outliers par zScore : \n{(z_scores > z_threshold ).sum() + (z_scores < -z_threshold ).sum()}")
```
On obtient également 0 outliers.
