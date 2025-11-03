import streamlit as st
import pickle
import os
import base64

# ----------------------------
# File Paths (Ensure models are loaded correctly)
# ----------------------------
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'model.pkl')
vectorizer_path = os.path.join(current_dir, 'vectorizer.pkl')

# ----------------------------
# Load the Model & Vectorizer
# ----------------------------
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(vectorizer_path, 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Fake News Detector 📰",
    page_icon="🧠",
    layout="wide",
)

# ----------------------------
# Custom CSS for Styling
# ----------------------------
def load_css():
    st.markdown("""
        <style>
        body {
            background: linear-gradient(135deg, #1c1c1c, #2e2e2e);
            color: #f2f2f2;
            font-family: 'Poppins', sans-serif;
        }
        .main-title {
            text-align: center;
            color: #00c3ff;
            font-size: 48px;
            font-weight: 700;
            margin-top: 10px;
            text-shadow: 2px 2px 10px rgba(0, 195, 255, 0.3);
        }
        .sub-title {
            text-align: center;
            color: #d0d0d0;
            font-size: 20px;
            margin-bottom: 40px;
        }
        .stTextArea textarea {
            background-color: #121212 !important;
            color: #e8e8e8 !important;
            border-radius: 10px;
            border: 1px solid #00c3ff !important;
        }
        .stButton>button {
            background-color: #00c3ff !important;
            color: white !important;
            font-weight: bold;
            border-radius: 10px !important;
            border: none;
            padding: 0.6em 2em;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #0086b3 !important;
            transform: scale(1.05);
        }
        .result-box {
            background-color: #101820;
            border-radius: 12px;
            padding: 20px;
            margin-top: 25px;
            box-shadow: 0px 4px 15px rgba(0, 195, 255, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

# Apply CSS
load_css()

# ----------------------------
# App Title Section
# ----------------------------
st.markdown("<h1 class='main-title'>📰 Fake News Detection System</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Enter a news headline or paragraph to check if it's Real or Fake</p>", unsafe_allow_html=True)

# ----------------------------
# Input Section
# ----------------------------
user_input = st.text_area("🔍 Type or paste your news content below:", height=200)

# ----------------------------
# Prediction Logic
# ----------------------------
if st.button("Detect Fake News"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text before prediction.")
    else:
        input_data = vectorizer.transform([user_input])
        prediction = model.predict(input_data)[0]

        result_color = "#00ff99" if prediction == 0 else "#ff4d4d"
        result_label = "✅ Real News" if prediction == 0 else "🚫 Fake News"

        st.markdown(f"""
        <div class='result-box' style='border-left: 5px solid {result_color};'>
            <h3 style='color: {result_color}; text-align:center;'>{result_label}</h3>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------
# Footer
# ----------------------------
st.markdown("""
    <br><hr style='opacity:0.3;'>
    <p style='text-align:center; color:gray;'>
        Developed with ❤️ by Karthik | Powered by Streamlit
    </p>
""", unsafe_allow_html=True)

