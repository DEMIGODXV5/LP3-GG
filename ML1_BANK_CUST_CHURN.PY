# =====================================================
# CELL 1: IMPORT LIBRARIES
# =====================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping


# =====================================================
# CELL 2: READ DATASET
# =====================================================

data = pd.read_csv("Churn_Modelling.csv")

print("Dataset Loaded Successfully")
print(data.head())


# =====================================================
# CELL 3: DATASET INFORMATION
# =====================================================

print("\nDataset Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDataset Shape:", data.shape)


# =====================================================
# CELL 4: DATA PREPROCESSING
# =====================================================

# Remove unnecessary columns
data = data.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

# Convert categorical data into numerical data
data = pd.get_dummies(
    data, columns=["Geography", "Gender"], dtype=int
)

# Separate features and target
X = data.drop("Exited", axis=1)
y = data["Exited"]

print("\nFeatures and Target Separated")


# =====================================================
# CELL 5: SPLIT TRAINING AND TESTING DATA
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# =====================================================
# CELL 6: NORMALIZE DATA
# =====================================================

scaler = StandardScaler()

# Fit scaler on training data
X_train = scaler.fit_transform(X_train)

# Transform testing data
X_test = scaler.transform(X_test)

print("Data Normalized Successfully")


# =====================================================
# CELL 7: BUILD NEURAL NETWORK MODEL - A Neural Network is a machine learning model inspired by the human brain. It consists of interconnected neurons arranged in layers.
# =====================================================

model = Sequential()

# First hidden layer
model.add(Dense(16, activation="relu",
                input_shape=(X_train.shape[1],)))

# Second hidden layer
model.add(Dense(8, activation="relu"))

# Dropout to reduce overfitting
model.add(Dropout(0.2))

# Output layer
model.add(Dense(1, activation="sigmoid"))

model.summary()


# =====================================================
# CELL 8: COMPILE MODEL
# =====================================================

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

print("Model Compiled Successfully")


# =====================================================
# CELL 9: TRAIN MODEL
# =====================================================

# Early stopping to prevent overfitting
early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

history = model.fit(
    X_train,
    y_train,
    epochs=30,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop]
)


# =====================================================
# CELL 10: MAKE PREDICTIONS
# =====================================================

predictions = model.predict(X_test)

# Convert probabilities into 0 or 1
y_pred = (predictions > 0.5).astype(int)

print("Predictions Completed")


# =====================================================
# CELL 11: CALCULATE ACCURACY
# =====================================================

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy * 100, "%")


# =====================================================
# CELL 12: CONFUSION MATRIX
# =====================================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# =====================================================
# CELL 13: POINTS OF IMPROVEMENT
# =====================================================

print("\nPoints of Improvement:")
print("1. Data Normalization using StandardScaler")
print("2. Multiple Hidden Layers")
print("3. Dropout to reduce Overfitting")
print("4. Early Stopping")
print("5. Adam Optimizer")
