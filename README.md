# 📞 Telecom Customer Churn Prediction Project

This project uses machine learning to predict whether a telecom customer is likely to churn.  
It includes a **Streamlit web dashboard**, a **trained ML model**, and a **Jupyter Notebook** used for data exploration and model training.



## Project Overview

- Customer churn is when customers stop using a company's service.  
- Telecom companies use churn prediction to identify high-risk customers so they can take action.

This project:

- Preprocesses telecom customer data  
- Trains ML models (Random Forest, Logistic Regression)  
- Deploys a **Streamlit dashboard** for real-time predictions  
- Visualizes model output, including churn probability  



##  Machine Learning Models Used

- **Random Forest Classifier** (used for final prediction)
- Logistic Regression (tested during development)


---
📊 Dashboard Features

The Streamlit app allows you to enter:

- Area Code
- International Plan (Yes/No)
- Voice Mail Plan (Yes/No)
- Customer Service Calls
- Total Day Minutes
- Total International Minutes

Based on these, the model predicts:

🟢 Unlikely to churn

🔴 Likely to churn

  
---
📓 Notebook (Training + EDA)

Telecom_churn.ipynb includes:

- Dataset loading
- Exploratory data analysis
- Label encoding
- Model training & accuracy
- Model saving with pickle

---
🧑‍💻Technologies Used:

- Python 3
- Streamlit
- Pandas
- Scikit-learn
- Jupyter Notebook

