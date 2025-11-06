import streamlit as st
import pickle
import re

# Load the saved model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Streamlit App
st.title("📧 Spam Email Detector")
st.write("This AI model classifies emails as **Spam** or **Ham (Not Spam)**")

# Input box for email text
user_input = st.text_area("Enter the email/message text here:")

# Prediction button
if st.button("Check Mail"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text first!")
    else:
        # Preprocess the text (optional)
        cleaned_input = re.sub(r'\s+', ' ', user_input.strip())

        # Transform the input using the vectorizer
        input_data = vectorizer.transform([cleaned_input])

        # Make prediction
        prediction = model.predict(input_data)

        # Display result
        if prediction[0] == 1:
            st.success("✅ Mail Ochindi Chusko ra, **SPAM kaadhu idi HAM 😄**")
        elif prediction[0] == 0:
            st.error("🚨 Adhi Spam Mail ra nik Kanpinchanu nenu **HAHAHAHA 😈**")
        else:
            st.info("🤔 Idi naa dataset lo leni Mail!!!")
st.markdown("""
    <footer>
        Made with ❤️ by <b>Karthik.M</b> | BE CSE-AI Student <br>
    </footer>
""", unsafe_allow_html=True)