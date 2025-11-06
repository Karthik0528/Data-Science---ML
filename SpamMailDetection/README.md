📧 Spam Mail Detection App (Streamlit + ML)

This project is a Machine Learning–based Spam Email Detector built using Python, Scikit-Learn, and Streamlit.
It classifies messages as Spam or Ham (Not Spam) based on their content using a trained TF-IDF vectorizer and a supervised ML model.

🚀 Features

🧠 Uses TF-IDF Vectorizer for text feature extraction

🤖 Pre-trained Machine Learning model for spam classification

💬 Simple Streamlit web interface

⚡ Real-time predictions (no retraining needed)

🌐 Ready for deployment on Streamlit Cloud / Render / Hugging Face Spaces

🏗️ Tech Stack
Component	Technology
Language	Python 🐍
Web Framework	Streamlit
ML Library	scikit-learn
Feature Extraction	TF-IDF Vectorizer
Model	Logistic Regression / Naive Bayes (customizable)
Serialization	pickle
📂 Folder Structure
spam_detector_app/
│
├── app.py                # Streamlit app file
├── model.pkl             # Saved trained ML model
├── vectorizer.pkl        # Saved TF-IDF vectorizer
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

⚙️ How It Works

The input email text is taken from the user.

It is transformed into numerical vectors using the TF-IDF vectorizer.

The pre-trained model predicts whether the email is Spam (0) or Ham (1).

Streamlit displays a fun and interactive message as output 🎉

🧩 Sample Code (Prediction Logic)
input_mail = ['WINNER!! You have been selected to receive a £900 reward!']
new_input = vectorizer.transform(input_mail)
prediction = model.predict(new_input)

if prediction[0] == 1:
    print("✅ Mail Ochindi Chusko ra, SPAM kaadhu idi HAM 😄")
elif prediction[0] == 0:
    print("🚨 Adhi Spam Mail ra nik Kanpinchanu nenu HAHAHAHA 😈")
else:
    print("🤔 Idi naa dataset lo leni Mail!!!")

🧠 Training Summary

Dataset: SMS Spam Collection / Email Spam Dataset

Preprocessing: Text cleaning, lowercasing, removing stopwords, TF-IDF transformation

Labels:

0 → Spam

1 → Ham (Not Spam)

▶️ Run Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit app
streamlit run app.py

3️⃣ Open in browser
http://localhost:8501

🌐 Deploy Online
Streamlit Cloud (Recommended)

Push your project to GitHub

Go to https://share.streamlit.io

Connect your repo → Deploy 🚀

Or use Render.com or Hugging Face Spaces.

📦 requirements.txt Example
streamlit
scikit-learn
pandas
numpy

🧑‍💻 Author

Karthik
🎓 BE CSE - Artificial Intelligence Student
💡 Passionate about Machine Learning, NLP & AI Applications

📜 License

This project is open-source under the MIT License.
Feel free to use, modify, and share with credit.

✨ Example Output

Input:

"Congratulations! You have won a free vacation to Goa. Call now!"

Output:

🚨 Adhi Spam Mail ra nik Kanpinchanu nenu HAHAHAHA 😈
