# chall_data354

## Description api

Une API de détection de phishing basée sur un modèle de régression logistique.

Il est stocké dans le repectoire Utils/API
Il contient un fichier api.py qui l'api

requirements.txt pour les bibliothèques de l'api

Regression_logistic_model.pkl qui est le modèle 

vectorizer.pkl qui est le vectorizer

## Description application web 

Une application web de détection de phishing basée sur un modèle de régression logistique.
Il est stocké dans le repectoire Utils/APP

## Description du repectoire data

Il contient le fichier fishing-submission_ehouman.csv qui qui sont les données de prediction

Il contient le fichier fishing-train (1).csv qui sont les données d'entrainement  et de test 

## Description du repectoire model 

Il contient Challenge_data354_Ehouman_phishing_detection_final.ipynb qui est le notebook 

## Fonctionnalités
- Prédiction de phishing ( ou pas ) pour les liens fournis.


## Configuration Requise
- Python 3.x
-  Liste des bibliothèques Python requises : pip install -r requirements.txt

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/golden225/chall_data354.git
   cd chall_data354

2. Pour utiliser l'api 

   - pip install -r requirements.txt

   - lancer avec  : uvicorn api:app --reload

   - accéder en local : http://127.0.0.1:8000/

   - la route /docs pour l'interface de documentation standard 
   - la route /predict pour les prédictions de l'api ( testable dans /docs )


3. Pour l'application web 
   
   - pip install -r requirements.txt

   - lancer avec streamlit run app.py

   - accéder en local : http://localhost:8501/

   - accéder en reseau : http://172.20.10.4:8501

