import streamlit as st
import joblib
import numpy as np
import random
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Crop Yield Prediction", layout="wide")

# ==========================================
# SESSION STATE FOR PAGE NAVIGATION
# ==========================================

if "page" not in st.session_state:
    st.session_state.page = "home"

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main {
    background: linear-gradient(135deg,#eefbf0,#f5fff5);
}

/* HOME PAGE */

.home-wrapper {
    animation: homeEntry 1s ease;
}

.home-container {
    background: linear-gradient(135deg,#e8f5e9,#f1f8e9);
    padding: 60px;
    border-radius: 28px;
    margin-top: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.08);
}

/* TITLES */

.home-title {
    text-align: center;
    color: #1b5e20;
    font-size: 60px;
    font-weight: bold;
    margin-bottom: 20px;
}

.home-subtitle {
    text-align: center;
    color: #388e3c;
    font-size: 24px;
    margin-bottom: 40px;
}

/* CONTENT BOX */

.section-box {
    background: rgba(255,255,255,0.88);
    backdrop-filter: blur(10px);
    padding: 30px;
    border-radius: 24px;
    margin-top: 25px;
    border-left: 8px solid #43a047;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
    animation: boxEntry 1s ease;
}

/* TEXT */

.section-title {
    color: #1b5e20;
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 15px;
}

.section-content {
    color: #333;
    font-size: 18px;
    line-height: 1.9;
}

/* BUTTON */

div[data-testid="stButton"] button[kind="secondary"] {
    height: 80px;
    font-size: 32px;
    font-weight: bold;
    border-radius: 22px;
    background: linear-gradient(135deg,#1b5e20,#43a047);
    color: white;
    border: none;
    box-shadow: 0px 8px 20px rgba(46,125,50,0.35);
    transition: 0.3s ease;
}

div[data-testid="stButton"] button[kind="secondary"]:hover {
    transform: scale(1.04);
    background: linear-gradient(135deg,#0d4715,#2e7d32);
    color: white;
}

/* HOME ENTRY */

@keyframes homeEntry {

    from {
        opacity: 0;
        transform: translateX(-120px);
    }

    to {
        opacity: 1;
        transform: translateX(0px);
    }
}

/* BOX ENTRY */

@keyframes boxEntry {

    from {
        opacity: 0;
        transform: translateY(50px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* HOME EXIT */

.slide-out {

    animation: slideOut 0.8s ease forwards;
}

@keyframes slideOut {

    from {
        opacity: 1;
        transform: translateX(0px);
    }

    to {
        opacity: 0;
        transform: translateX(-250px);
    }
}

/* PREDICTION PAGE ENTRY */

.prediction-page {

    animation: predictionEntry 0.8s ease;
}

@keyframes predictionEntry {

    from {
        opacity: 0;
        transform: translateX(250px);
    }

    to {
        opacity: 1;
        transform: translateX(0px);
    }
}

</style>
""", unsafe_allow_html=True)
# ==========================================
# HOME PAGE
# ==========================================

if st.session_state.page == "home":
    st.markdown('<div class="home-wrapper">', unsafe_allow_html=True)
    st.markdown("""
    <div class="home-container">

    <div class="home-title">
    🌾 Crop Yield Prediction System
    </div>

    <div class="home-subtitle">
    AI Based Smart Agriculture Prediction And Recommendation Platform
    </div>
    
    </div>
    """, unsafe_allow_html=True)

    # ABOUT
    st.markdown("""
    <div class="section-box">

    <div class="section-title">
    🌱 About Crop Yield Prediction
    </div>

    <div class="section-content">

    Crop Yield Prediction is an Artificial Intelligence based agricultural system
    used to estimate crop production using environmental and agricultural factors
    such as temperature, rainfall, soil condition, season, and location.

    This system helps farmers identify suitable crops and estimate expected crop
    yield before cultivation using Machine Learning algorithms.

    </div>

    </div>
    """, unsafe_allow_html=True)

    # USES
    st.markdown("""
    <div class="section-box">

    <div class="section-title">
    📈 Uses Of Crop Prediction System
    </div>

    <div class="section-content">

    ✅ Helps farmers choose the best crop.<br><br>

    ✅ Reduces crop loss risks.<br><br>

    ✅ Improves farming productivity.<br><br>

    ✅ Supports smart agriculture decisions.<br><br>

    ✅ Predicts estimated crop production.<br><br>

    ✅ Helps maintain proper irrigation and fertilizer management.

    </div>

    </div>
    """, unsafe_allow_html=True)

    # HOW TO USE
    st.markdown("""
    <div class="section-box">

    <div class="section-title">
    🖥 How To Use The Model
    </div>

    <div class="section-content">

    1️⃣ Select crop type.<br><br>

    2️⃣ Select district/location.<br><br>

    3️⃣ Select season.<br><br>

    4️⃣ System automatically fetches live weather.<br><br>

    5️⃣ Select soil type and land area.<br><br>

    6️⃣ Complete captcha verification.<br><br>

    7️⃣ Click Predict Yield button.<br><br>

    8️⃣ System generates yield prediction and crop recommendation.

    </div>

    </div>
    """, unsafe_allow_html=True)

    # PRECAUTIONS
    st.markdown("""
    <div class="section-box">

    <div class="section-title">
    ⚠ Precautions For Better Crop Yield
    </div>

    <div class="section-content">

    🌧 Maintain proper irrigation.<br><br>

    🌡 Avoid crops unsuitable for temperature conditions.<br><br>

    🌱 Use suitable soil and season combinations.<br><br>

    🧪 Maintain soil nutrients and pH balance.<br><br>

    🐛 Monitor pests and diseases regularly.<br><br>

    🚜 Use balanced fertilizers and modern farming techniques.

    </div>

    </div>
    """, unsafe_allow_html=True)

    # NEXT BUTTON
    st.markdown('<div class="next-btn">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,3,1])

    with col2:
        next_clicked = st.button(
            "➡ Next - Open Crop Yield Prediction",
            key="next_button"
        )

    if next_clicked:
    
        st.markdown("""
        <script>
        const elements = window.parent.document.querySelectorAll('.home-wrapper');
        elements.forEach(el => {
            el.classList.add('slide-out');
        });
        </script>
        """, unsafe_allow_html=True)
    
        import time
        time.sleep(0.7)
    
        st.session_state.page = "prediction"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "prediction":

    st.markdown('<div class="prediction-page">', unsafe_allow_html=True)

    # BACK BUTTON
    col1, col2, col3 = st.columns([1, 1.2, 6])

    with col1:
        back_btn = st.button("⬅ Back", key="back_btn")

    if back_btn:
        st.session_state.page = "home"
        st.rerun()
    # ==========================================
    # PREDICTION PAGE TITLE
    # ==========================================

    st.markdown("""
    <h1 style='text-align: center; color: #1b5e20; font-size: 42px; margin-bottom: 10px;'>
        Crop Yield Prediction
    </h1>
    <p style='text-align: center; color: #388e3c; font-size: 18px; margin-bottom: 30px;'>
        Enter crop and land details to predict crop yield
    </p>
    """, unsafe_allow_html=True)

    API_KEY = "686c735583837cebe3550948176fdbcc"
    
    def get_weather(city):
    
        city_alias = {
    
            "Hyderabad": "Hyderabad",
            "Warangal": "Warangal",
            "Karimnagar": "Karimnagar",
            "Nizamabad": "Nizamabad",
            "Khammam": "Khammam",
            "Adilabad": "Adilabad",
    
            "Mahabubnagar": "Mahbubnagar",
    
            "Medak": "Medak",
    
            "Rangareddy": "Hyderabad",
    
            "Siddipet": "Siddipet",
    
            "Suryapet": "Suryapet",
    
            "Nalgonda": "Nalgonda",
    
            "Jagtial": "Jagitial",
    
            "Peddapalli": "Peddapalle",
    
            "Mancherial": "Mancherial",
    
            "Sangareddy": "Sangareddy",
    
            "Kamareddy": "Kamareddy",
    
            "Wanaparthy": "Wanaparthy",
    
            "Nagarkurnool": "Nagarkurnool"
        }
    
        try:
    
            api_city = city_alias.get(city, city)
    
            url = f"https://api.openweathermap.org/data/2.5/weather?q={api_city},IN&appid={API_KEY}&units=metric"
    
            response = requests.get(url).json()
    
            if response.get("cod") != 200:
                return 28.0, 0.0
    
            temp = response["main"]["temp"]
    
            rain = response.get("rain", {}).get("1h", 0.0)
    
            return temp, rain
    
        except:
            return 28.0, 0.0
    df = pd.read_csv("final_rainfall_dataset 1.csv")
     #CLEAN district names
    df['district'] = df['district'].str.strip().str.lower()
    expected_rain_df = df.groupby(['district','season'])['rainfall'].mean().reset_index()
    print(expected_rain_df.head())
    print(expected_rain_df['district'].unique())
    # Load Model
    model = joblib.load("model.pkl")
    
    # Language Selection
    language = st.selectbox(
        "Select Language",
        ["English"]
    )
    
    # Crop Names
    crop_names = {
        "English": {
            "Paddy": "Paddy",
            "Wheat": "Wheat",
            "Maize": "Maize",
            "Barley": "Barley"
        }
    }
    
    # Location Names
    location_names = {
        "English": [
            "Select Location",
            "Hyderabad",
            "Warangal",
            "Karimnagar",
            "Nizamabad",
            "Khammam",
            "Adilabad",
            "Mahabubnagar",
            "Medak",
            "Rangareddy",
            "Siddipet",
            "Suryapet",
            "Nalgonda",
            "Jagtial",
            "Peddapalli",
            "Mancherial",
            "Sangareddy",
            "Kamareddy",
            "Wanaparthy",
            "Nagarkurnool"
        ]
    }
    
    # Location Encoding
    location_mapping = {
        "Hyderabad": 0,
        "Warangal": 1,
        "Karimnagar": 2,
        "Nizamabad": 3,
        "Khammam": 4,
        "Adilabad": 5,
        "Mahabubnagar": 6,
        "Medak": 7,
        "Rangareddy": 8,
        "Siddipet": 9,
        "Suryapet": 10,
        "Nalgonda": 11,
        "Jagtial": 12,
        "Peddapalli": 13,
        "Mancherial": 14,
        "Sangareddy": 15,
        "Kamareddy": 16,
        "Wanaparthy": 17,
        "Nagarkurnool": 18
    }
    
    # Soil Type Options
    soil_types = {
        "English": [
            "Select Soil Type",
            "Black Soil",
            "Red Soil",
            "Clay Soil",
            "Sandy Soil",
            "Loamy Soil",
            "Alluvial Soil",
            "Laterite Soil"
        ]
    }
    
    soil_type_mapping = {
        "Black Soil": 1,
        "Red Soil": 2,
        "Clay Soil": 3,
        "Sandy Soil": 4,
        "Loamy Soil": 5,
        "Alluvial Soil": 6,
        "Laterite Soil": 7
    }
    
    # Default Soil Type Based On Location
    location_soil_mapping = {
        "Hyderabad": ("Alluvial Soil", 6.6),
        "Warangal": ("Red Soil", 6.8),
        "Karimnagar": ("Black Soil", 7.4),
        "Nizamabad": ("Black Soil", 7.8),
        "Khammam": ("Laterite Soil", 6.3),
        "Adilabad": ("Alluvial Soil", 6.9),
        "Mahabubnagar": ("Red Soil", 6.5),
        "Medak": ("Black Soil", 7.3),
        "Rangareddy": ("Red Soil", 6.7),
        "Siddipet": ("Black Soil", 7.5),
        "Suryapet": ("Sandy Soil", 6.2),
        "Nalgonda": ("Red Soil", 6.6),
        "Jagtial": ("Alluvial Soil", 8.1),
        "Peddapalli": ("Black Soil", 7.7),
        "Mancherial": ("Alluvial Soil", 7.0),
        "Sangareddy": ("Black Soil", 7.4),
        "Kamareddy": ("Black Soil", 7.8),
        "Wanaparthy": ("Sandy Soil", 6.0),
        "Nagarkurnool": ("Sandy Soil", 5.9)
    }
    
    # Weather Data By Season
    season_options = ["Kharif", "Rabi", "Zaid"]
    
    weather_data = {
        "Hyderabad": {
            "Kharif": {"temp": 30, "rain": 420},
            "Rabi": {"temp": 24, "rain": 140},
            "Zaid": {"temp": 38, "rain": 60}
        },
        "Warangal": {
            "Kharif": {"temp": 29, "rain": 520},
            "Rabi": {"temp": 23, "rain": 150},
            "Zaid": {"temp": 37, "rain": 75}
        },
        "Karimnagar": {
            "Kharif": {"temp": 30, "rain": 480},
            "Rabi": {"temp": 22, "rain": 130},
            "Zaid": {"temp": 38, "rain": 70}
        },
        "Nizamabad": {
            "Kharif": {"temp": 29, "rain": 550},
            "Rabi": {"temp": 21, "rain": 160},
            "Zaid": {"temp": 37, "rain": 80}
        },
        "Khammam": {
            "Kharif": {"temp": 28, "rain": 650},
            "Rabi": {"temp": 22, "rain": 180},
            "Zaid": {"temp": 36, "rain": 90}
        }
    }
    
    texts = {
        "English": {
            "title": "Crop Yield Prediction",
            "subtitle": "Enter crop and land details to predict crop yield",
            "crop": "Select Crop",
            "location": "Select Location",
            "temperature": "Expected Avg Temperature For Next 6 Months (°C)",
            "rainfall": "Expected Rainfall For Next 6 Months (mm)",
            "soil": "Soil Value",
            "acres": "Land Area (Acres)",
            "captcha": "Captcha",
            "predict": "Predict Yield",
            "yield": "Predicted Crop Yield",
            "report": "Detailed Crop Report",
            "required": "Please select crop, location and soil type",
            "captcha_wrong": "Captcha is incorrect",
            "valid": "Prediction error. Please check model input features.",
            "yield_status": "Yield Status",
            "condition": "Condition Analysis",
            "loss": "Crop Loss Possibility",
            "recommendation": "Recommendation",
            "advice": "Additional Advice",
            "high": "High Yield Expected",
            "medium": "Moderate Yield Expected",
            "low": "Low Yield Expected",
            "good_condition": "Weather conditions are suitable for crop growth",
            "bad_condition": "Extreme weather may affect crop growth",
            "low_loss": "Low chance of crop loss",
            "high_loss": "High chance of crop loss",
            "recommend_text": "Maintain proper irrigation, balanced fertilizers and soil nutrients.",
            "advice_text": "Monitor pests, rainfall and soil health regularly for better yield."
        }
    }
    
    t = texts[language]
    
    
    # Custom CSS
    st.markdown("""
    <style>
    
    .main {
        background-color: #f5fff5;
    }
    
    .stSelectbox label,
    .stNumberInput label {
        font-size: 18px !important;
        font-weight: 600 !important;
        color: #1b5e20 !important;
    }
    
    .stSelectbox > div > div,
    .stNumberInput > div > div > input {
        border-radius: 12px !important;
        border: 2px solid #81c784 !important;
    }
    
    .stButton > button {
        width: 100%;
        height: 45px;
        font-size: 26px;
        font-weight: bold;
        background: linear-gradient(135deg,#1b5e20,#43a047);
        color: white;
        border-radius: 18px;
        border: none;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.15);
        transition: 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg,#0d4715,#2e7d32);
        color: white;
        transform: scale(1.03);
    }
    
    .captcha-box {
        background: linear-gradient(135deg, #dcedc8, #f1f8e9);
        padding: 18px;
        border-radius: 14px;
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        color: #1b5e20;
        margin-top: 20px;
        margin-bottom: 15px;
        border: 2px solid #aed581;
    }
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    </style>
    """, unsafe_allow_html=True)
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)
    
    with row1_col1:
        crop_options = ["Select Crop"] + list(crop_names[language].values())
    
        selected_crop_display = st.selectbox(t["crop"], crop_options)
        selected_location = st.selectbox(t["location"], location_names[language])
        selected_season = st.selectbox("Select Season", season_options)
    
        # REALTIME WEATHER
        current_temp, current_rain = get_weather(selected_location)
    
        # SHOW CURRENT TEMPERATURE
        if selected_location != "Select Location":
            st.markdown(f"""
            <div style="
                background-color:#e8f5e9;
                padding:12px;
                border-radius:10px;
                margin-top:10px;
                text-align:center;
                font-size:22px;
                font-weight:bold;
                color:#1b5e20;">
                🌡 Current Temperature in {selected_location}: {current_temp:.1f} °C
            </div>
            """, unsafe_allow_html=True)
    # ✅ initialize first (VERY IMPORTANT)
    # ✅ initialize first
    auto_temp = 0
    auto_rain = 0
    
    if selected_location != "Select Location":
    
        # realtime weather
        current_temp, current_rain = get_weather(selected_location)
    
        # expected rainfall from dataset
        expected_rain = expected_rain_df[
            (expected_rain_df['district'] == selected_location.lower()) &
            (expected_rain_df['season'] == selected_season)
        ]['rainfall'].values
    
        if len(expected_rain) > 0:
            expected_rain = expected_rain[0]
        else:
            expected_rain = 0
    
        # seasonal temp
        if selected_season == "Kharif":
            seasonal_temp = 30
        elif selected_season == "Rabi":
            seasonal_temp = 22
        else:
            seasonal_temp = 35
    
        # FINAL VALUES
        auto_temp = round((current_temp + seasonal_temp) / 2, 1)
    
        auto_rain = round(
            (expected_rain * 0.4) + (current_rain * 0.6),
            1
        )
    
        # LIMITS
        auto_rain = max(0.0, min(auto_rain, 5000.0))
    temperature = st.number_input(
            t["temperature"],
            min_value=0.0,
            max_value=60.0,
            value=float(auto_temp),
            step=1.0,
            disabled=(selected_location == "Select Location")
    )
    
    with row1_col2:
        if selected_location != "Select Location":
            default_soil_type, default_soil_value = location_soil_mapping[selected_location]
        else:
            default_soil_type = "Select Soil Type"
            default_soil_value = 0.0
    
        rainfall = st.number_input(
            t["rainfall"],
            min_value=0.0,
            max_value=5000.0,
            value=min(float(auto_rain), 5000.0),
            step=10.0,
            disabled=(selected_location == "Select Location")
        )
    
        soil_type = st.selectbox(
            "Soil Type" if language == "English" else "మట్టి రకం",
            soil_types[language],
            index=soil_types[language].index(default_soil_type)
        )
    
        default_soil_values = {
            "Black Soil": 8.5,
            "Red Soil": 6.5,
            "Clay Soil": 9.0,
            "Sandy Soil": 4.5,
            "Loamy Soil": 7.5,
            "Alluvial Soil": 7.0,
            "Laterite Soil": 5.8
        }
    
        selected_soil_value = default_soil_values.get(soil_type, default_soil_value)
    
        soil = st.number_input(
            t["soil"],
            min_value=0.0,
            max_value=14.0,
            value=float(selected_soil_value),
            step=0.1,
            disabled=True
        )
    
        acres = st.number_input(
            t["acres"],
            min_value=0.1,
            max_value=1000.0,
            value=1.0,
            step=0.5
        )
    
    if "captcha_num1" not in st.session_state:
        st.session_state.captcha_num1 = random.randint(1, 20)
        st.session_state.captcha_num2 = random.randint(1, 20)
    
    st.markdown(
        f"""
        <div class='captcha-box'>
            {t['captcha']}: {st.session_state.captcha_num1} + {st.session_state.captcha_num2} = ?
        </div>
        """,
        unsafe_allow_html=True
    )
    
    captcha_answer = st.number_input("Enter Captcha", min_value=0, step=1)
    
    season_crop_bonus = {
        "Kharif": {
            "Paddy": 90,
            "Wheat": -20,
            "Maize": 30,
            "Barley": -25
        },
        "Rabi": {
            "Paddy": 40,
            "Wheat": 75,
            "Maize": 15,
            "Barley": 60
        },
        "Zaid": {
            "Paddy": -80,
            "Wheat": -50,
            "Maize": 50,
            "Barley": -40
        }
    }
    
    crop_mapping = {
        "Paddy": 0,
        "Wheat": 1,
        "Maize": 2,
        "Barley": 3
    }
    
    if st.button(t["predict"]):
    
        if (
            selected_crop_display == "Select Crop" or
            selected_location == "Select Location" or
            soil_type == "Select Soil Type"
        ):
            st.error(t["required"])
    
        else:
            correct_answer = st.session_state.captcha_num1 + st.session_state.captcha_num2
    
            if captcha_answer != correct_answer:
                st.error(t["captcha_wrong"])
    
            else:
                try:
                    crop_value = crop_mapping[selected_crop_display]
                    location_value = location_mapping[selected_location]
                    soil_type_value = soil_type_mapping[soil_type]
    
                    adjusted_soil = soil
                    crop_soil_bonus = 0
    
                    if crop_value == 0 and soil_type_value in [1, 3, 6]:
                        crop_soil_bonus = 2.5
                    elif crop_value == 1 and soil_type_value in [2, 5]:
                        crop_soil_bonus = 2.0
                    elif crop_value == 2 and soil_type_value in [1, 4, 6]:
                        crop_soil_bonus = 2.2
                    elif crop_value == 3 and soil_type_value in [2, 5]:
                        crop_soil_bonus = 1.8
    
                    adjusted_soil += crop_soil_bonus
    
                    data = np.array([[crop_value, location_value, temperature, rainfall, adjusted_soil]])
                    prediction = model.predict(data)
    
                    predicted_base_yield = prediction[0]
                    base_yield_per_acre = (predicted_base_yield / 1000)
    
                    crop_base_multiplier = {
                        "Paddy": 22,
                        "Wheat": 16,
                        "Maize": 18,
                        "Barley": 14
                    }
    
                    season_yield_multiplier = {
                        "Paddy": {
                            "Kharif": 1.5,
                            "Rabi": 1.15,
                            "Zaid": 0.55
                        },
                        "Wheat": {
                            "Kharif": 0.8,
                            "Rabi": 1.6,
                            "Zaid": 0.7
                        },
                        "Maize": {
                            "Kharif": 1.2,
                            "Rabi": 1.0,
                            "Zaid": 1.35
                        },
                        "Barley": {
                            "Kharif": 0.75,
                            "Rabi": 1.5,
                            "Zaid": 0.65
                        }
                    }
    
                    if selected_crop_display == "Paddy":
                        if selected_season == "Kharif":
                            total_quintals = random.uniform(28, 35) * acres
                        elif selected_season == "Rabi":
                            total_quintals = random.uniform(22, 27) * acres
                        else:
                            total_quintals = random.uniform(10, 15) * acres
    
                        total_yield = total_quintals * 100
    
                    soil_yield_multiplier = 1.0
    
                    if selected_crop_display == "Paddy":
                        if soil_type in ["Black Soil", "Clay Soil", "Alluvial Soil"]:
                            soil_yield_multiplier = 1.4
                        elif soil_type == "Sandy Soil":
                            soil_yield_multiplier = 0.7
    
                    elif selected_crop_display == "Wheat":
                        if soil_type in ["Loamy Soil", "Red Soil"]:
                            soil_yield_multiplier = 1.3
                        elif soil_type == "Laterite Soil":
                            soil_yield_multiplier = 0.8
    
                    elif selected_crop_display == "Maize":
                        if soil_type in ["Sandy Soil", "Black Soil"]:
                            soil_yield_multiplier = 1.25
                        elif soil_type == "Clay Soil":
                            soil_yield_multiplier = 0.75
    
                    elif selected_crop_display == "Barley":
                        if soil_type in ["Loamy Soil", "Red Soil"]:
                            soil_yield_multiplier = 1.35
                        elif soil_type == "Sandy Soil":
                            soil_yield_multiplier = 0.8
    
                    rainfall_multiplier = 1.0
    
                    if selected_crop_display == "Paddy":
                        if rainfall >= 400:
                            rainfall_multiplier = 1.3
                        elif rainfall >= 150 and rainfall < 400:
                            rainfall_multiplier = 1.0
                        elif rainfall < 150:
                            rainfall_multiplier = 0.6
    
                        if selected_season == "Kharif":
                            rainfall_multiplier += 0.2
                        elif selected_season == "Zaid":
                            rainfall_multiplier -= 0.2
    
                    elif selected_crop_display == "Wheat":
                        if rainfall >= 80 and rainfall <= 200:
                            rainfall_multiplier = 1.5
                            
                        elif rainfall < 150:
                            rainfall_multiplier = 0.6
                            
                        elif rainfall > 350:
                            rainfall_multiplier = 0.7
    
                    elif selected_crop_display == "Maize":
                        if rainfall >= 150 and rainfall <= 300:
                            rainfall_multiplier = 1.25
                        elif rainfall > 500:
                            rainfall_multiplier = 0.8
    
                    elif selected_crop_display == "Barley":
                        if rainfall >= 60 and rainfall <= 180:
                            rainfall_multiplier = 1.3
                        elif rainfall > 300:
                            rainfall_multiplier = 0.75
    
                    if selected_crop_display != "Paddy":
                        realistic_multiplier = crop_base_multiplier[selected_crop_display]
                        seasonal_factor = season_yield_multiplier[selected_crop_display][selected_season]
    
                        total_yield = (
                            base_yield_per_acre *
                            realistic_multiplier *
                            seasonal_factor *
                            soil_yield_multiplier *
                            rainfall_multiplier *
                            acres
                        )
    
                        total_quintals = total_yield / 100
    
                    if total_yield > 10000:
                        total_yield = 10000
    
                    total_quintals = total_yield / 100
    
                    if total_yield >= 2500:
                        yield_status = "High Yield Expected"
    
                    elif total_yield >= 1200:
                        yield_status = "Moderate Yield Expected"
    
                    else:
                        yield_status = "Low Yield Expected"
                    # =========================================
                    # SMART CROP WEATHER ANALYSIS
                    # =========================================
    
                    crop_conditions = {
    
                        "Paddy": {
                            "temp_min": 20,
                            "temp_max": 38,
                            "rain_min": 600,
                            "rain_max": 1400,
                            "best_soils": ["Black Soil", "Clay Soil", "Alluvial Soil"]
                        },
    
                        "Wheat": {
                            "temp_min": 10,
                            "temp_max": 28,
                            "rain_min": 50,
                            "rain_max": 400,
                            "best_soils": ["Loamy Soil", "Red Soil"]
                        },
    
                        "Maize": {
                            "temp_min": 18,
                            "temp_max": 36,
                            "rain_min": 100,
                            "rain_max": 800,
                            "best_soils": ["Black Soil", "Sandy Soil", "Alluvial Soil"]
                        },
    
                        "Barley": {
                            "temp_min": 8,
                            "temp_max": 26,
                            "rain_min": 40,
                            "rain_max": 350,
                            "best_soils": ["Loamy Soil", "Red Soil"]
                        }
                    }
    
                    selected_crop_rules = crop_conditions[selected_crop_display]
    
                    # CONDITION SCORE
                    condition_score = 0
    
                    # temperature analysis
                    if (
                        temperature >= selected_crop_rules["temp_min"]
                        and temperature <= selected_crop_rules["temp_max"]
                    ):
                        condition_score += 1
    
                    # rainfall analysis
                    if (
                        rainfall >= selected_crop_rules["rain_min"]
                        and rainfall <= selected_crop_rules["rain_max"]
                    ):
                        condition_score += 1
    
                    # soil analysis
                    if soil_type in selected_crop_rules["best_soils"]:
                        condition_score += 1
    
    
                    # FINAL CONDITION RESULT
                    if condition_score == 3:
    
                        condition = "Excellent weather and soil conditions for crop growth"
                        loss = "Very low chance of crop loss"
    
                    elif condition_score == 2:
    
                        condition = "Moderate conditions for crop growth"
                        loss = "Medium chance of crop loss"
    
                    else:
    
                        condition = "Unfavorable weather conditions may affect crop growth"
                        loss = "High chance of crop loss"
    
                    crop_predictions = {}
    
                    for crop_name, crop_code in crop_mapping.items():
    
                        rules = crop_conditions[crop_name]
    
                        suitability_score = 0
    
                        # =========================
                        # TEMPERATURE ANALYSIS
                        # =========================
                        if (
                            temperature >= rules["temp_min"]
                            and temperature <= rules["temp_max"]
                        ):
                            suitability_score += 30
    
                        # =========================
                        # RAINFALL ANALYSIS
                        # =========================
                        if (
                            rainfall >= rules["rain_min"]
                            and rainfall <= rules["rain_max"]
                        ):
                            suitability_score += 30
    
                        # =========================
                        # SOIL ANALYSIS
                        # =========================
                        if soil_type in rules["best_soils"]:
                            suitability_score += 20
    
                        # =========================
                        # SEASON ANALYSIS
                        # =========================
                        season_bonus = season_crop_bonus[selected_season].get(crop_name, 0)
    
                        suitability_score += season_bonus
    
                        # =========================
                        # ML PREDICTION
                        # =========================
                        test_data = np.array([
                            [crop_code, location_value, temperature, rainfall, adjusted_soil]
                        ])
    
                        predicted_yield = model.predict(test_data)[0]
    
                        # normalize ML yield
                        normalized_yield = predicted_yield / 100
                        # heavy penalty for unsuitable conditions
                        if suitability_score < 40:
                            normalized_yield *= 0.4
    
                        if suitability_score < 20:
                            normalized_yield *= 0.2
                        # FINAL SCORE
                        final_score = suitability_score + normalized_yield
                        base_best_yield = predicted_yield / 1000
    
                        realistic_best_yield = (
                            base_best_yield *
                            crop_base_multiplier[crop_name] *
                            season_yield_multiplier[crop_name][selected_season]
                        )
    
                        # soil adjustment
                        if soil_type in rules["best_soils"]:
                            realistic_best_yield *= 1.2
                        else:
                            realistic_best_yield *= 0.8
    
                        # rainfall adjustment
                        if (
                            rainfall >= rules["rain_min"]
                            and rainfall <= rules["rain_max"]
                        ):
                            realistic_best_yield *= 1.1
                        else:
                            realistic_best_yield *= 0.7
    
                        realistic_best_yield *= acres
                        
                         # If selected crop itself is best crop
                        if crop_name == selected_crop_display:
    
                            # Same as displayed predicted yield
                            final_best_yield = total_yield
    
                        else:
    
                            # realistic best crop yield calculation
                            final_best_yield = (
                                realistic_best_yield
                                * soil_yield_multiplier
                                * rainfall_multiplier
                            )
    
                            # suitability adjustment
                            if suitability_score >= 70:
                                final_best_yield *= 1.10
    
                            elif suitability_score >= 50:
                                final_best_yield *= 1.00
    
                            else:
                                final_best_yield *= 0.75
    
                            # realistic limits
                            final_best_yield = max(300, final_best_yield)
                            final_best_yield = min(final_best_yield, 8000)
                            
                        crop_predictions[crop_name] = {
                            "score": final_score,
                            "yield": final_best_yield
                        }
    
                    # =========================
                    # BEST CROP
                    # =========================
    
                    best_crop = max(
                        crop_predictions,
                        key=lambda x: crop_predictions[x]["score"]
                    )
    
                    best_crop_value = crop_predictions[best_crop]["yield"]
    
                    selected_crop_score = crop_predictions[selected_crop_display]["score"]
                    # recommendation logic
                    if best_crop == selected_crop_display:
    
                        recommendation_text = (
                            f"{selected_crop_display} is the best suitable crop "
                            f"for this location and weather conditions."
                        )
    
                    else:
    
                        recommendation_text = (
                            f"{best_crop} is more suitable than "
                            f"{selected_crop_display} under current conditions."
                        )
                    st.success(f"{t['yield']}: {total_yield:.2f} Kg")
    
                    st.markdown(f"""
                    ### {t['report']}
    
                    - **{t['crop']}**: {selected_crop_display}
                    - **{t['location']}**: {selected_location}
                    - **Season**: {selected_season}
                    - **{t['temperature']}**: {temperature} °C
                    - **{t['rainfall']}**: {rainfall} mm
                    - **{t['soil']}**: {soil:.1f}
                    - **{t['acres']}**: {acres}
                    - **{t['yield']}**: {total_yield:.2f} Kg
                    - **Predicted Yield In Quintals**: {total_quintals:.2f}
                    - **{t['yield_status']}**: {yield_status}
                    - **{t['condition']}**: {condition}
                    - **{t['loss']}**: {loss}
                    - **Soil Type**: {soil_type}
                    - **Best Suitable Crop**: {best_crop}
                    - **Best Crop Estimated Yield**: {best_crop_value:.2f} Kg
                    - **{t['recommendation']}**: {recommendation_text}
                    - **{t['advice']}**: {t['advice_text']}
                    - **Date**: {datetime.now().strftime('%d-%m-%Y')}
                    """)
    
                    st.session_state.captcha_num1 = random.randint(1, 20)
                    st.session_state.captcha_num2 = random.randint(1, 20)
    
                except Exception as e:
                    st.error(f"{t['valid']}\n{e}")

                    st.markdown('</div>', unsafe_allow_html=True)
