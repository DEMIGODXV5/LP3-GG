# =====================================================
# CELL 1: IMPORT LIBRARIES
# =====================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# =====================================================
# CELL 2: READ DATASET
# =====================================================

data = pd.read_csv("emails.csv")

print("Dataset Loaded Successfully")
print(data.head())

print("\nDataset Shape:", data.shape)

# =====================================================
# CELL 3: DATA PREPROCESSING
# =====================================================

# Remove unnecessary Email ID column
data = data.drop("Email No.", axis=1)

# Separate features and target
X = data.drop("Prediction", axis=1) #X contains input features (word frequencies).
y = data["Prediction"] #y contains the target/output (Spam or Not Spam).

print("\nFeatures and Target Separated")
print("Features Shape:", X.shape)
print("Target Shape:", y.shape)

# =====================================================
# CELL 4: SPLIT TRAINING AND TESTING DATA
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
#test_size=0.2	20% data for testing ,  random_state=42	Ensures reproducible splitting , stratify=y	Maintains the proportion of spam and non-spam emails in both sets

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# =====================================================
# CELL 5: NORMALIZE DATA -Normalization brings features to a similar scale so that features with larger values do not dominate the learning process.
# =====================================================

scaler = StandardScaler() # it uses the formula - Z= (X(og value)-u(mean))/S.D

# Fit and transform training data
X_train = scaler.fit_transform(X_train) #fit_transform() Calculates mean and standard deviation, then scales training data

# Transform testing data
X_test = scaler.transform(X_test) #transform() Uses the same calculated values to scale testing data

print("\nData Normalized Successfully")


# =====================================================
# CELL 6: K-NEAREST NEIGHBORS (KNN) - K-Nearest Neighbors is a supervised machine learning algorithm used for classification and regression
# =====================================================

# Initialize KNN model
knn = KNeighborsClassifier(n_neighbors=5)

# Train KNN model
knn.fit(X_train, y_train) #Provides training data to the KNN algorithm

# Predict test data
knn_pred = knn.predict(X_test) #Predicts whether each testing email is spam or not spam.

# Calculate accuracy
knn_accuracy = accuracy_score(y_test, knn_pred)

print("\nKNN Accuracy:", knn_accuracy * 100, "%")

print("\nKNN Confusion Matrix:")
print(confusion_matrix(y_test, knn_pred))

# =====================================================
# CELL 7: SUPPORT VECTOR MACHINE (SVM)-Support Vector Machine is a supervised machine learning algorithm used for classification and regression.It finds the best decision boundary (hyperplane) that separates different classes.
# =====================================================

# Initialize SVM model
svm = SVC(kernel="linear") #A kernel helps SVM determine the decision boundary between different classes. kernel="linear" uses a linear decision boundary to separate the classes.

# Train SVM model
svm.fit(X_train, y_train)

# Predict test data
svm_pred = svm.predict(X_test)

# Calculate accuracy
svm_accuracy = accuracy_score(y_test, svm_pred)

print("\nSVM Accuracy:", svm_accuracy * 100, "%")

print("\nSVM Confusion Matrix:")
print(confusion_matrix(y_test, svm_pred))

# =====================================================
# CELL 8: CLASSIFICATION REPORT
# =====================================================

print("\nKNN Classification Report:")
print(classification_report(y_test, knn_pred))

print("\nSVM Classification Report:")
print(classification_report(y_test, svm_pred))

"""
Precision	Out of predicted spam emails, how many were actually spam? TP/TP+FP
Recall	Out of actual spam emails, how many were correctly identified? TP/TP+FN
F1-score	Harmonic mean of precision and recall .... 2*(Precision*Recall)/(Precision+Recall)
Support	Number of actual samples belonging to each class



Precision	Recall
Out of predicted Spam, how many were actually Spam?	Out of actual Spam, how many did we identify?
Focuses on correctness of predictions	Focuses on finding all positive cases
High precision = Fewer false alarms	High recall = Fewer missed spam emails
"""


# =====================================================
# CELL 9: PERFORMANCE COMPARISON
# =====================================================

print("\n===== MODEL PERFORMANCE COMPARISON =====")

print("KNN Accuracy:", knn_accuracy * 100, "%")
print("SVM Accuracy:", svm_accuracy * 100, "%")

if knn_accuracy > svm_accuracy:
    print("\nKNN performs better.")
elif svm_accuracy > knn_accuracy:
    print("\nSVM performs better.")
else:
    print("\nBoth models have equal accuracy.")