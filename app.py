import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Smart Temple Crowd Analytics",
                   page_icon="🛕",
                   layout="wide")

st.title("🛕 Smart Temple Crowd Analytics")

st.sidebar.header("Prediction Inputs")

visitor_count = st.sidebar.number_input(
    "Visitor Count",100,100000,5000)

temperature = st.sidebar.slider(
    "Temperature (°C)",0.0,50.0,25.0)

precipitation = st.sidebar.slider(
    "Precipitation (mm)",0.0,100.0,5.0)

is_weekend = st.sidebar.selectbox(
    "Weekend?",["No","Yes"])

is_holiday = st.sidebar.selectbox(
    "Holiday?",["No","Yes"])

is_festival = st.sidebar.selectbox(
    "Festival?",["No","Yes"])

if st.button("Predict Congestion"):

    score = (
        visitor_count/10000 +
        temperature/20 +
        precipitation/10 +
        (is_weekend=="Yes")*2 +
        (is_holiday=="Yes")*2 +
        (is_festival=="Yes")*3
    )

    if score < 5:
        prediction = "LOW"
    elif score < 10:
        prediction = "MODERATE"
    elif score < 15:
        prediction = "HIGH"
    else:
        prediction = "CRITICAL"

    st.success(
        f"Predicted Congestion Level: {prediction}"
    )
