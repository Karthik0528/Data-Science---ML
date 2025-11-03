# 📰 Fake News Detection System

An AI-based web app that predicts whether a given news headline or article is **Fake** or **Real**, built using **Machine Learning (NLP)** and deployed using **Streamlit**.

---

## 🚀 Live Demo

👉 [[[Click here to try the app]](https://fakenewsdetection10.streamlit.app/)](#) *(Replace this link with your Streamlit Cloud app link after deployment)*

---

## 🧠 Project Overview

The rise of misinformation has made it crucial to identify fake news automatically.
This project uses Natural Language Processing (NLP) and Machine Learning to classify news articles as **Real** or **Fake**.

---

## 🧩 Tech Stack

* **Python** 🐍
* **Pandas**, **NumPy**, **Scikit-learn** for ML
* **NLTK** for text preprocessing
* **Streamlit** for interactive web app
* **Pickle** for model serialization

---

## 📁 Folder Structure

```
FakeNewsDetection/
├── P4_FakeNewsDetection.ipynb   # Colab notebook (model training)
├── app.py                       # Streamlit web app
├── model.pkl                    # Trained model
├── vectorizer.pkl               # TF-IDF vectorizer
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Data-Science---ML.git
cd Data-Science---ML/FakeNewsDetection
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App Locally

```bash
streamlit run app.py
```

---

## 🧪 How It Works

1. Enter a news headline or paragraph.
2. The text is processed using TF-IDF vectorization.
3. A trained ML model predicts whether it’s **Fake** or **Real**.
4. The result is displayed with color-coded visualization.

---

## 🌐 Deployment on Streamlit Cloud

1. Push this folder to your GitHub repository.
2. Visit [https://share.streamlit.io](https://share.streamlit.io).
3. Connect your repo and select:

   ```
   FakeNewsDetection/app.py
   ```
4. Click **Deploy** 🚀

---

## 📸 Preview

*(Add screenshots here after deployment)*

---

## 👨‍💻 Author

**Karthik**
🎓 BE CSE - Artificial Intelligence
📍 Saveetha School of Engineering

---

## 🏷️ License

This project is open-source and available under the **MIT License**.
