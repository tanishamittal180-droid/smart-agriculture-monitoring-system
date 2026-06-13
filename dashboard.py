import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import numpy as np
import random
import time
import joblib
import os
from datetime import datetime

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="🌱 AgriSense AI Ultimate",
    page_icon="🌱",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.metric-card {
    background:#1e293b;
    padding:15px;
    border-radius:15px;
    text-align:center;
}

.big-title{
    text-align:center;
    color:#22c55e;
    font-size:40px;
    font-weight:bold;
}

.live{
    color:#22c55e;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# LOGIN SYSTEM
# ==================================================

USERS = {
    "admin": "admin123",
    "farmer": "farmer123"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.markdown(
        "<h1 class='big-title'>🌱 AgriSense AI Login</h1>",
        unsafe_allow_html=True
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if USERS.get(username) == password:

            st.session_state.logged_in = True
            st.rerun()

        else:

            st.error("Invalid Credentials")

    st.stop()

# ==================================================
# DATABASE PATH
# ==================================================

DB_FOLDER = "database"

os.makedirs(
    DB_FOLDER,
    exist_ok=True
)

DB_PATH = os.path.join(
    DB_FOLDER,
    "farm_data.db"
)

# ==================================================
# CREATE DATABASE
# ==================================================

def create_database():

    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS sensor_data(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        soil_moisture REAL,

        temperature REAL,

        humidity REAL,

        water_tank REAL,

        light_intensity REAL,

        pump_status TEXT,

        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()
    conn.close()

create_database()

# ==================================================
# LIVE SENSOR GENERATOR
# ==================================================

def generate_sensor_data():

    return {

        "soil_moisture":
        round(
            random.uniform(35,90),
            2
        ),

        "temperature":
        round(
            random.uniform(20,45),
            2
        ),

        "humidity":
        round(
            random.uniform(40,90),
            2
        ),

        "water_tank":
        round(
            random.uniform(20,100),
            2
        ),

        "light_intensity":
        round(
            random.uniform(200,900),
            2
        ),

        "pump_status":
        random.choice(
            ["ON","OFF"]
        )
    }

# ==================================================
# INSERT SENSOR DATA
# ==================================================

def insert_sensor_data():

    data = generate_sensor_data()

    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()

    cur.execute("""
    INSERT INTO sensor_data(

        soil_moisture,
        temperature,
        humidity,
        water_tank,
        light_intensity,
        pump_status

    )
    VALUES(?,?,?,?,?,?)
    """,

    (

        data["soil_moisture"],
        data["temperature"],
        data["humidity"],
        data["water_tank"],
        data["light_intensity"],
        data["pump_status"]

    ))

    conn.commit()
    conn.close()

# ==================================================
# AUTO GENERATE DATA
# ==================================================

if "last_insert" not in st.session_state:

    st.session_state.last_insert = time.time()

if time.time() - st.session_state.last_insert > 5:

    insert_sensor_data()

    st.session_state.last_insert = time.time()

# ==================================================
# LOAD DATA
# ==================================================

@st.cache_data(ttl=2)
def load_data():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        """
        SELECT *
        FROM sensor_data
        ORDER BY id DESC
        """,
        conn
    )

    conn.close()

    return df

# ==================================================
# FIRST RECORD IF DB EMPTY
# ==================================================

df = load_data()

if len(df) == 0:

    for _ in range(10):
        insert_sensor_data()

    df = load_data()

latest = df.iloc[0]

# ==================================================
# FARM HEALTH SCORE
# ==================================================

def farm_health(row):

    score = (
        row["soil_moisture"]
        +
        row["humidity"]
        +
        row["water_tank"]
        +
        (100 - abs(row["temperature"]-25))
    ) / 4

    return round(
        min(score,100),
        2
    )

health_score = farm_health(latest)

# ==================================================
# NDVI INDEX
# ==================================================

def ndvi_index(row):

    ndvi = (
        row["soil_moisture"]/100
    ) * 0.6 + (
        1 - abs(
            row["temperature"]-25
        )/50
    ) * 0.4

    return round(
        ndvi,
        2
    )

ndvi = ndvi_index(latest)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title(
    "🌱 AgriSense AI"
)

page = st.sidebar.radio(

    "Navigation",

    [

        "Dashboard",
        "Analytics",
        "Predictions",
        "AI Assistant",
        "Multi Farm",
        "Reports"

    ]
)

if st.sidebar.button("Logout"):

    st.session_state.logged_in = False

    st.rerun()
    # ==================================================
# WEATHER SIMULATION
# ==================================================

def get_weather():

    weather_types = [
        "Sunny ☀️",
        "Cloudy ☁️",
        "Rainy 🌧️",
        "Windy 🌬️"
    ]

    return random.choice(weather_types)

weather = get_weather()

# ==================================================
# ALERT ENGINE
# ==================================================

alerts = []

if latest["soil_moisture"] < 40:
    alerts.append("🚨 Low Soil Moisture")

if latest["temperature"] > 40:
    alerts.append("🔥 High Temperature")

if latest["water_tank"] < 25:
    alerts.append("💧 Low Water Tank")

if latest["humidity"] < 45:
    alerts.append("🌾 Low Humidity")

# ==================================================
# MANUAL CONTROL STATE
# ==================================================

if "manual_pump" not in st.session_state:
    st.session_state.manual_pump = latest["pump_status"]

# ==================================================
# DASHBOARD PAGE
# ==================================================

if page == "Dashboard":

    st.markdown(
        "<h1 class='big-title'>🌱 AgriSense AI Control Center</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='live'>🟢 LIVE FARM MONITORING</p>",
        unsafe_allow_html=True
    )

    # ============================================
    # TOP STATUS
    # ============================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🌿 Farm Health",
            f"{health_score}%"
        )

    with col2:

        st.metric(
            "🛰 NDVI Index",
            ndvi
        )

    with col3:

        st.metric(
            "🌦 Weather",
            weather
        )

    st.divider()

    # ============================================
    # SENSOR CARDS
    # ============================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🌱 Soil Moisture",
        f"{latest['soil_moisture']}%"
    )

    c2.metric(
        "🌡 Temperature",
        f"{latest['temperature']}°C"
    )

    c3.metric(
        "💧 Humidity",
        f"{latest['humidity']}%"
    )

    c4.metric(
        "🚰 Water Tank",
        f"{latest['water_tank']}%"
    )

    st.divider()

    # ============================================
    # ALERT PANEL
    # ============================================

    st.subheader("🚨 Alert Center")

    if len(alerts) == 0:

        st.success(
            "No Active Alerts"
        )

    else:

        for alert in alerts:

            st.error(alert)

    st.divider()

    # ============================================
    # MANUAL FARM CONTROL
    # ============================================

    st.subheader("🎮 Farm Control Panel")

    cc1, cc2 = st.columns(2)

    with cc1:

        if st.button("🚿 Turn Pump ON"):

            st.session_state.manual_pump = "ON"

    with cc2:

        if st.button("⛔ Turn Pump OFF"):

            st.session_state.manual_pump = "OFF"

    st.info(
        f"Current Pump Status: {st.session_state.manual_pump}"
    )

    st.divider()

    # ============================================
    # SENSOR OVERRIDE
    # ============================================

    st.subheader("⚙️ Manual Sensor Override")

    manual_soil = st.slider(
        "Soil Moisture",
        0,
        100,
        int(latest["soil_moisture"])
    )

    manual_temp = st.slider(
        "Temperature",
        0,
        50,
        int(latest["temperature"])
    )

    manual_humidity = st.slider(
        "Humidity",
        0,
        100,
        int(latest["humidity"])
    )

    if st.button("Apply Virtual Settings"):

        st.success(
            "Simulation Settings Applied"
        )

    st.divider()

    # ============================================
    # LIVE CHARTS
    # ============================================

    st.subheader("📈 Live Analytics")

    chart_df = df.sort_values("id")

    fig1 = px.line(
        chart_df,
        x="id",
        y="soil_moisture",
        title="Soil Moisture Trend"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    fig2 = px.line(
        chart_df,
        x="id",
        y="temperature",
        title="Temperature Trend"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    fig3 = px.line(
        chart_df,
        x="id",
        y="humidity",
        title="Humidity Trend"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    fig4 = px.line(
        chart_df,
        x="id",
        y="water_tank",
        title="Water Tank Trend"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    # ============================================
    # LAST UPDATE
    # ============================================

    st.caption(
        f"Last Updated : {datetime.now().strftime('%H:%M:%S')}"
    )
    # ==================================================
# AI RECOMMENDATION ENGINE
# ==================================================

def generate_recommendations(row):

    recommendations = []

    if row["soil_moisture"] < 40:
        recommendations.append(
            "💧 Soil moisture is low. Consider irrigation."
        )

    if row["temperature"] > 40:
        recommendations.append(
            "🌡 Temperature is high. Protect crops from heat stress."
        )

    if row["water_tank"] < 30:
        recommendations.append(
            "🚰 Refill water tank soon."
        )

    if row["humidity"] < 50:
        recommendations.append(
            "🌾 Low humidity detected."
        )

    if len(recommendations) == 0:

        recommendations.append(
            "✅ Farm conditions are healthy."
        )

    return recommendations

# ==================================================
# RISK FORECAST ENGINE
# ==================================================

def future_risk_forecast():

    forecast = []

    base = health_score

    for hour in range(1, 7):

        value = max(
            0,
            min(
                100,
                base + random.randint(-10, 10)
            )
        )

        forecast.append(
            {
                "Hour": f"+{hour}h",
                "Health": value
            }
        )

    return pd.DataFrame(forecast)

# ==================================================
# AI ASSISTANT PAGE
# ==================================================

if page == "AI Assistant":

    st.title("🤖 AgriSense AI Assistant")

    st.subheader(
        "Ask Questions About Your Farm"
    )

    query = st.text_input(
        "Type your question"
    )

    if query:

        query = query.lower()

        if "water" in query:

            if latest["soil_moisture"] < 40:

                st.warning(
                    "Yes. Soil moisture is low."
                )

            else:

                st.success(
                    "Soil moisture is sufficient."
                )

        elif "temperature" in query:

            st.info(
                f"Current temperature is {latest['temperature']}°C"
            )

        elif "humidity" in query:

            st.info(
                f"Current humidity is {latest['humidity']}%"
            )

        elif "yield" in query:

            st.success(
                "Check Prediction page for crop yield."
            )

        elif "health" in query:

            st.success(
                f"Farm Health Score : {health_score}%"
            )

        elif "ndvi" in query:

            st.success(
                f"NDVI Index : {ndvi}"
            )

        else:

            st.info(
                "Try asking about water, temperature, humidity, health, yield, or NDVI."
            )

    st.divider()

    st.subheader("🤖 AI Recommendations")

    recs = generate_recommendations(
        latest
    )

    for rec in recs:

        st.info(rec)

# ==================================================
# CROP YIELD PREDICTION PAGE
# ==================================================

elif page == "Predictions":

    st.title(
        "🌾 AI Crop Yield Prediction"
    )

    prediction = round(

        (
            latest["soil_moisture"] * 0.30
            +
            latest["humidity"] * 0.20
            +
            latest["water_tank"] * 0.30
            +
            (
                100
                -
                abs(
                    latest["temperature"] - 25
                )
            ) * 0.20
        ),

        2
    )

    st.metric(
        "Predicted Yield",
        f"{prediction}%"
    )

    if prediction > 85:

        st.success(
            "🌱 Excellent Yield Expected"
        )

    elif prediction > 70:

        st.warning(
            "🌾 Moderate Yield Expected"
        )

    else:

        st.error(
            "⚠ Poor Yield Expected"
        )

    st.divider()

    st.subheader(
        "📈 Future Farm Health Forecast"
    )

    forecast_df = future_risk_forecast()

    fig = px.line(
        forecast_df,
        x="Hour",
        y="Health",
        markers=True,
        title="6 Hour Forecast"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==================================================
# MULTI FARM INTELLIGENCE PAGE
# ==================================================

elif page == "Multi Farm":

    st.title(
        "🌐 Multi-Farm Intelligence"
    )

    farm_a = health_score

    farm_b = round(
        health_score - random.randint(5, 15),
        2
    )

    farm_c = round(
        health_score + random.randint(-5, 10),
        2
    )

    farms = pd.DataFrame({

        "Farm": [

            "Farm A",
            "Farm B",
            "Farm C"

        ],

        "Health Score": [

            farm_a,
            farm_b,
            farm_c

        ]

    })

    st.dataframe(
        farms,
        use_container_width=True
    )

    fig = px.bar(

        farms,

        x="Farm",

        y="Health Score",

        title="Farm Comparison"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    best_farm = farms.loc[
        farms["Health Score"].idxmax()
    ]

    st.success(
        f"🏆 Best Performing Farm : {best_farm['Farm']}"
    )

# ==================================================
# ADVANCED NDVI ANALYSIS
# ==================================================

elif page == "NDVI Analysis":

    st.title(
        "🛰 Satellite NDVI Analysis"
    )

    st.metric(
        "Current NDVI",
        ndvi
    )

    st.progress(
        int(ndvi * 100)
    )

    if ndvi > 0.75:

        st.success(
            "Excellent Crop Health"
        )

    elif ndvi > 0.50:

        st.warning(
            "Moderate Crop Health"
        )

    else:

        st.error(
            "Poor Crop Health"
        )

    ndvi_history = []

    for i in range(20):

        ndvi_history.append(
            {
                "Day": i + 1,
                "NDVI": round(
                    random.uniform(
                        0.3,
                        0.9
                    ),
                    2
                )
            }
        )

    ndvi_df = pd.DataFrame(
        ndvi_history
    )

    fig = px.line(

        ndvi_df,

        x="Day",

        y="NDVI",

        title="NDVI History"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "Predictions",
        "AI Assistant",
        "Multi Farm",
        "Reports",
        "Farm Game"
    ]
)