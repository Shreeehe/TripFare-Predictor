
# 🚖 TripFare: Predicting Urban Taxi Fare with Machine Learning

A complete regression pipeline to estimate NYC taxi fares using real-world data. This project includes data preprocessing, feature engineering, model training, evaluation, and a Streamlit-based web UI for real-time predictions.

---

## 📂 Project Structure

```
├── taxi_fare.csv                         # Raw and cleaned CSVs
├── EDA + Future Engineering + ML.ipynb   # Jupyter notebooks for EDA and model building
├── best_gbr_model.pkl                    # Saved .pkl models
├── app.py                                # Streamlit app
├── README.md                             
```

---

## 🧠 Problem Statement

Predict the **total taxi fare amount** based on trip details like distance, time, passenger count, and more — aiming to support better fare transparency and planning.

---

## 🗃️ Dataset Overview

NYC Yellow Taxi Trip Dataset  
**Rows**: 212,345+  
**Columns**: 18  

| Column | Description |
|--------|-------------|
| `VendorID` | ID of the taxi provider |
| `tpep_pickup_datetime` | Trip start datetime |
| `tpep_dropoff_datetime` | Trip end datetime |
| `passenger_count` | Number of passengers |
| `pickup_longitude`, `pickup_latitude` | Pickup coordinates |
| `dropoff_longitude`, `dropoff_latitude` | Dropoff coordinates |
| `RatecodeID` | Type of rate (e.g., standard, JFK) |
| `payment_type` | Method used to pay |
| `fare_amount` | Base fare |
| `tip_amount`, `tolls_amount`, `mta_tax`, `extra` | Other fare components |
| `total_amount` | Final amount paid (🎯 target) |

---

## 🔍 EDA & Insights

- Visualized fare trends by:
  - **Hour of day**, **Day of week**, **Weekend vs Weekday**
  - Trip distance vs fare per mile/min
- Identified **night trips** and **weekend rides** affecting fare
- Plotted **trip durations**, **pickup times**, and **high demand hours**

---

## 🏗️ Data Preprocessing

✅ Converted datetimes to new features  
✅ Removed duplicates  
✅ Outlier treatment (IQR-based)  
✅ Skewness fixed using log transformations  
✅ Label encoded categorical columns

---

## ⚙️ Feature Engineering

New features added:

| Feature | Description |
|--------|-------------|
| `trip_distance` | Haversine distance from pickup to dropoff |
| `pickup_hour`, `pickup_day` | From pickup datetime |
| `is_weekend`, `is_night`, `am_pm` | Time-based indicators |

Final Features used in training:

```python
['trip_distance', 'passenger_count', 'pickup_hour',
 'pickup_day', 'is_weekend', 'is_night',
 'RatecodeID', 'payment_type', 'am_pm']
```

---

## 🧪 Model Building & Evaluation

Built and evaluated 5 regression models:

| Model                  | R² Score | MAE   | RMSE  |
|------------------------|----------|-------|-------|
| Linear Regression      | 0.616    | 1.87  | 2.75  |
| Ridge Regression       | 0.616    | 1.87  | 2.75  |
| Lasso Regression       | 0.596    | 2.18  | 2.82  |
| Random Forest Regressor| 0.643    | 1.97  | 2.66  |
| Gradient Boosting      | **0.713**| **1.75**| **2.38** |

### ✅ Final Model: Gradient Boosting Regressor (Tuned)

Hyperparameter Tuning with `GridSearchCV`:

```python
Best Parameters:
{
  'learning_rate': 0.05,
  'max_depth': 4,
  'min_samples_leaf': 3,
  'min_samples_split': 5,
  'n_estimators': 200
}
```

---

## 💾 Model Saving

Final model saved using `joblib`:
```python
import joblib
joblib.dump(best_model, "best_gbr_model.pkl")
```

---

## 🌐 Streamlit App

🎉 Live UI to test fare predictions!

### Features:
- Input: distance, passenger count, time, day, etc.
- Output: Estimated total fare

### How to Run:
```bash
streamlit run app.py
```

---

## 🔮 Sample Prediction

```
Input:
Trip Distance: 2.4 km
Passenger Count: 2
Pickup Hour: 22 (night)
Pickup Day: Friday

Output:
💸 Estimated Fare: $17.36
```
---

## 📎 License

MIT License. Use freely with love 💖
