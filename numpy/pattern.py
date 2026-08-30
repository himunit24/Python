import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import streamlit as st


# Model aur Scaler train karne ka function (Cache kiya taaki baar baar train na ho)
@st.cache_resource
def load_and_train_model():
  housing = fetch_california_housing(as_frame=True)
  df = housing.frame

  X = df.drop(columns=['MedHouseVal'])
  y = df['MedHouseVal']

  scaler = StandardScaler()
  X_scaled = scaler.fit_transform(X)

  model = RandomForestRegressor(n_estimators=50, random_state=42)
  model.fit(X_scaled, y)

  return model, scaler


model, scaler = load_and_train_model()

# --- UI Setup ---
st.set_page_config(page_title='House Price Predictor', layout='centered')
st.title('🏡 House Price Prediction App')
st.write(
    'Apne house parameters enter karein aur estimated price calculate karein.'
)

# Input Form
col1, col2 = st.columns(2)

with col1:
  med_inc = st.number_input(
      'Median Income (in $10k)', min_value=0.5, max_value=15.0, value=3.5
  )
  house_age = st.number_input(
      'House Age (Years)', min_value=1.0, max_value=100.0, value=25.0
  )
  ave_rooms = st.number_input(
      'Average Rooms', min_value=1.0, max_value=20.0, value=5.0
  )
  ave_bedrms = st.number_input(
      'Average Bedrooms', min_value=0.5, max_value=10.0, value=1.0
  )

with col2:
  population = st.number_input(
      'Population in Area', min_value=10.0, max_value=50000.0, value=1200.0
  )
  ave_occup = st.number_input(
      'Average Occupancy', min_value=1.0, max_value=20.0, value=3.0
  )
  latitude = st.number_input(
      'Latitude', min_value=32.0, max_value=42.0, value=35.5
  )
  longitude = st.number_input(
      'Longitude', min_value=-125.0, max_value=-114.0, value=-119.5
  )

# Predict Button
if st.button('Predict House Price'):
  input_data = np.array([[
      med_inc,
      house_age,
      ave_rooms,
      ave_bedrms,
      population,
      ave_occup,
      latitude,
      longitude,
  ]])

  # Scale features
  input_scaled = scaler.transform(input_data)

  # Prediction ($100k units me aati hai)
  pred_val = model.predict(input_scaled)[0]
  final_price = pred_val * 100000

  st.success(f'Estimated House Price: **${final_price:,.2f}**')