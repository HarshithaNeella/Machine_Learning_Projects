import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn  

st.title("Risk Categories in EV ")

with open("D:\ML_preparation\Tree_model", "rb") as f:
    loaded_model = pickle.load(f)

# Create input` fields for user to enter values
df = {}
df['Age'] = st.number_input("Enter value for Age")
df['City_Tier'] = st.selectbox("Enter value for City_Tier", options=["Tier 1", "Tier 2", "Tier 3", "Tier 4", "Tier 5"])
df["EV_Type"] = st.selectbox("Enter value for EV_Type", options=["2KW", "3KW", "4KW","5KW"])
df["Battery_Capacity_kWh"] = st.number_input("Enter value for Battery_Capacity_kWh ")
df["Charging_Sessions_Per_Month"] = st.number_input("Enter value for Charging_Sessions_Per_Month")
df["Avg_Charge_Cost"] = st.number_input("Enter value for Avg_Charge_Cost")
df["Distance_Travelled_Per_Month"]= st.number_input("Enter value for Distance_Travelled_Per_Month")
df["Income_Level"] = st.selectbox("Enter value for Income_Level", options=["Low", "Medium", "High"])
df["Loan_Taken"] = st.selectbox("Enter value for Loan_Taken ", options=["Yes", "No"])
df["Missed_Payments_Last_6M"] = st.number_input("Enter value for Missed_Payments_Last_6M")
df["Tenure_Months"] = st.number_input("Enter value for Tenure_Months")
df["Charging_Location_Type"] = st.selectbox("Enter value for Charging_Location_Type", options=["Highway", "Public", "Private"])
df["App_Usage_Score"] = st.number_input("Enter value for App_Usage_Score")
df["Charger_Working_Status"] = st.selectbox("Enter value for Charger_Working_Status", options=["Working", "Not Working"])
df["Charging_Time_Minutes"] = st.number_input("Enter value for Charging_Time_Minutes")
df["Charging_Efficiency_Index"] = st.number_input("Enter value for Charging_Efficiency_Index")
input_df = pd.DataFrame([df])

# Make prediction using the loaded model
if st.button("Predict Risk Category"):
    prediction = loaded_model.predict(input_df)
    st.write(f"Predicted Risk Category: {prediction[0]}")
