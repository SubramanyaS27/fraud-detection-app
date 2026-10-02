# 💳 Real-Time Financial Fraud Detection System

**Live Demo:** https://fraud-detection-app-mt95.onrender.com  
**Repository:** https://github.com/SubramanyaS27/fraud-detection-app

> End-to-end ML system for fraud detection, built from data cleaning to production deployment.

### 🎯 Problem
Traditional systems miss evolving fraud and create false positives. This system handles extreme imbalance (0.17% fraud in 284k transactions) and provides real-time detection.

### 🧠 Tech Stack
**ML:** Random Forest (Final), Logistic Regression, Decision Tree  
**Data:** Python, Pandas, Scikit-Learn, SMOTE, StandardScaler, Feature Engineering  
**Deployment:** Streamlit, Docker, Render, Git  
**Viz:** Matplotlib, Seaborn, Plotly

### 📊 Model
- **Final Model:** Random Forest
- **Techniques:** SMOTE, StandardScaler, Hyperparameter Tuning
- Outperformed baseline models on Precision, Recall, and F1.

### 🏗️ Workflow
Raw Data -> EDA -> Scaling -> SMOTE -> Random Forest Training -> Evaluation -> Streamlit App -> Docker -> Render

### ✨ Features
1.  **Simplified Inference:** Live app uses curated profiles (High Amount, Night Txn etc.) for demo ease. Full 30-feature model available in notebook.
2.  **Analytics Dashboard:** Visualizes fraud patterns and trends.
3.  **Production Ready:** Live, containerized, deployed app.

### 🚀 Run Locally
```bash
git clone https://github.com/SubramanyaS27/fraud-detection-app.git
cd fraud-detection-app
pip install -r requirements.txt
streamlit run app.py

📂 Structure
├── app.py
├── model/fraud_model.pkl
├── notebooks/
├── requirements.txt
├── Dockerfile
└── README.md

👨‍💻 Author
Subramanya S
GitHub: https://github.com/SubramanyaS27
Live App: https://fraud-detection-app-mt95.onrender.com
Built as complete end-to-end ML project from data to deployment.