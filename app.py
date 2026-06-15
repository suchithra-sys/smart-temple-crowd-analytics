import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

st.set_page_config(
page_title="Smart Temple Crowd Analytics",
page_icon="🏛",
layout="wide"
)

# -----------------------------

# Sidebar

# -----------------------------

st.sidebar.title("🏛 Navigation")
page = st.sidebar.radio(
"Select Page",
["Home", "Analytics", "Prediction", "Crowd Alerts", "About"]
)

# -----------------------------

# Home Page

# -----------------------------

if page == "Home":

```
st.title("🏛 Smart Temple Crowd Analytics")
st.subheader("Temple Crowd Prediction & Management Dashboard")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Temples", "1,250")
c2.metric("Total Visitors", "2.4 M")
c3.metric("High Crowd Alerts", "185")
c4.metric("Model Accuracy", "94%")

st.markdown("---")

st.info(
    """
    Smart Temple Crowd Analytics uses Big Data and Machine Learning
    to predict temple congestion levels and assist authorities
    in crowd management and resource planning.
    """
)

chart_data = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Visitors":[12000,15000,18000,22000,25000,30000]
})

fig = px.line(
    chart_data,
    x="Month",
    y="Visitors",
    title="Monthly Visitor Trend"
)

st.plotly_chart(fig, use_container_width=True)
```

# -----------------------------

# Analytics Page

# -----------------------------

elif page == "Analytics":

```
st.title("📊 Analytics Dashboard")

col1, col2 = st.columns(2)

with col1:

    crowd = pd.DataFrame({
        "Level":["Low","Moderate","High","Critical"],
        "Count":[1200,3500,2200,900]
    })

    fig = px.pie(
        crowd,
        names="Level",
        values="Count",
        title="Crowd Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    feature = pd.DataFrame({
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
            0.06,
            0.04,
            0.02
        ]
    })

    fig = px.bar(
        feature,
        x="Feature",
        y="Importance",
        title="Feature Importance"
    )

    st.plotly_chart(fig, use_container_width=True)
```

# -----------------------------

# Prediction Page

# -----------------------------

elif page == "Prediction":

```
st.title("🔮 Temple Crowd Prediction")

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
    "Precipitation (mm)",
    0.0,
    100.0,
    20.0
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

    if visitor < 6000:
        level = "🟢 Low"

    elif visitor < 12000:
        level = "🟡 Moderate"

    elif visitor < 20000:
        level = "🟠 High"

    else:
        level = "🔴 Critical"

    st.success(f"Predicted Congestion Level : {level}")

    st.subheader("Recommendations")

    st.write("✓ Increase Security Personnel")
    st.write("✓ Manage Entry Gates")
    st.write("✓ Monitor Visitor Flow")
    st.write("✓ Improve Parking Control")
```

# -----------------------------

# Crowd Alerts

# -----------------------------

elif page == "Crowd Alerts":

```
st.title("🚨 Crowd Alert Center")

st.error("🔴 Critical Alert")
st.warning("🟠 High Alert")
st.info("🟡 Moderate Alert")
st.success("🟢 Normal")
```

# -----------------------------

# About

# -----------------------------

elif page == "About":

```
st.title("ℹ About Project")

st.markdown(
    """
    ### Smart Temple Crowd Analytics

    Technologies Used:

    - Hadoop HDFS
    - Apache Spark
    - PySpark
    - Machine Learning
    - Random Forest
    - Streamlit
    - Data Analytics

    Objective:

    Predict temple congestion levels and assist temple authorities
    in crowd management using Big Data technologies.
    """
)
```
