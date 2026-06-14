import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Temple Crowd Analytics",
    page_icon="🛕",
    layout="wide"
)

st.title("🛕 Smart Temple Crowd Analytics")
st.markdown("### Big Data Project using Hadoop, PySpark & Machine Learning")

st.write("""
This project analyzes temple visitor data and predicts crowd congestion levels.
""")

st.subheader("Project Features")

st.markdown("""
- Hadoop HDFS Storage
- PySpark Data Processing
- Feature Engineering
- Random Forest Prediction
- Crowd Congestion Analysis
- Interactive Dashboard
""")

st.subheader("Technology Stack")

tech = pd.DataFrame({
    "Technology":["Hadoop","PySpark","Machine Learning","Streamlit","Docker"],
    "Purpose":[
        "Distributed Storage",
        "Data Processing",
        "Prediction",
        "Dashboard",
        "Containerization"
    ]
})

st.dataframe(tech,use_container_width=True)

st.success("Project Successfully Deployed 🚀")
