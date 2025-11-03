import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("📰 Fake News Detection App")

news = st.text_area("Enter the news text or title:")

if st.button("Predict"):
    transformed_text = vectorizer.transform([news])
    prediction = model.predict(transformed_text)[0]
    if prediction == '0':
        st.error("🚫 This news seems **FAKE**.")
    else:
        st.success("✅ This news seems **REAL**.")
