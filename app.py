import streamlit as st
import pandas as pd
import pickle

with open("churn_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="📞Customer Churn Prediction", layout="wide")
st.title("📞Customer Churn Prediction Dashboard")
st.write("Enter customer details below to predict if the customer is likely to churn.")

col1, col2 = st.columns(2)

with col1:
    area_code = st.selectbox("Area Code", [408, 415, 510])
    international_plan = st.selectbox("International Plan", ["Yes", "No"])
    voice_mail_plan = st.selectbox("Voice Mail Plan", ["Yes", "No"])
with col2:
    customer_service_calls = st.number_input("Customer Service Calls", min_value=0, max_value=10)
    total_day_minutes = st.number_input("Total Day Minutes", min_value=0.0, max_value=500.0)
    total_intl_minutes = st.number_input("Total Intl Minutes (0–50)", min_value=0.0, max_value=50.0)
  
input_data = pd.DataFrame({
    "Area code": [area_code],
    "International plan": [1 if international_plan == "Yes" else 0],
    "Voice mail plan": [1 if voice_mail_plan == "Yes" else 0],
    "Customer service calls": [customer_service_calls],
    "Total day minutes": [total_day_minutes],
    "Total intl minutes": [total_intl_minutes]
})

if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] 

    st.markdown("---") 

    if prediction == 1:
        st.error(f"🔴Customer is likely to churn!\nProbability: **{probability:.2f}**")
    else:
        st.success(f"🟢Customer is unlikely to churn.\nProbability: **{probability:.2f}**")
    
    st.metric(label="Churn Probability", value=f"{probability*100:.1f}%")
