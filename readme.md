
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

### Exo 3 :
*test de ShapiroWilk :*
| **Variable**                          | **p-value**                     |
|---------------------------------------|---------------------------------|
| *Poids_poulet_g*                 | 9.10e-06                        |
| *Nourriture_consommee_g_jour*       | 6.23e-07                        |
| *Temperature_enclos_C*              | 4.41e-07                        |

Sachant que l'hypothèse nulle est que la population est normalement distribuée,  en choisissant un alpha egale à 0.05, on peut en deduire que l'hypothèse nulle est rejetée pour chaque variable.
[Source](https://fr.wikipedia.org/wiki/Test_de_Shapiro-Wilk)

*T de Student :*
Je crée deux groupes en les séparant par la médiane de la variable Poids, ensuite j'applique la fonction ttest_ind de scipy.stats pour obtenir les p-values entre les groupes, qui décrivent à quel point les deux groupes sont différents. Plus cette valeur est petite, plus les groupes sont différents sur la variable concernée, vois les résultats :
| Variable                           | p-value  |
|-------------------------------------|----------|
| Poids_poulet_g                      | 0.0000   |
| Nourriture_consommee_g_jour         | 0.7307   |
| Temperature_enclos_C                | 0.6041   |
| Humidite_%                          | 0.4714   |
| Age_poulet_jours                    | 0.1576   |
| Gain_poids_jour_g                   | 0.9398   |
| Taux_survie_%                       | 0.1607   |
| Cout_elevage_FCFA                   | 0.4053   |

En choisissant un alpha égal à 0.05, on en déduit que les deux groupes sont similaires sur toutes les variables sauf le Poids, et c'est normal car c'est celle que nous avons choisie pour séparer les deux groupes.

### Exo 4 :
####  **> ⚠️ALERTE : J'ai utilisé TOUTES les variables pour cet EXO, pas seulement les 3 premières !**
---  
Pour appliquer l'acp avec numpy, j'ai d'abord standardisé les données, j'ai calculer la covariance des variables ensuite j'en ai extrait les vecteurs propres et valeurs propres avec `np.linalg.eig`, ensuite je les ai trié par ordre croissant. Ensuite j'ai projeter les données sur les composantes principales en faisant le produit scalaire des données avec les vecteurs propres.
Apres application d'ACP avec numpy, j'obtiens cette projections sur les deux premiere composantes : 
![Acp manual](https://github.com/HachimiBouizegarene/ATDN-TP1/blob/master/assets/acp_manual.png?raw=true)

voici la proportion de variance expliquée par chaque composante principal : ```[15.82633829 14.32670966 13.79586215 13.18341518 12.68416454 11.83528158
  9.74507921  8.60314938]```. J'aurais suggeré de garder toutes les composantes sauf les deux derniere , qui expliquent environ 80% de la variance, cela va nous permettre de réduire la complexité du modèle tout en conservant la majorité de l'information.


Ensuite, avec `KernelPCA` j'ai appliquee des ACP a noyau `(linéaire, RBF, polynomial)` et j'ai obtenu ces résultats : 
![ACP noyeau](https://github.com/HachimiBouizegarene/ATDN-TP1/blob/master/assets/acp_noyau.png?raw=true)
Les noyau RBF, polynomial donnent des resultats mediocres par rapport a l'ACP avec noyau lineaire (qui est equivalent à l'ACP classique). KernelPCA n'apporte donc pas de valeur ajoutée et dégrade carrement les résultats. On peut en deduire qu'aucune transformation non linéaire n'est nécessaire.