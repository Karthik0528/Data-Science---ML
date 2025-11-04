import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
import base64

st.set_page_config(page_title="Calories Burnt — AI Studio", layout="wide", page_icon="🔥")

# -----------------------------
# Helper: Load model
# -----------------------------
@st.cache_resource
def load_model(path="model.pkl"):
    try:
        model = joblib.load(path)
        return model
    except Exception as e:
        return None

model = load_model()

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif !important;
    }

    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #0b1220 40%, #021022 100%);
        color: #e6eef8;
        min-height: 100vh;
    }

    .app-card {
        background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
        border: 1px solid rgba(255,255,255,0.04);
        box-shadow: 0 8px 30px rgba(2,6,23,0.6);
        padding: 24px;
        border-radius: 16px;
    }

    .hero {
        display: flex;
        align-items: center;
        gap: 18px;
    }
    .logo-circle {
        width:64px; height:64px; border-radius:16px;
        background:linear-gradient(135deg,#ff7a18,#af002d);
        display:flex; align-items:center; justify-content:center;
        font-weight:800; color:white; font-size:24px;
        box-shadow: 0 8px 20px rgba(175,0,45,0.25);
    }

    h1.streamlit-heading {
        font-size:28px; margin:0; color: #fff;
    }
    p.lead { margin:4px 0 0 0; color: #c9d6e8; opacity:0.9 }

    .stNumberInput>div>div>input {
        border-radius: 10px !important;
        padding: 12px !important;
        background: rgba(255,255,255,0.02) !important;
        color: #e6eef8 !important;
        border: 1px solid rgba(255,255,255,0.04) !important;
    }

    .big-predict {
        background: linear-gradient(90deg,#ff7a18,#ffb199) !important;
        color: #08121b !important;
        font-weight:700 !important;
        padding: 12px 18px !important;
        border-radius: 12px !important;
    }

    .result-card {
        background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
        border-radius: 12px; padding: 18px; text-align:center;
        border: 1px solid rgba(255,255,255,0.04);
    }

    .muted { color:#9fb0ce; font-size:13px }
    .footer { color:#7f9bb3; font-size:12px; opacity:0.9 }

    @media (max-width: 760px) {
        .hero {flex-direction:row}
        .logo-circle {width:52px;height:52px}
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Top section

left_col, right_col = st.columns([2, 1])
with left_col:
    st.markdown(
        "<div class='hero app-card'>"
        "<div class='logo-circle'>🔥</div>"
        "<div><h1 class='streamlit-heading'>Calories Burnt Predictor — AI Studio</h1>"
        "<p class='lead'>Accurate, fast predictions using your wearable & activity inputs.</p></div>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.write("\n")
    st.markdown("<div class='muted'>Tip: For best results, use averaged heart rate and duration from your wearable device.</div>", unsafe_allow_html=True)

with right_col:
    st.markdown("<div class='app-card'>", unsafe_allow_html=True)
    st.markdown("**Model Status:**")
    if model is None:
        st.error("Model not found. Make sure 'model.pkl' is in the app folder.")
    else:
        st.success("Model loaded — ready to predict!")
    st.markdown("</div>", unsafe_allow_html=True)

st.write("\n")


# Main input area

with st.container():
    st.markdown("<div class='app-card'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        duration = st.number_input("Duration (minutes)", min_value=1.0, value=30.0, step=1.0)
        age = st.number_input("Age", min_value=10, value=28, step=1)

    with col2:
        heart_rate = st.number_input("Average Heart Rate (bpm)", min_value=40.0, value=110.0, step=1.0)
        weight = st.number_input("Weight (kg)", min_value=30.0, value=70.0, step=0.5)

    with col3:
        body_temp = st.number_input("Body Temperature (°C)", min_value=34.0, max_value=42.0, value=37.0, step=0.1)
        intensity = st.selectbox("Activity Intensity", ["Low", "Moderate", "High"], index=1)

    st.write("\n")

    intensity_map = {"Low": 0, "Moderate": 1, "High": 2}
    intensity_val = intensity_map[intensity]

    predict_html = "<button class='big-predict' id='predict-btn'>Predict Calories Burnt</button>"
    st.markdown(predict_html, unsafe_allow_html=True)

    if st.button("Run Prediction", key="predict_native"):
        input_df = pd.DataFrame([[duration, heart_rate, body_temp, age, weight, intensity_val]],
                                columns=['Duration', 'Heart_Rate', 'Body_Temp', 'Age', 'Weight', 'Intensity'])

        if model is None:
            st.error("Prediction failed — model not loaded. Upload the .pkl file in the app directory.")
        else:
            try:
                pred = model.predict(input_df)
                calories = float(pred[0])

                st.markdown("<div class='result-card'>", unsafe_allow_html=True)
                st.markdown(f"<h2 style='margin:0'>🔥 {calories:.2f} kcal</h2>")
                st.markdown("<div class='muted'>Estimated calories burnt for the activity</div>")
                st.markdown("</div>", unsafe_allow_html=True)

                kpi1, kpi2, kpi3 = st.columns(3)
                kpi1.metric("Duration (min)", f"{duration}")
                kpi2.metric("Avg HR (bpm)", f"{heart_rate}")
                kpi3.metric("Intensity", intensity)

                out_df = input_df.copy()
                out_df['Predicted_Calories'] = calories
                csv = out_df.to_csv(index=False).encode('utf-8')
                st.download_button("Download prediction (CSV)", csv, "calories_prediction.csv", "text/csv")

            except Exception as e:
                st.exception(e)

    st.markdown("</div>", unsafe_allow_html=True)


# Batch predictions (CSV upload)

st.write("\n")
with st.container():
    st.markdown("<div class='app-card'>", unsafe_allow_html=True)
    st.subheader("Batch Predictions")
    st.write("Upload a CSV with columns: Duration, Heart_Rate, Body_Temp, Age, Weight, Intensity (0/1/2)")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"], key="batch")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            if model is None:
                st.error("Model not loaded; cannot run batch predictions.")
            else:
                preds = model.predict(df)
                df['Predicted_Calories'] = preds
                st.dataframe(df)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("Download results", csv, "batch_predictions.csv", "text/csv")
        except Exception as e:
            st.exception(e)
    st.markdown("</div>", unsafe_allow_html=True)


# Footer

st.write("\n")
with st.container():
    st.markdown("<div class='app-card'>", unsafe_allow_html=True)
    st.markdown("<div style='display:flex;justify-content:space-between;align-items:center'>")
    st.markdown("<div class='footer'>Made with ❤️ • AI Studio — Calories Model</div>", unsafe_allow_html=True)
    st.markdown("<div class='footer'>Tips: average your wearable readings for better accuracy.</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)