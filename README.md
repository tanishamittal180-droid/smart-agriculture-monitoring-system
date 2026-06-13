# 🌱 AgriSense AI – Digital Twin Smart Agriculture Monitoring System

## 📌 Project Overview

AgriSense AI is an AI-powered Digital Twin Smart Agriculture Monitoring System developed using Python, Streamlit, SQLite, Plotly, and Machine Learning.

The project simulates a real farm environment by generating virtual IoT sensor data, monitoring environmental conditions, automating irrigation decisions, predicting crop yield using Machine Learning, and providing a real-time interactive dashboard.

The system acts as a Digital Twin of a physical farm where users can monitor, analyze, predict, and control farm operations through a game-like interface.

---

# 🎯 Objectives

* Monitor farm conditions in real time
* Simulate IoT sensor readings
* Automate irrigation decisions
* Generate alerts for abnormal conditions
* Predict crop yield using Machine Learning
* Visualize farm operations through a Digital Twin dashboard
* Provide interactive farm controls
* Support data analytics and reporting

---

# 🚀 Key Features

## 🌡 Environmental Monitoring

* Temperature Monitoring
* Humidity Monitoring
* Soil Moisture Monitoring
* Water Tank Monitoring
* Light Intensity Monitoring

## 🚿 Smart Irrigation System

* Automatic Pump ON/OFF Logic
* Soil Moisture-Based Irrigation
* Water Tank Monitoring
* Irrigation Alerts

## 🌱 Digital Twin Simulation

* Virtual Farm Environment
* Crop Growth Simulation
* Weather Simulation
* Day/Night Cycle
* Animated Farm Visualization
* Real-Time Sensor Simulation

## 🤖 Artificial Intelligence

### Crop Yield Prediction

Uses Machine Learning to predict crop yield based on:

* Soil Moisture
* Temperature
* Humidity
* Water Tank Level

### AI Recommendation Engine

Provides recommendations such as:

* Increase Irrigation
* Refill Water Tank
* Heat Stress Detection
* Optimal Farm Conditions

## 📊 Data Analytics

* Average Temperature Analysis
* Average Humidity Analysis
* Average Soil Moisture Analysis
* Pump Usage Analysis
* Farm Health Score
* Historical Data Analysis

## 📈 Interactive Dashboard

* Live Monitoring
* Plotly Interactive Charts
* Farm Analytics
* Prediction Dashboard
* Alert Center
* Report Generation

## 🎮 Farm Game Mode

### Features

* Start Simulation Button
* Stop Simulation Button
* Manual Sensor Controls
* Animated Water Flow
* Crop Growth Animation
* Farm Health Meter
* Interactive Farm Controls

Users can control:

* Soil Moisture
* Temperature
* Humidity

in real time through sliders.

---

# 🏗 System Architecture

```text
Virtual Sensors
       │
       ▼
Farm Simulator
       │
       ▼
SQLite Database
       │
       ▼
Analytics Engine
       │
       ├────────► Alert Engine
       │
       ├────────► ML Prediction
       │
       └────────► Streamlit Dashboard
```

---

# 📂 Project Structure

```text
AgriSense-AI/

├── dashboard/
│   └── dashboard.py
│
├── database/
│   ├── farm_data.db
│   └── database_manager.py
│
├── simulation/
│   ├── farm_simulator.py
│   ├── crop_growth.py
│   ├── weather_effect.py
│   ├── day_night.py
│   └── farm_visualizer.py
│
├── farm_analytics/
│   ├── __init__.py
│   └── analytics_engine.py
│
├── ml_model/
│   ├── train_model.py
│   ├── predict_yield.py
│   ├── crop_yield_model.pkl
│   └── farm_training_data.csv
│
├── ai/
│   └── recommendation_engine.py
│
├── alerts/
│   └── alert_manager.py
│
├── weather/
│   ├── weather_service.py
│   └── rain_predictor.py
│
├── reports/
│   └── report_generator.py
│
├── notifications/
│   └── email_alert.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🛠 Technologies Used

### Programming Language

* Python

### Database

* SQLite

### Dashboard

* Streamlit

### Data Visualization

* Plotly

### Machine Learning

* Scikit-Learn
* Random Forest Regressor

### Data Processing

* Pandas
* NumPy

### Reporting

* ReportLab

### APIs

* Open-Meteo Weather API

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/agrisense-ai.git
```

## Move into Project Folder

```bash
cd agrisense-ai
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run Project

## Start Simulation

```bash
python main.py
```

## Run Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

# 📈 Machine Learning Model

### Algorithm Used

Random Forest Regressor

### Input Features

* Soil Moisture
* Temperature
* Humidity
* Water Tank Level

### Output

Predicted Crop Yield (%)

---

# 📊 Dashboard Modules

## Dashboard

* Live Sensor Monitoring
* Alert Center
* Pump Monitoring

## Virtual Farm

* Digital Twin View
* Crop Growth Stage
* Weather Status

## Analytics

* Historical Trends
* Interactive Charts
* Farm Health Analysis

## Predictions

* Crop Yield Prediction
* AI Recommendations

## Reports

* CSV Download
* Historical Records



# 🔮 Future Enhancements

* Real IoT Sensor Integration
* ESP32 Support
* Arduino Support
* MQTT Communication
* Mobile Application
* Cloud Deployment
* Drone Monitoring
* Satellite Data Integration
* Computer Vision Crop Detection
* Disease Detection Using Deep Learning

# screenshots
<img width="1366" height="768" alt="Screenshot 2026-06-13 124946" src="https://github.com/user-attachments/assets/a6c26193-f27e-4a21-a860-bb35abb58fb3" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125001" src="https://github.com/user-attachments/assets/a9d0ad3a-29d3-4845-95c5-4101a6343f72" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125042" src="https://github.com/user-attachments/assets/e288b942-bdc5-4575-8f8e-914e0d7fc0e8" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125057" src="https://github.com/user-attachments/assets/bb37f7d4-99f9-4839-80b0-0b538cc6fa8a" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125107" src="https://github.com/user-attachments/assets/47073e71-2d6c-4491-855a-798734289736" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125119" src="https://github.com/user-attachments/assets/62f4ab4e-3ece-4e7f-a2aa-1cb2124218ab" />

# 🎓 Learning Outcomes

* Internet of Things (IoT)
* Digital Twin Systems
* Smart Agriculture
* Machine Learning
* Data Analytics
* Database Management
* Dashboard Development
* Predictive Analytics
* Automation Systems
* Software Engineering


# 👩‍💻 Author

**Tanisha Mittal**

B.Tech Electronics and Communication Engineering

AI • IoT • Machine Learning • Data Analytics


# 📄 License

This project is developed for educational, research, internship, and academic purposes.


# ⭐ Resume Project Title

**AI-Powered Digital Twin Smart Agriculture Monitoring and Predictive Analytics System**

### Tech Stack

Python, Streamlit, SQLite, Plotly, Scikit-Learn, Machine Learning, Digital Twin Simulation, Data Analytics, IoT Concepts.
