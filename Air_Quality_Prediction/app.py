import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open("AQI_deplo.pkl", "rb") as f:
    knn = pickle.load(f)

st.title("AQI Prediction App")

city = st.selectbox("City ", ['Hyderabad', 'Delhi', 'Mumbai', 'Bengaluru', 'Visakhapatnam',
       'Jaipur', 'Thiruvananthapuram', 'Coimbatore', 'Lucknow', 'Patna',
       'Chandigarh', 'Shillong', 'Amaravati', 'Chennai', 'Ahmedabad',
       'Kochi', 'Amritsar', 'Talcher', 'Jorapokhar', 'Gurugram',
       'Brajrajnagar', 'Guwahati', 'Kolkata', 'Bhopal', 'Aizawl',
       'Ernakulam'
    
])



pm = int(st.number_input("PM2.5", value=0.00))
no = int(st.number_input("NO", value=0.00))
no2 = int(st.number_input("NO2", value=0.00))
nox = int(st.number_input("NOx", value=0.00))
co = int(st.number_input("CO", value=0.00))
so2 = int(st.number_input("SO2", value=0.00))
o3= int(st.number_input("O3", value=0.00))
benzene= int(st.number_input("Benzene", value=0.00))


if st.button("Predict AQI"):

    input_df = pd.DataFrame([{
        "City": city,
        "PM2.5": pm,
        "NO": no,
        "NO2": no2,
        "NOx":nox,
        "CO": co,
        "SO2": so2,
        "O3":o3,
        "Benzene": benzene,
        
    }])
    

    result = knn.predict(input_df)[0]

    st.success(f"Predicted AQI : {result:}")
