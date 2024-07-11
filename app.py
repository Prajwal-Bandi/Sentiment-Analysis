import streamlit as st
import pickle

# Function to load the model and vectorizer
def load_model_and_vectorizer():
    with open("./vector.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    with open("./model.pkl", "rb") as f:
        ensemble_model = pickle.load(f)
    return vectorizer, ensemble_model

# Function to get sentiment
def get_sentiment(Review):
    vectorizer, ensemble_model = load_model_and_vectorizer()
    x = vectorizer.transform([Review]).toarray()
    
    # Predicting sentiment
    y = ensemble_model.predict(x)
    return y[0]  # Return the first (and only) prediction

# Streamlit app
st.title("Sentiment Analysis App")

user_input = st.text_area("Enter text to analyze sentiment")

if st.button("Analyze"):
    sentiment = get_sentiment(user_input)
    st.write(f"This is a {sentiment} sentiment!")
