import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# ================================

# 🌟 Load Model and Vectorizer

# ================================

# Make sure these .pkl files are in the same folder as app.py

model_path = "model.pkl"
vectorizer_path = "vectorizer.pkl"

# Load using pickle

with open(model_path, "rb") as model_file:
model = pickle.load(model_file)

with open(vectorizer_path, "rb") as vec_file:
vectorizer = pickle.load(vec_file)

# ================================

# 🎨 Streamlit Page Configuration

# ================================

st.set_page_config(
page_title="Fake News Detection System",
page_icon="📰",
layout="centered",
initial_sidebar_state="collapsed"
)

# Add CSS styling

st.markdown(
""" <style>
body {
background-color: #0e1117;
color: white;
}
.title {
text-align: center;
color: #ffffff;
font-size: 40px;
font-weight: bold;
text-shadow: 0px 0px 10px #00BFFF;
}
.subtitle {
text-align: center;
font-size: 18px;
color: #AAAAAA;
margin-bottom: 20px;
}
.stTextArea textarea {
background-color: #1c1e22;
color: white;
border-radius: 10px;
border: 1px solid #00BFFF;
font-size: 16px;
}
.result-box {
padding: 20px;
text-align: center;
border-radius: 10px;
font-size: 20px;
font-weight: bold;
margin-top: 20px;
}
.fake {
background-color: #FF4B4B;
color: white;
}
.real {
background-color: #00C851;
color: white;
} </style>
""",
unsafe_allow_html=True
)

# ================================

# 📰 App Title

# ================================

st.markdown('<div class="title">📰 Fake News Detection System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter a news headline or paragraph to check if it's Real or Fake</div>', unsafe_allow_html=True)

# ================================

# 🧾 User Input

# ================================

user_input = st.text_area("🧠 Type or paste your news content below:")

if st.button("🔍 Detect Fake News"):
if user_input.strip() == "":
st.warning("⚠️ Please enter some text before detecting.")
else:
try:
# Vectorize the input text
input_data = vectorizer.transform([user_input])

```
        # Predict using the model
        prediction = model.predict(input_data)[0]

        # Display result
        if prediction == 1 or prediction == "REAL":
            st.markdown('<div class="result-box real">✅ The News is Real</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-box fake">🚫 The News is Fake</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
```

