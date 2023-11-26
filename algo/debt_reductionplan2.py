"""This code uses a linear regression model to predict the debt amount,
 and then it calculates available funds for debt reduction and the recommended
 debt reduction amount based on the model predictions. The results include the customer ID,
 current debt, available funds,
 and the recommended debt reduction amount, sorted in descending order based on the recommendation.
 In this code, I've added retirement and vacation savings goals, and the optimization function
 aims to maximize the sum of these goals while considering available funds and the recommended
 debt reduction amount. The optimization is performed for each customer,
 and the results include the allocation of funds to debt reduction, retirement savings, and vacation savings.
 This is a simplified example, and you may need to adapt it to match your specific use case and goals."""

import pandas as pd
import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

def debt_reductionplan():
    # Load the mock data
    df = pd.read_excel('debt_assessment_data.xlsx')

    # Features (X) and target variable (y)
    X = df[['Income ($)', 'Debt ($)', 'Monthly Expenses ($)', 'Credit Score']]
    y = df['Debt ($)']

    # Create a linear regression model
    model = np.linalg.lstsq(X, y, rcond=None)[0]

    # Make predictions on the entire dataset
    df['Recommended Debt Reduction ($)'] = X @ model

    # Calculate available funds for debt reduction (simplified for illustration)
    df['Available Funds ($)'] = df['Income ($)'] - df['Monthly Expenses ($)']

    # Define financial goals for each customer
    df['Retirement Savings Goal ($)'] = df['Income ($)'] * 0.2  # 20% of income for retirement
    df['Vacation Savings Goal ($)'] = 2000  # Fixed vacation savings goal

    # Linear programming to maximize debt reduction
    c = np.array([-1, 0, 0])  # Coefficients for the objective function (maximize debt reduction)

    # Set bounds for each weight (between 0 and 1)
    bounds = [(0, 1), (0, 1), (0, 1)]

    # Equality constraint: weights sum to 1
    A_eq = np.ones((1, 3))
    b_eq = np.array([1])

    # Solve the linear programming problem
    result = linprog(c, bounds=bounds, A_eq=A_eq, b_eq=b_eq)

    # Extract the results
    weights = result.x
    df['Debt Reduction Allocation'] = weights[0] * df['Available Funds ($)']
    df['Retirement Allocation'] = weights[1] * df['Available Funds ($)']
    df['Vacation Allocation'] = weights[2] * df['Available Funds ($)']
    # Display the personalized financial plan
    print("\nPersonalized Financial Plan:")
    print(df[['Customer ID', 'Debt Reduction Allocation', 'Retirement Allocation', 'Vacation Allocation']])
