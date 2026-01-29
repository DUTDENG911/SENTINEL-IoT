import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os
from traffic_sim import generate_traffic

# Ensure directories exist
if not os.path.exists('models'):
    os.makedirs('models')
if not os.path.exists('data'):
    os.makedirs('data')

def train_model():
    print("Step 1: Generating Training Data...")
    # Generate 5000 packets for training
    df = generate_traffic(n_samples=5000, anomaly_ratio=0.05)
    
    # Features to train on (exclude timestamp and label)
    features = ['packet_size', 'time_interval', 'protocol', 'dest_port']
    X = df[features]
    
    print("Step 2: Training Isolation Forest...")
    # Isolation Forest setup
    # contamination=0.05 means we expect roughly 5% anomalies
    iso_forest = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    iso_forest.fit(X)
    
    print("Step 3: Saving Model...")
    joblib.dump(iso_forest, 'models/isolation_forest.pkl')
    print("Model saved to models/isolation_forest.pkl")

if __name__ == "__main__":
    train_model()
