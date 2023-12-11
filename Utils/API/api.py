import pickle
from fastapi import FastAPI, HTTPException
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
import nltk
from wordcloud import STOPWORDS

nltk.download('punkt')

stemmer = SnowballStemmer("english")

app = FastAPI()

# Chargement du model
with open("Regression_logistic_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Chargement du vectorizer 
with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

#  stopwords
stopwords_set = set(STOPWORDS).union({'com', 'http', 'html', 'https'})

def remove_stopwords(text):
    """Fonction pour supprimer les stopwords d'un texte."""
    words = word_tokenize(text)
    cleaned_words = [word.lower() for word in words if word.lower() not in stopwords_set and len(word) > 3]
    return ' '.join(cleaned_words)

@app.get("/")
def home():
    """Endpoint pour la page d'accueil."""
    return {"message": "Bienvenue sur mon API de détection de phishing."}

@app.post("/prediction_lien")
def prediction_lien(lien: str):
    """Endpoint pour la prédiction du lien."""
    try:
        # Prétraitement du texte
        doc_no_stop_word = remove_stopwords(' '.join([stemmer.stem(word) for word in word_tokenize(lien)]))
        
        # Transformation avec le vectorizer
        lien_pres = vectorizer.transform([doc_no_stop_word])
        
        # Prédiction avec le modèle
        prediction = model.predict(lien_pres)
        
        if prediction == 1:
            return {"message": "Ce lien est identifié comme un phishing."}
        elif prediction == 0:
            return {"message": "Ce lien est légitime, ne vous inquiétez pas."}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
