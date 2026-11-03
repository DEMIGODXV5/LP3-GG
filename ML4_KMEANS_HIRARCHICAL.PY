# K-Means :=>
# =====================================================
# CELL 1: IMPORT LIBRARIES
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# =====================================================
# CELL 2: READ DATASET
# =====================================================

data = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print("Dataset Loaded Successfully")
print(data.head())

print("\nDataset Shape:", data.shape)


# =====================================================
# CELL 3: SELECT FEATURES
# =====================================================

# Select numerical sales-related columns
#Because K-Means works with numerical features and calculates distances between data points.We store the selected features in X.
X = data[[
    "SALES",
    "QUANTITYORDERED",
    "PRICEEACH",
    "MSRP"
]]

print("\nSelected Features:")
print(X.head())


# =====================================================
# CELL 4: NORMALIZE DATA
# =====================================================
#Suppose our data has:
# - SALES = 5000
# - QUANTITYORDERED = 20
# - PRICEEACH = 100
# The values have very different ranges.

# Since K-Means uses distance calculations, features with larger numerical values could dominate the clustering.
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nData Normalized Successfully")


# =====================================================
# CELL 5: ELBOW METHOD
# =====================================================

wcss = [] #WCSS stands for Within-Cluster Sum of Squares.It measures the sum of squared distances between each data point and its assigned cluster centroid.Lower WCSS means data points are closer to their respective centroids.

# Calculate WCSS for different cluster values
for i in range(1, 11):

    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )
    #n_clusters=i → Number of clusters.
    # random_state=42 → Makes initialization reproducible.
    # n_init=10 → Runs the algorithm with 10 different centroid initializations and keeps the best result.

    kmeans.fit(X_scaled)

    wcss.append(kmeans.inertia_) #inertia_ gives the WCSS value of the fitted model.

# Plot Elbow Graph
plt.plot(range(1, 11), wcss, marker="o")

plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")

plt.show()

#Initially, WCSS decreases rapidly as K increases.
# After a certain point, the decrease becomes slower.
# This bending point looks like an elbow.
# We select K near this elbow as a reasonable cluster count.


# =====================================================
# CELL 6: APPLY K-MEANS CLUSTERING
# =====================================================

# Select optimal number of clusters
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train the model
kmeans.fit(X_scaled)

# Assign cluster labels
data["Cluster"] = kmeans.labels_

print("\nClustering Completed Successfully")


# =====================================================
# CELL 7: DISPLAY CLUSTER RESULTS
# =====================================================

print("\nCluster Assignments:")
print(data[["SALES", "QUANTITYORDERED", "Cluster"]].head(10))

print("\nNumber of Records in Each Cluster:")
print(data["Cluster"].value_counts())


# =====================================================
# CELL 8: VISUALIZE CLUSTERS
# =====================================================

plt.scatter(
    X_scaled[:, 0], #Selects the first feature, which is SALES.
    X_scaled[:, 1], #Selects the second feature, which is QUANTITYORDERED.
    c=kmeans.labels_
)

plt.title("K-Means Clustering of Sales Data")

plt.xlabel("Sales (Normalized)")
plt.ylabel("Quantity Ordered (Normalized)")

plt.show()
#===== END OF PROGRAM=======



"""
Working of K-Means
1. Initialize centroids
   
   Randomly selects 3 initial cluster centres.
2. Calculate distances
   
   Calculates the distance of each data point from all 3 centroids.
3. Assign clusters
   
   Assigns each data point to its nearest centroid.
4. Update centroids
   
   Calculates the mean of all points belonging to each cluster and updates its centre.
5. Repeat
   
   Repeats distance calculation and centroid updating until the clusters stop changing significantly or convergence is reached.

"""