import streamlit as st
import numpy as np
import pickle
import time

# Load the trained model
with open("best_gbr_model.pkl", "rb") as file:
    model = pickle.load(file)

# ---------------------- ✨ Page Config ✨ ----------------------
st.set_page_config(page_title="TripFare Predictor", page_icon="🚕", layout="centered")
st.markdown("<h1 style='text-align: center;'>🚕 TripFare Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Estimate your taxi fare instantly 💸</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------- 📥 Input Section ----------------------

with st.form("fare_form"):
    st.subheader("📋 Trip Details")

    col1, col2 = st.columns(2)
    with col1:
        trip_distance = st.number_input("Trip Distance (km)", min_value=0.1, step=0.1, format="%.2f")
        passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, step=1)

    with col2:
        pickup_hour = st.slider("Pickup Hour (0–23)", 0, 23, 12)
        pickup_day = st.selectbox("Pickup Day", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    col3, col4 = st.columns(2)
    with col3:
        RatecodeID = st.selectbox("Rate Code", [1, 2, 3, 4, 5, 6])
    with col4:
        payment_type = st.selectbox("Payment Type", [1, 2, 3, 4])

    # Derived features
    is_weekend = 1 if pickup_day in ['Saturday', 'Sunday'] else 0
    is_night = 1 if (pickup_hour <= 5 or pickup_hour >= 22) else 0
    am_pm = 0 if pickup_hour < 12 else 1

    # Encode day to number
    day_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
               'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    pickup_day_encoded = day_map[pickup_day]

    # Predict Button
    submitted = st.form_submit_button("🎯 Predict Fare")

# ---------------------- 💸 Prediction Output ----------------------

if submitted:
    with st.spinner('⏳ Predicting fare... please wait...'):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

    input_data = np.array([[trip_distance, passenger_count, pickup_hour,
                            pickup_day_encoded, is_weekend, is_night,
                            RatecodeID, payment_type, am_pm]])

    prediction = model.predict(input_data)[0]

    st.markdown(
    f"""
    <div style='
        background-color: #f9f9f9;
        padding: 1.2rem;
        border-radius: 12px;
        border: 2px dashed #ffd700;
        text-align: center;
        font-size: 1.6rem;
        font-weight: 600;
        color: #2c2c2c;
        margin-top: 20px;'
    >
    💰 Your Estimated Fare: <span style='color:#27ae60;'>${round(prediction, 2)}</span>
    </div>
    """,
    unsafe_allow_html=True
)

