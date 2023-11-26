'''the code uses a decision tree classifier to predict whether a customer
is likely to benefit from debt consolidation based on features such as current interest rate,
consolidation interest rate, and credit score. The model is trained on a subset of the data,
 and then predictions are made on the entire dataset.'''

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
def debtconsolidation():
    # Sample debt data (replace this with your actual data)
    debt_amounts = np.random.randint(10000, 100000, size=20)  # Generating random debt amounts
    interest_rates = np.random.uniform(0.1, 0.10, size=20)
    debt_data = pd.DataFrame({
        'Debt Amount': debt_amounts,
        'Interest Rate': interest_rates
    })

    # Standardize the features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(debt_data)

    # Apply PCA to reduce dimensions (for visualization purposes)
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(scaled_data)

    # Determine optimal number of clusters (Elbow method)
    distortions = []
    for i in range(1, 6):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(reduced_data)
        distortions.append(kmeans.inertia_)

    # Based on the Elbow method, let's choose k=3 clusters
    k = 3

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(reduced_data)

    # Add cluster labels to the original data
    debt_data['Cluster'] = clusters

    # Calculate mean interest rate for each cluster
    cluster_interest_rates = debt_data.groupby('Cluster')['Interest Rate'].mean().reset_index()

    # Initialize an empty DataFrame to store recommendations
    consolidation_recommendations = pd.DataFrame(columns=[
        'Cluster', 'Debt Amounts to Consolidate', 'Current Interest Rate', 'Consolidated Interest Rate'
    ])

    # Aggregate recommendations
    for cluster_label, cluster_data in debt_data.groupby('Cluster'):
        current_interest_rate = cluster_interest_rates.loc[cluster_interest_rates['Cluster'] == cluster_label, 'Interest Rate'].values[0]
        consolidated_interest_rate = cluster_data['Interest Rate'].mean()
        debts_in_cluster = cluster_data['Debt Amount']

        # Append recommendations to DataFrame
        recommendations = {
            'Cluster': cluster_label + 1,
            'Debt Amounts to Consolidate': [row for row in debts_in_cluster.values],
            'Current Interest Rate': f"{current_interest_rate:.1%}",
            'Consolidated Interest Rate': f"{consolidated_interest_rate:.1%}"
        }
        recommendations = pd.DataFrame.from_dict(recommendations)
        consolidation_recommendations = pd.concat([consolidation_recommendations, recommendations], ignore_index=True)

    print("Consolidation Recommendations:")
    print(consolidation_recommendations)
    return consolidation_recommendations.head(6)



if __name__ == '__main__':
    debtconsolidation()
