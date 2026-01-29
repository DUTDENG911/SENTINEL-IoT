import pandas as pd
import numpy as np
import time

def generate_traffic(n_samples=1000, anomaly_ratio=0.1):
    """
    Generates synthetic IoT network traffic data.
    Features: Packet Size, Time Interval, Protocol (mapped to int), Source Port
    """
    # 1. Normal Traffic (e.g., Temperature sensors sending small, regular packets)
    n_normal = int(n_samples * (1 - anomaly_ratio))
    
    # Normal: Small packets (40-64 bytes), Regular intervals
    normal_data = {
        'packet_size': np.random.normal(loc=50, scale=10, size=n_normal),
        'time_interval': np.random.exponential(scale=1.0, size=n_normal),
        'protocol': np.random.choice([0, 1], size=n_normal), # 0=MQTT, 1=CoAP
        'dest_port': np.random.choice([80, 443, 8080], size=n_normal)
    }
    
    # 2. Anomalous Traffic (Botnet DDoS or Scanning)
    n_anomaly = n_samples - n_normal
    
    # Anomaly: Huge packets (DDoS) or tiny rapid ones (Scanning)
    anomaly_data = {
        'packet_size': np.random.normal(loc=1500, scale=200, size=n_anomaly),
        'time_interval': np.random.exponential(scale=0.01, size=n_anomaly), # Very fast
        'protocol': np.random.choice([2, 3], size=n_anomaly), # Unknown protocols
        'dest_port': np.random.randint(1024, 65535, size=n_anomaly) # Random high ports
    }
    
    # Combine
    df_normal = pd.DataFrame(normal_data)
    df_normal['label'] = 0 # Normal
    
    df_anomaly = pd.DataFrame(anomaly_data)
    df_anomaly['label'] = 1 # Attack
    
    df = pd.concat([df_normal, df_anomaly]).sample(frac=1).reset_index(drop=True)
    
    # Add timestamps
    df['timestamp'] = pd.date_range(start=pd.Timestamp.now(), periods=n_samples, freq='S')
    
    return df

if __name__ == "__main__":
    print("Generating synthetic network traffic...")
    df = generate_traffic(2000)
    df.to_csv("data/network_traffic.csv", index=False)
    print("Saved to data/network_traffic.csv")
