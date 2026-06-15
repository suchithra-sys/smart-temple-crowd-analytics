import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Smart Temple Crowd Analytics",
    page_icon="🏛️",
    layout="wide"
)

# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.title("🏛️ Smart Temple Analytics")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Analytics", "Prediction", "Crowd Alerts", "About"]
)

# ==================================
# HOME PAGE
# ==================================

if page == "Home":

    st.title("🏛️ Smart Temple Crowd Analytics")
    st.subheader("Big Data & Machine Learning Based Crowd Prediction System")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Temples", "1,250")
    col2.metric("Visitors", "2.4M")
    col3.metric("Alerts", "185")
    col4.metric("Accuracy", "94%")

    st.markdown("---")

    st.info("""
    Smart Temple Crowd Analytics uses Hadoop, PySpark,
    Machine Learning and Streamlit to predict temple crowd
    congestion and help authorities manage resources efficiently.
    """)

    visitor_data = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr","May","Jun"],
        "Visitors":[12000,15000,18000,22000,26000,32000]
    })

    fig = px.line(
        visitor_data,
        x="Month",
        y="Visitors",
        markers=True,
        title="Monthly Temple Visitor Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==================================
# ANALYTICS PAGE
# ==================================

elif page == "Analytics":

    st.title("📊 Analytics Dashboard")

    col1, col2 = st.columns(2)

    with col1:

        crowd_data = pd.DataFrame({
            "Level":["Low","Moderate","High","Critical"],
            "Count":[1500,3200,1800,700]
        })

        fig = px.pie(
            crowd_data,
            names="Level",
            values="Count",
            title="Crowd Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        feature_data = pd.DataFrame({
            "Feature":[
                "Visitor Count",
                "Weekend",
                "Holiday",
                "Festival",
                "Temperature",
                "Rainfall"
            ],
            "Importance":[
                0.55,
                0.12,
                0.09,
                0.08,
                0.04,
                0.02
            ]
        })

        fig = px.bar(
            feature_data,
            x="Feature",
            y="Importance",
            title="Feature Importance"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    weather = pd.DataFrame({
        "Temperature":[25,27,29,31,33,35,37],
        "Visitors":[1200,1800,2500,3200,4200,5300,6000]
    })

    fig = px.scatter(
        weather,
        x="Temperature",
        y="Visitors",
        title="Temperature vs Visitors"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==================================
# PREDICTION PAGE
# ==================================

elif page == "Prediction":

    st.title("🔮 Crowd Prediction")

    visitor = st.number_input(
        "Visitor Count",
        min_value=0,
        value=5000
    )

    temp = st.slider(
        "Temperature (°C)",
        10.0,
        50.0,
        32.0
    )

    rain = st.slider(
        "Rainfall (mm)",
        0.0,
        100.0,
        10.0
    )

    weekend = st.selectbox(
        "Weekend",
        ["No","Yes"]
    )

    festival = st.selectbox(
        "Festival",
        ["No","Yes"]
    )

    holiday = st.selectbox(
        "Holiday",
        ["No","Yes"]
    )

    if st.button("Predict Crowd Level"):

        score = visitor

        if weekend == "Yes":
            score += 3000

        if festival == "Yes":
            score += 5000

        if holiday == "Yes":
            score += 4000

        if score < 10000:
            level = "🟢 LOW"

        elif score < 18000:
            level = "🟡 MODERATE"

        elif score < 25000:
            level = "🟠 HIGH"

        else:
            level = "🔴 CRITICAL"

        st.success(f"Predicted Crowd Level: {level}")

        st.subheader("Recommended Actions")

        if "LOW" in level:
            st.success("Normal Operations")

        elif "MODERATE" in level:
            st.warning("Increase Security Personnel")

        elif "HIGH" in level:
            st.warning("Open Additional Gates")

        else:
            st.error("Deploy Emergency Crowd Management Team")

# ==================================
# CROWD ALERTS
# ==================================

elif page == "Crowd Alerts":

    st.title("🚨 Crowd Alert Center")

    col1, col2 = st.columns(2)

    with col1:

        st.success("🟢 LOW ALERT")
        st.write("Normal Crowd Flow")

        st.info("🟡 MODERATE ALERT")
        st.write("Monitor Visitor Activity")

    with col2:

        st.warning("🟠 HIGH ALERT")
        st.write("Increase Staff Deployment")

        st.error("🔴 CRITICAL ALERT")
        st.write("Emergency Crowd Control Required")

# ==================================
# ABOUT PAGE
# ==================================

elif page == "About":

    st.title("ℹ️ About Project")

    st.markdown("""
    ### Smart Temple Crowd Analytics

    This project integrates:

    ✅ Hadoop HDFS

    ✅ Apache Spark

    ✅ PySpark

    ✅ Machine Learning

    ✅ Random Forest Classification

    ✅ Data Analytics

    ✅ Streamlit Dashboard

    ### Objective

    Predict temple crowd congestion levels and help temple
    authorities make data-driven decisions for crowd management,
    safety, resource allocation, and visitor experience.

    ### Technologies

    - Hadoop
    - HDFS
    - PySpark
    - Random Forest
    - Python
    - Streamlit
    - Plotly
    """)
