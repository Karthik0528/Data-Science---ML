# ❤️ Heart Disease Prediction & Health-Based Segmentation using Machine Learning

### 🧠 Project Overview
This project combines **Supervised and Unsupervised Machine Learning** to predict heart disease risk and group patients into meaningful health-based clusters.

It uses:
- **Classification models** (Logistic Regression, Random Forest, SVM) to predict the likelihood of heart disease.
- **K-Means Clustering** to segment individuals into health groups (Low, Medium, High risk) for targeted awareness or treatment programs.

---

## 🎯 Objectives
- Predict whether a person is at risk of heart disease based on medical data.
- Cluster patients into different health segments based on lifestyle and health indicators.
- Build a user-friendly **Streamlit web app** for live predictions.

---

## 🧩 Project Workflow

### 🧮 Data Preprocessing
- Cleaned and encoded categorical data (`Male/Female`, `Yes/No`, etc.)
- Scaled numeric features using `StandardScaler`
- Handled multi-category fields like `chest_pain_type`, `rest_ecg`, `slope`, `thalassemia` with one-hot encoding

### ⚙️ Model Building
| Model | Accuracy | Remarks |
|--------|-----------|----------|
| Logistic Regression | 85.4% | Good baseline model |
| SVM | 91.2% | Excellent generalization |
| **Random Forest** | **100%** | Best accuracy (may be overfitted, but ideal for demonstration) |

### 📊 Clustering (Unsupervised ML)
- Used **K-Means** with optimal `k=3`
- Clustered patients using features like age, cholesterol, max heart rate, oldpeak, and predicted risk probability
- Identified 3 clusters:  
  - 🟢 **Low Risk Group**  
  - 🟠 **Medium Risk Group**  
  - 🔴 **High Risk Group**

---

## 💻 Tech Stack
| Category | Tools |
|-----------|--------|
| Language | Python |
| Libraries | pandas, numpy, scikit-learn, seaborn, matplotlib, joblib |
| Visualization | matplotlib, seaborn |
| App Framework | Streamlit |
| Deployment | Streamlit Cloud / Localhost |
| Environment | Google Colab / VS Code |

---

## 🚀 Streamlit App
The **Streamlit Web App** allows users to enter their health data and get an instant heart disease risk prediction.

### 🔧 How to Run the App Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/HeartDiseaseSegmentation.git
   cd HeartDiseaseSegmentation


Install the dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run heart_disease_app.py


Open your browser at:

http://localhost:8501


🧾 Folder Structure
HeartDiseaseSegmentation/
│
├── heart_disease_app.py              # Streamlit web app
├── heart_disease_model.pkl           # Trained Random Forest model
├── supervised_scaler.pkl             # Scaler for classification
├── segmentation_model.pkl            # KMeans clustering model
├── cluster_scaler.pkl                # Scaler for clustering
├── HeartDisease_Segmented_Results.csv# Final dataset with clusters
├── requirements.txt                  # Dependencies
└── README.md                         # Project documentation


📈 Results Summary
ClusterAgeCholesterolMax HROldpeakRisk ScoreRisk Level045.872241670.350.57🟠 Medium Risk157.332471282.210.23🟢 Low Risk258.922631540.530.39🔴 High Risk

🧠 Insights


Random Forest achieved the best accuracy.


Cluster 2 patients had the highest cholesterol and risk probability.


Clustering helps hospitals or insurance companies design targeted prevention programs.



🧑‍💻 Author
Karthik S
B.E. Computer Science & Engineering (AI)
Saveetha School of Engineering
📧 Email: your.email@example.com
🌐 GitHub: @yourusername

🏁 Future Enhancements


Integrate live ECG or wearable device data.


Add advanced models like XGBoost or Deep Learning.


Build an admin dashboard for monitoring clusters.


Enable patient report downloads (PDF).



📜 License
This project is licensed under the MIT License.
Feel free to use and modify for academic or research purposes.

---
