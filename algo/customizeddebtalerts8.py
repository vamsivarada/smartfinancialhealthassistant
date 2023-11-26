"""
In this example:

Mock data is generated to simulate bank transactions.
Normal transactions are drawn from a normal distribution with a mean of 200,
while fraudulent transactions have a mean of 800.
An Isolation Forest model is trained on the transaction amounts to detect anomalies,
i.e., transactions that are significantly different from the majority of transactions.
Detected anomalies (potential unwanted debits) are printed based on the model's predictions.
Replace this mock data with your actual transaction data. Adjust the model
 parameters and data preprocessing based on the specifics of your dataset and the nature of unwanted debits you want to detect. Additionally, you might want to explore other anomaly detection techniques or feature engineering to improve the detection accuracy.
"""
import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np

# Generating mock data for bank transactions
np.random.seed(42)

# Creating a mock dataset (assuming 'Amount' is the transaction amount)
num_samples = 1000
normal_transactions = np.random.normal(loc=200, scale=50, size=num_samples)
fraud_transactions = np.random.normal(loc=800, scale=100, size=20)  # Simulating fraudulent transactions

# Combining normal and fraudulent transactions
data = np.concatenate([normal_transactions, fraud_transactions])

# Creating a DataFrame
df = pd.DataFrame({'Amount': data})

# Training the Isolation Forest model
model = IsolationForest(contamination=0.02, random_state=42)  # Adjust contamination based on expected anomaly ratio
model.fit(df[['Amount']])

# Predicting anomalies (transactions considered as anomalies)
df['Anomaly'] = model.predict(df[['Amount']])
anomalies = df[df['Anomaly'] == -1]

# Printing detected anomalies
print("Detected Anomalies (Potential Unwanted Debits):")
print(anomalies)
