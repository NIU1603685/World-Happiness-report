# World-Happiness-report




# Pràctica Kaggle APC UAB 2022-23
### Nom: Sofia Di Capua 
### DATASET: World-Happiness-report
### URL: https://www.kaggle.com/datasets/unsdsn/world-happiness
## Resum
T'encanta on vius i t'escandalitza perquè tothom no viu al teu país? O potser odies absolutament on vius i no entens per què algú es traslladaria al teu país. En qualsevol cas, pots obtenir resposta a les teves preguntes mitjançant aquesta anàlisi. Hi ha molts factors que afecten directament o indirectament la felicitat general d'un país. Sent una qüestió subjectiva com aquesta, conèixer exactament quins són els factors que més afecten en la felicitat d'una població és un repte.

The World Happiness Report és un dataset publicat per les Nacions Unides que classifica els països en funció dels nivells de felicitat. L'informe conté una puntuació de felicitat (Happiness Score) que després s'utilitza per a determinar el rang d'un país en relació amb les puntuacions d'un altre. Hi ha diferents mètriques que es juxtaposen amb la puntuació i tenia curiositat per veure quina mètrica podia ser assenyalada (si és que fos) com la millor predictora de la puntuació d'un país. Aquesta puntuació de felicitat s'ha calculat emprant les respostes d'una enquesta estadísticament representativa.

L'enquesta a partir de la qual es va crear aquest dataset constava de preguntes amb resposta numèrica ("Imagineu una escala, amb passos numerats des del 0 com a més baix fins al 10 com a més alt. La part superior de l'escala representa la millor vida possible per a tu i el fons de l'escala representa la pitjor vida possible per a tu. En quin pas de l'escala diria vostè personalment que sent en aquest moment?") o binària ("Estàs satisfet o insatisfet amb la vostra llibertat per escollir què fas amb la teva vida?", "Has donat diners a una organització benèfica el mes passat?", etc.). Per això hi ha variables que van del 0 al 10 i d'altres que van del 0 a l'1. Per a més informació llegir els Statistical Appendix dels datasets de cada any que trobareu al següent enllaç:

https://worldhappiness.report/archive/

### Objectius del dataset
L'objectiu d'aquest treball és aprendre a predir la felicitat de la població d'una regió en funció del PIB per capita, l'esperança de vida, la confiaça en el govern, la generositat de la població envers els altres, el suport d'amics i/o familiars i la llibertat per a prendre decisions sobre la propia vida.

### Preprocessat
He substituit els outliers d'algunes variables per la seva mitjana. 
He normalitzat les dades per a qué totes estiguin disperses en un rang de 0 a 1.
Les variables que tenen més correlació amb el Happiness Score (mitjana de felicitat d'un país) són : Economy (PIB per capita), Health (l'esperança de vida), Familiy (Suport Social) i Freedom (llibertat).
També vaig realitzar una PCA (Principal Component Analysis), amb la qual vaig concloure que Trust i Generosity no eren tan necesàries per als models com les latres variables però no era segur descartar-les.
### Model
![Underfitting+HO](https://user-images.githubusercontent.com/73697639/208115232-35027c99-a259-4af9-9cff-ac2575fe3c8f.PNG)
| Model | Hiperparametres | Mètrica | Temps |
| -- | -- | -- | -- |

| [Random Forest](link) | 100 Trees, XX | 57% | 100ms |
| Random Forest | 1000 Trees, XX | 58% | 1000ms |
| SVM | kernel: lineal C:10 | 58% | 200ms |
| -- | -- | -- | -- |
| [model de XXX](link al kaggle) | XXX | 58% | ?ms |
| [model de XXX](link al kaggle) | XXX | 62% | ?ms |
## Conclusions
El millor model que s'ha aconseguit ha estat...
En comparació amb l'estat de l'art i els altres treballs que hem analitzat....
## Idees per treballar en un futur
Crec que seria interesant tornar a fer aquest treball ens uns 10 anys perquè tindria moltes més dades amb les quals poder fer millor les prediccions. Tot i així les Nacions Unides, que són qui fa el dataset, haurien d'etablir un conveni per a tots els anys. El canvi, aportació i/o elimianció de variables redueix molt les caracteristiques a escollir a l'hora de fer un model que inclogui diversos anys. Tenint tot aixó en compte, es podrà augmentar la precisió de les prediccions de forma destacable.
