import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import shap
from traffic_sim import generate_traffic

# Page Config
st.set_page_config(page_title="Sentinel-IoT Dashboard", layout="wide")

# Title
st.title(" Sentinel-IoT: Zero-Day Attack Detection")
st.markdown("**Status:** System Active | **Model:** Isolation Forest (Unsupervised)")

# Load Model
@st.cache_resource
def load_model():
    try:
        return joblib.load('models/isolation_forest.pkl')
    except:
        return None

model = load_model()

# Sidebar
st.sidebar.header("Control Panel")
simulation_mode = st.sidebar.checkbox("Run Real-Time Simulation", value=False)

if model is None:
    st.error("Model not found! Please run 'model_train.py' first.")
else:
    # Generate mock live data
    if simulation_mode:
        data = generate_traffic(n_samples=1, anomaly_ratio=0.2) # Single packet
        
        # Display Metrics
        col1, col2, col3 = st.columns(3)
        
        packet_size = data['packet_size'].values[0]
        interval = data['time_interval'].values[0]
        
        col1.metric("Packet Size", f"{packet_size:.2f} bytes")
        col2.metric("Time Interval", f"{interval:.4f} ms")
        
        # Prediction
        features = ['packet_size', 'time_interval', 'protocol', 'dest_port']
        prediction = model.predict(data[features])[0] # 1 is normal, -1 is anomaly
        score = model.decision_function(data[features])[0]
        
        col3.metric("Anomaly Score", f"{score:.4f}")
        
        # Alert Logic
        if prediction == -1:
            st.error(" ANOMALY DETECTED! Potential Botnet Activity.")
            
            # Explainability Section (SHAP)
            st.subheader(" Attack Analysis (Why was this blocked?)")
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(data[features])
            
            # Visualize
            st_shap(shap.force_plot(explainer.expected_value, shap_values, data[features]), height=150)
            
        else:
            st.success(" Traffic Normal")
            
    else:
        st.info("Check the box in the sidebar to start live monitoring.")

    # Historical View (Static for MVP)
    st.divider()
    st.subheader(" Network Traffic Overview")
    hist_data = generate_traffic(200)
    st.line_chart(hist_data['packet_size'])
