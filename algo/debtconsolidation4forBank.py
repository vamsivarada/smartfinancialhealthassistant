'''the code uses a decision tree classifier to predict whether a customer
is likely to benefit from debt consolidation based on features such as current interest rate,
consolidation interest rate, and credit score. The model is trained on a subset of the data,
 and then predictions are made on the entire dataset.'''


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

def debtconsolidationbank():
    # Mock data generation
    np.random.seed(42)
    num_samples = 100

    data = {
        'Customer ID': range(1, num_samples + 1),
        'Credit Score': np.random.randint(300, 850, num_samples),
        'Current Interest Rate': np.random.uniform(10, 25, num_samples),
        'Consolidation Interest Rate': np.random.uniform(5, 20, num_samples),
    }

    df = pd.DataFrame(data)

    # Display the mock data
    print("Mock Data:")
    print(df.head())

    # Assuming 'Current Interest Rate', 'Consolidation Interest Rate', and other features in the dataset
    features = df[['Current Interest Rate', 'Consolidation Interest Rate', 'Credit Score']]
    labels = (df['Consolidation Interest Rate'] < df['Current Interest Rate']).astype(int)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Build a decision tree classifier
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)

    # Evaluate the accuracy of the model
    accuracy = accuracy_score(y_test, predictions)
    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

    # Identify opportunities for debt consolidation using the trained model
    consolidation_opportunities = df[model.predict(features) == 1]

    # Display the opportunities
    print("\nOpportunities for Debt Consolidation:")
    # return (consolidation_opportunities[['Customer ID', 'Current Interest Rate', 'Consolidation Interest Rate']].head(1))
    print (consolidation_opportunities[['Customer ID', 'Current Interest Rate', 'Consolidation Interest Rate']].head(1)['Current Interest Rate'])
    # return consolidation_opportunities[['Customer ID', 'Current Interest Rate', 'Consolidation Interest Rate']]
if __name__ == '__main__':
    debtconsolidationbank()
