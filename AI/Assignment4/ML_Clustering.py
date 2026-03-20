# ---------------------------------------------------------
# Machine Learning - Assignment (2)
# Deema Mohammed AL-Maqadma
# ---------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ============================
# 1) Load Dataset
# ============================
df = pd.read_csv("Mall_Customers.csv")

# ============================
# 2) Select Numeric Features
# ============================
X = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]

# ============================
# 3) Handle Missing Values
# ============================
X = X.dropna()

# ============================
# 4) Scale Features
# ============================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ============================
# 5) Try K-Means for k = 2..10
# ============================
inertias = []
sil_scores = []

K = range(2, 11)

for k in K:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)
    
    inertias.append(km.inertia_)
    sil_scores.append(silhouette_score(X_scaled, labels))

# ============================
# 6) Plot Elbow Method
# ============================
plt.figure(figsize=(6,4))
plt.plot(K, inertias, marker="o")
plt.xlabel("k")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.grid(True)
plt.show()

# ============================
# 7) Plot Silhouette Scores
# ============================
plt.figure(figsize=(6,4))
plt.plot(K, sil_scores, marker="o", color="green")
plt.xlabel("k")
plt.ylabel("Silhouette Score")
plt.title("Silhouette vs k")
plt.grid(True)
plt.show()

# ============================
# 8) Choose Best k (based on silhouette)
# ============================
best_k = K[np.argmax(sil_scores)]
print("Best k based on silhouette:", best_k)

# ============================
# 9) Final K-Means Model
# ============================
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

df["cluster"] = clusters
print("\nCluster counts:")
print(df["cluster"].value_counts())

print("\nCluster centers (scaled):")
print(kmeans.cluster_centers_)