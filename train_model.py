import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

import joblib

# -----------------------------
# LOAD DATA
# -----------------------------

data = pd.read_csv(
    "ml_model/farm_training_data.csv"
)

# -----------------------------
# FEATURES
# -----------------------------

X = data[
    [
        "soil_moisture",
        "temperature",
        "humidity",
        "water_tank"
    ]
]

y = data["crop_yield"]

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# MODEL
# -----------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# -----------------------------
# ACCURACY
# -----------------------------

predictions = model.predict(
    X_test
)

score = r2_score(
    y_test,
    predictions
)

print(
    f"Model Accuracy: {score:.2f}"
)

# -----------------------------
# SAVE MODEL
# -----------------------------

joblib.dump(
    model,
    "ml_model/crop_yield_model.pkl"
)

print(
    "Model Saved Successfully"
)