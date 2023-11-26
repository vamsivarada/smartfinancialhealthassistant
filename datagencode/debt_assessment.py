import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Number of samples
num_samples = 100

# Generate mock data
data = {
    'Customer ID': [f"{i+1:03d}" for i in range(num_samples)],
    'Income ($)': np.random.randint(4000, 9000, size=num_samples),
    'Debt ($)': np.random.randint(1500, 4000, size=num_samples),
    'Monthly Expenses ($)': np.random.randint(1200, 2500, size=num_samples),
    'Credit Score': np.random.randint(600, 800, size=num_samples)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel file
df.to_excel('debt_assessment_data.xlsx', index=False)
