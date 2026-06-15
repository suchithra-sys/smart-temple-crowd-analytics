import streamlit as st
import joblib
import pandas as pd

model = joblib.load("rf_model.pkl")

st.title("🛕 Smart Temple Crowd Analytics")

visitor_count = st.number_input("Visitor Count", 100, 100000, 5000)
temperature = st.slider("Temperature", 0.0, 50.0, 25.0)
precipitation = st.slider("Precipitation", 0.0, 100.0, 5.0)

is_weekend = st.selectbox("Weekend", ["No", "Yes"])
is_festival = st.selectbox("Festival", ["No", "Yes"])
is_holiday = st.selectbox("Holiday", ["No", "Yes"])

if st.button("Predict Crowd Level"):

    data = pd.DataFrame([{
        "Visitor_Count": visitor_count,
        "Temperature_C": temperature,
        "Precipitation_mm": precipitation,
        "Is_Weekend": 1 if is_weekend == "Yes" else 0,
        "Is_Festival": 1 if is_festival == "Yes" else 0,
        "Is_Holiday_Num": 1 if is_holiday == "Yes" else 0
    }])

    pred = model.predict(data)[0]

    mapping = {
        0: "LOW",
        1: "MODERATE",
        2: "HIGH",
        3: "CRITICAL"
    }

    st.success(
        f"Predicted Congestion Level: {mapping.get(pred, pred)}"
    )
