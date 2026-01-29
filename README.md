# Sentinel-IoT: Zero-Day Botnet Detection Framework

Sentinel-IoT is an Explainable AI (XAI) framework designed to detect Zero-Day IoT botnet attacks using Isolation Forests and SHAP (SHapley Additive exPlanations).  
It applies unsupervised learning to identify anomalous network behavior without relying on predefined attack signatures.

This project targets critical security gaps in Kenya’s rapidly expanding IoT infrastructure, where traditional signature-based firewalls fail against unknown threats.

---

##  Project Overview

Traditional intrusion detection systems depend on known attack signatures, making them ineffective against new and evolving threats.  
Sentinel-IoT introduces an unsupervised anomaly detection pipeline capable of identifying previously unseen attacks in IoT network traffic while providing explainable insights for security analysts.

---

##  Key Features

- Real-Time Anomaly Detection using Isolation Forest
- Explainable AI with SHAP-based feature contribution analysis
- Edge-Ready design optimized for low-resource devices (IoT Gateways, Raspberry Pi)
- Unsupervised learning approach with no dependency on labeled attack data
- Interactive Streamlit dashboard for visualization and monitoring

---

##  System Architecture


Network Traffic → Feature Extraction → Isolation Forest Model → Anomaly Detection → SHAP Explanation → Dashboard Visualization


---

## Repository Structure

SENTINEL-IoT/
- data/ # Simulated PCAP/CSV datasets
- models/ # Serialized model files (.pkl)
-  src/
-  pp.py # Streamlit Dashboard Entry Point
-  odel_train.py # Model Training Script
-  raffic_sim.py # Live Traffic Simulator
-  requirements.txt # Python Dependencies
-  EADME.md # Project Documentation


---

## Getting Started

### Prerequisites

- Python 3.8+
- Streamlit
- Scikit-learn

### Installation

Clone the repository:

```
git clone https://github.com/DUTDENG911/SENTINEL-IoT.git
cd SENTINEL-IoT
```
Install dependencies:

- pip install -r requirements.txt

Run the dashboard:

- streamlit run src/app.py

## Technical Roadmap

| Phase   | Description                                       | Status      |
| ------- | ------------------------------------------------- | ----------- |
| Phase 1 | Model Training & Validation (90% Recall achieved) | Completed   |
| Phase 2 | Dashboard & Visualization                         | In Progress |
| Phase 3 | Edge Deployment Optimization                      | Planned     |

## Model Performance (Sample Metrics)

- Recall: 90%

- Precision: 87%

- F1-Score: 88%

Metrics based on simulated IoT network traffic.

## Technologies Used

- Python

- Scikit-learn

- SHAP

- Streamlit

- Pandas & NumPy

- Network Traffic Simulation (PCAP/CSV)

## Team

Dut Deng — Lead Developer & Project Lead

## Hackathon Submission

Submitted to the NIRU AI Hackathon 2026.
