# app.py  (copy this entire file)
import streamlit as st
import pickle
import os
import traceback

# ----------------------------
# Helper: get path relative to this file
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# ----------------------------
# Load model & vectorizer with clear errors
# ----------------------------
model = None
vectorizer = None

def load_artifacts():
    global model, vectorizer
    # Check files exist
    missing = []
    if not os.path.isfile(MODEL_PATH):
        missing.append(MODEL_PATH)
    if not os.path.isfile(VECTORIZER_PATH):
        missing.append(VECTORIZER_PATH)
    if missing:
        raise FileNotFoundError(f"Missing files: {', '.join(missing)}")

    # Load with pickle
    with open(MODEL_PATH, "rb") as mf:
        model = pickle.load(mf)
    with open(VECTORIZER_PATH, "rb") as vf:
        vectorizer = pickle.load(vf)

try:
    load_artifacts()
except Exception as e:
    st.title("📰 Fake News Detection System")
    st.error("Failed to load model or vectorizer. See details below.")
    st.markdown("**Reason:**")
    st.code(str(e))
    st.markdown("**Traceback (for debugging):**")
    st.code(traceback.format_exc())
    st.stop()  # stop further execution so user can fix files

# ----------------------------
# Simple CSS styling
# ----------------------------
st.markdown(
    """
    <style>
    .app-header {text-align:center; font-size:34px; font-weight:700; color:#00c3ff; margin-bottom:6px;}
    .app-sub {text-align:center; color:#bfc7cf; margin-bottom:20px;}
    .stTextArea textarea {background:#0f1113; color:#e6eef6; border-radius:8px; border:1px solid #00c3ff;}
    .btn {background:#00c3ff; color:white; font-weight:600; border-radius:8px; padding:8px 18px;}
    .result {padding:18px; border-radius:10px; margin-top:18px; font-size:18px; font-weight:600;}
    .fake {background:#ff4d4d; color:white;}
    .real {background:#00c851; color:white;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# UI
# ----------------------------
st.markdown('<div class="app-header">📰 Fake News Detection System</div>', unsafe_allow_html=True)
st.markdown("<div class='app-sub'>Paste a news headline or short article below and click Detect</div>", unsafe_allow_html=True)

user_text = st.text_area("Type or paste news text here:", height=220)

if st.button("Detect", key="detect_btn"):
    if not user_text or str(user_text).strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        try:
            # Ensure vectorizer is a transformer with transform method
            if not hasattr(vectorizer, "transform"):
                raise TypeError("Loaded vectorizer does not have a 'transform' method.")

            X = vectorizer.transform([user_text])  # <-- standard usage
            if not hasattr(model, "predict"):
                raise TypeError("Loaded model does not have a 'predict' method.")

            pred = model.predict(X)[0]

            # Interpret prediction safely:
            # Many labels are 0/1, or "FAKE"/"REAL". Handle common cases.
            is_real = None
            if isinstance(pred, str):
                p = pred.lower()
                if p in ("real", "true", "1"):
                    is_real = True
                elif p in ("fake", "false", "0"):
                    is_real = False
            elif isinstance(pred, (int, float)):
                # common convention: 1 = real, 0 = fake (but check your training)
                is_real = bool(int(pred))
            else:
                # fallback: try casting
                try:
                    is_real = bool(int(pred))
                except Exception:
                    is_real = None

            if is_real is True:
                st.markdown('<div class="result real">✅ The model predicts: REAL</div>', unsafe_allow_html=True)
            elif is_real is False:
                st.markdown('<div class="result fake">🚫 The model predicts: FAKE</div>', unsafe_allow_html=True)
            else:
                # If label format is unknown, show raw prediction
                st.info(f"Model returned: `{pred}` — check label encoding in training.")
        except Exception as e:
            st.error("An error occurred during prediction. Details below:")
            st.code(str(e))
            st.markdown("Traceback:")
            st.code(traceback.format_exc())

# Footer
st.markdown("---")
st.markdown("Built by Karthik ♠ Model trained in Colab ▼ Model Used LogisticRegression")
