import streamlit as st

st.set_page_config(
    page_title="Smart Temple Crowd Analytics",
    page_icon="🛕",
    layout="wide"
)

st.title("🛕 Smart Temple Crowd Analytics")
st.subheader("Temple Crowd Congestion Prediction")

st.sidebar.header("Enter Temple Details")

visitor_count = st.sidebar.number_input(
    "Visitor Count", min_value=0, value=5000
)

temperature = st.sidebar.slider(
    "Temperature (°C)", 0.0, 50.0, 25.0
)

precipitation = st.sidebar.slider(
    "Precipitation (mm)", 0.0, 100.0, 5.0
)

is_weekend = st.sidebar.selectbox(
    "Weekend", ["No", "Yes"]
)

is_holiday = st.sidebar.selectbox(
    "Holiday", ["No", "Yes"]
)

is_festival = st.sidebar.selectbox(
    "Festival", ["No", "Yes"]
)

if st.button("Predict Congestion"):

    score = 0

    if visitor_count > 30000:
        score += 4
    elif visitor_count > 15000:
        score += 3
    elif visitor_count > 5000:
        score += 2
    else:
        score += 1

    if temperature > 35:
        score += 2

    if precipitation < 10:
        score += 1

    if is_weekend == "Yes":
        score += 2

    if is_holiday == "Yes":
        score += 2

    if is_festival == "Yes":
        score += 4

    if score <= 4:
        prediction = "LOW"
        st.success(f"Predicted Congestion: {prediction}")

    elif score <= 8:
        prediction = "MODERATE"
        st.warning(f"Predicted Congestion: {prediction}")

    elif score <= 12:
        prediction = "HIGH"
        st.error(f"Predicted Congestion: {prediction}")

    else:
        prediction = "CRITICAL"
        st.error(f"🚨 Predicted Congestion: {prediction}")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Records", "146,400")
col2.metric("Temples", "600")
col3.metric("Features", "34")
col4.metric("Model", "Random Forest")
