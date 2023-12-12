# chall_data354

## Description du repo

Il s'agit d'une api ( application programming interface  )  et une application web  de détection de phishing basée sur un modèle de régression logistique.

L'api est stockée dans le répertoire Utils/API. 

L'application web est stockée dans le répertoire Utils/APP.

le fichier Regression_logistic_model.pkl  est le modèle dumper.

le fichier vectorizer.pkl  est le vectorizer dumper.


## Description du repertoire data

- le fichier fishing-submission_ehouman.csv (  données de prédiction ).

- le fichier fishing-train (1).csv ( données d'entraînement  et de test ).

## Description du repertoire model 

- le fichier Challenge_data354_Ehouman_phishing_detection_final.ipynb qui est le notebook 



## Configuration Requise
- Python 3.x
-  Liste des bibliothèques Python requises : pip install -r requirements.txt

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/golden225/chall_data354.git
   cd chall_data354

2. Pour utiliser l'api 
   ```bash
   pip install -r requirements.txt
   uvicorn api:app --reload


- accéder en local : http://127.0.0.1:8000/

- la route /docs pour l'interface de documentation standard 
- la route /predict pour les prédictions de l'api ( testable dans /docs )


3. Pour l'application web 

   ```bash
   pip install -r requirements.txt
   streamlit run app.py


- accéder en local : http://localhost:8501/

- accéder en reseau : http://172.20.10.4:8501

