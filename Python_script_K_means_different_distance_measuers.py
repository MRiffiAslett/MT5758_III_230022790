import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import pairwise_distances
from sklearn.manifold import MDS
import numpy as np

# Read the CSV file into a DataFrame
data = pd.read_csv('merged_data_with_coordinates.csv')

# Drop rows with missing values inplace
data.dropna(inplace=True)

# Drop the 'country' column
data.drop(columns=['country'], inplace=True)

# Normalize the data
scaler = StandardScaler()
normalized_data = scaler.fit_transform(data)

# Perform KMeans clustering with 2 clusters
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(normalized_data)

# Calculate MDS with correlation as the distance metric
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
distances = pairwise_distances(normalized_data, metric='correlation')
mds_data = mds.fit_transform(distances)

# Plot MDS visualization with clusters colored by continent
plt.figure(figsize=(10, 6))
sns.scatterplot(x=mds_data[:, 0], y=mds_data[:, 1], hue=data['continent'], palette='Set1')

# Plot cluster centers with circles
cluster_centers_mds = mds.fit_transform(kmeans.cluster_centers_)
for i in range(len(cluster_centers_mds)):
    plt.scatter(cluster_centers_mds[i, 0], cluster_centers_mds[i, 1], color='black', marker='o', s=100, edgecolor='red')

# Set plot labels and title
plt.xlabel('MDS Dimension 1')
plt.ylabel('MDS Dimension 2')
plt.title('KMeans Clustering on MDS Visualization with Correlation Distance')
plt.legend(title='Continent')
plt.grid(True)
plt.show()
