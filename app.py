import streamlit as st
import tarfile
from pyspark.ml.classification import RandomForestClassificationModel

# Extract model only if folder doesn't exist
import os

if not os.path.exists("rf_model"):
    with tarfile.open("rf_model.tar") as tar:
        tar.extractall()

# Load model
model = RandomForestClassificationModel.load("rf_model")

st.title("🛕 Smart Temple Crowd Analytics")
st.write("Model loaded successfully!")
