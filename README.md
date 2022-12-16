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
L'objectiu d'aquest treball és aprendre a predir la felicitat de la població d'una regió en funció del PIB per capita, l'esperança de vida, la confiança en el govern, la generositat de la població envers els altres, el suport d'amics i/o familiars i la llibertat per a prendre decisions sobre la pròpia vida.

### Preprocessat
He substituït els outliers d'algunes variables per la seva mitjana.
He normalitzat les dades perquè totes estiguin disperses en un rang de 0 a 1.
Les variables que tenen més correlació amb l'Happiness Score (mitjana de felicitat d'un país) són : Economy (PIB per capita), Health (l'esperança de vida), Familiy (Suport Social) i Freedom (llibertat).
També vaig realitzar una PCA (Principal Component Analysis), amb la qual vaig concloure que Trust i Generosity no eren tan necessàries per als models com les altres variables, però no era segur descartar-les.
### Model
![Underfitting+HO](https://user-images.githubusercontent.com/73697639/208115232-35027c99-a259-4af9-9cff-ac2575fe3c8f.PNG)

Nota 1: Els models que els hi falta la primera fila van ser introduits a aquesta pràctica després de canviar el dataset.

Nota 2: Els models que els hi falta completar l'última fila van ser descartats per a reduir la cerca d'hiperparametres.
## Conclusions
El World Happiness Report és un informe útil elaborat per les Nacions Unides que permet a les nacions veure com el nivell de felicitat dels ciutadans es relaciona amb els nivells de felicitat d'altres països. Preguntes com "quines característiques específiques d'una nació determinen el nivell de felicitat dels ciutadans?" i "quina d'aquestes característiques hauria de millorar una nació per assegurar que els ciutadans siguin feliços?" es poden respondre a través del procés de l'anàlisi de les dades realitzat.

Per a respondre a les preguntes anteriors, sabem que el PIB és l'indicador més fort de felicitat. Un país decebut en la seva puntuació hauria d'intentar augmentar el seu PIB per càpita primer. Obtenir millors puntuacions en l'esperança de salut, el suport social i la llibertat no faria mal, i la Generositat i les Percepcions de la Corrupció poden ser colpejades o perdudes (totes aquestes mètriques ajudarien a fer que un país se centrés a maximitzar la inversió de recursos per millorar la seva puntuació de felicitat).

Per a poder predir com serà de feliç la població d'un país fent modificacions en el PIB per càpita, l'esperança de salut, el suport social o la llibertat, els millors models a fer són: l'AdaBoost, el Voting Regressor i la Xarxa Neuronal. Per a prediccions una mica pessimistes és recomanable utilitzar el Voting Regressor, mentre que per a prediccions més optimistes ho és l'AdaBoost.
## Idees per treballar en un futur
Considero que seria interessant tornar a fer aquest treball en uns deu anys perquè tindria moltes més dades amb les quals poder fer millor les prediccions. Tot i això, les Nacions Unides, que són qui fa el dataset, haurien d'establir un conveni per a cada any. El canvi, aportació i/o eliminació de variables redueix molt les característiques a escollir a l'hora de fer un model que inclogui diversos anys. Tenint tot això en compte, es podrà augmentar la precisió de les prediccions de forma destacable.
