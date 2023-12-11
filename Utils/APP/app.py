import streamlit as st
import pickle
import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from wordcloud import STOPWORDS

nltk.download('punkt')
stemmer = SnowballStemmer("english")

pickle_in = open("Regression_logistic_model.pkl", "rb")
model = pickle.load(pickle_in)

stopwords_set = set(STOPWORDS).union({'com', 'http', 'html', 'https'})

def remove_stopwords(text):
    words = word_tokenize(text)
    cleaned_words = [word.lower() for word in words if word.lower() not in stopwords_set and len(word) > 3]
    return ' '.join(cleaned_words)

vect_in = open("vectorizer.pkl", "rb")
vectorizer = pickle.load(vect_in)

def is_valid_url(url):
    # Fonction de vérification du format du lien
    return url.startswith("http://") or url.startswith("https://")

def prediction_lien(lien: str):
    try:   
        doc_no_stop_word = remove_stopwords(' '.join([stemmer.stem(word) for word in word_tokenize(lien)]))
        lien_pres = vectorizer.transform([doc_no_stop_word])
        prediction = model.predict(lien_pres)
        
        if prediction == 1:
            return {"message": "Ce lien est un phishing."}
        elif prediction == 0:
            return {"message": "Ce lien est légitime, ne vous inquiétez pas."}
        
    except Exception as e:
        return "erreur ❗️"

st.title("DETECTEUR DE LIEN PHISHING ")

upload = st.text_input("Entrer le lien puis appuyer sur Entrer de votre clavier pour connaître la nature de ce lien ", key="name")
c1, c2 = st.columns(2)

message = " "  
warn_messag = "Ceci n'est pas un lien HTTP ou HTTPS valide."
if st.button("Vérifier le lien"):
    if upload:
        if is_valid_url(upload):
            data = prediction_lien(upload)

            if data == {"message": "Ce lien est un phishing."}:
                message = "Ce lien est un phishing 😰"
            elif data == {"message": "Ce lien est légitime, ne vous inquiétez pas."}:
                message = "Ce lien est légitime, ne vous inquiétez pas 😎"
        else:
            st.warning(warn_messag)
         

st.write(message)
