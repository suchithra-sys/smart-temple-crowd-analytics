import streamlit as st

st.title("🛕 Smart Temple Crowd Analytics")

visitor_count = st.number_input("Visitor Count",100,100000,5000)
temperature = st.slider("Temperature",0,50,25)
festival = st.selectbox("Festival",["No","Yes"])
holiday = st.selectbox("Holiday",["No","Yes"])

if st.button("Predict"):

    score = visitor_count

    if festival=="Yes":
        score += 10000

    if holiday=="Yes":
        score += 5000

    if score < 10000:
        prediction = "LOW"
    elif score < 30000:
        prediction = "MODERATE"
    elif score < 60000:
        prediction = "HIGH"
    else:
        prediction = "CRITICAL"

    st.success(f"Predicted Congestion: {prediction}")
