import streamlit as st
import joblib
import pandas as pd

# ------------------------
# PAGE CONFIG
# ------------------------

st.set_page_config(
    page_title="Smart Temple Crowd Analytics",
    page_icon="🛕",
    layout="wide"
)

# ------------------------
# LOAD MODEL
# ------------------------

model = joblib.load("rf_model.pkl")

# ------------------------
# HEADER
# ------------------------

st.title("🛕 Smart Temple Crowd Analytics")
st.caption("Temple Crowd Prediction using Machine Learning")

st.markdown("---")

# ------------------------
# KPI CARDS
# ------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("Model", "Random Forest")
c2.metric("Accuracy", "94%")
c3.metric("Features", "6")
c4.metric("Status", "Active")

st.markdown("---")

# ------------------------
# TABS
# ------------------------

tab1, tab2 = st.tabs(
    ["🔮 Prediction", "ℹ️ About Project"]
)

# =================================================
# TAB 1
# =================================================

with tab1:

    st.subheader("Crowd Congestion Prediction")

    col1, col2 = st.columns(2)

    with col1:

        visitor_count = st.number_input(
            "Visitor Count",
            min_value=100,
            max_value=100000,
            value=5000
        )

        temperature = st.slider(
            "Temperature (°C)",
            0.0,
            50.0,
            25.0
        )

        precipitation = st.slider(
            "Precipitation (mm)",
            0.0,
            100.0,
            5.0
        )

    with col2:

        is_weekend = st.selectbox(
            "Weekend",
            ["No", "Yes"]
        )

        is_festival = st.selectbox(
            "Festival",
            ["No", "Yes"]
        )

        is_holiday = st.selectbox(
            "Holiday",
            ["No", "Yes"]
        )

    if st.button("🚀 Predict Crowd Level"):

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

        result = mapping.get(pred, pred)

        if result == "LOW":
            st.success("🟢 Predicted Crowd Level: LOW")

        elif result == "MODERATE":
            st.info("🟡 Predicted Crowd Level: MODERATE")

        elif result == "HIGH":
            st.warning("🟠 Predicted Crowd Level: HIGH")

        else:
            st.error("🔴 Predicted Crowd Level: CRITICAL")

        st.subheader("Recommended Actions")

        if result == "LOW":
            st.write("✅ Normal temple operations")
            st.write("✅ Regular monitoring")

        elif result == "MODERATE":
            st.write("✅ Increase volunteer support")
            st.write("✅ Monitor queue lengths")

        elif result == "HIGH":
            st.write("⚠ Open additional entry gates")
            st.write("⚠ Deploy extra security")

        else:
            st.write("🚨 Activate emergency crowd control")
            st.write("🚨 Restrict new entries temporarily")
            st.write("🚨 Notify temple authorities")

# =================================================
# TAB 2
# =================================================

with tab2:

    st.subheader("Project Overview")

    st.write("""
    Smart Temple Crowd Analytics is a Big Data and Machine Learning
    project developed to predict temple crowd congestion levels.

    Technologies Used:
    - Hadoop HDFS
    - Apache Spark
    - PySpark
    - Random Forest
    - Python
    - Streamlit

    Objective:
    To assist temple authorities in crowd management,
    visitor safety, and resource planning.
    """)

    st.subheader("Input Features")

    st.write("""
    • Visitor Count

    • Temperature

    • Precipitation

    • Weekend Indicator

    • Festival Indicator

    • Holiday Indicator
    """)
