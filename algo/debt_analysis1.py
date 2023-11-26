import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def prioritize_debt(new_amount_owed, new_interest_rate):
    # Function to generate data for different types of debts for a customer
    def generate_customer_data(num_customers, num_debts_per_customer):
        customer_data = []
        for _ in range(num_customers):
            customer_debts = []
            for i in range(num_debts_per_customer):
                debt_type = random.choice(['Credit Card', 'Housing Loan', 'Personal Loan'])
                if debt_type == 'Credit Card':
                    amount_owed = round(random.uniform(500, 5000), 2)
                    interest_rate = round(random.uniform(0.1, 0.25), 4)
                elif debt_type == 'Housing Loan':
                    amount_owed = round(random.uniform(10000, 200000), 2)
                    interest_rate = round(random.uniform(0.03, 0.08), 4)
                else:
                    amount_owed = round(random.uniform(1000, 10000), 2)
                    interest_rate = round(random.uniform(0.05, 0.15), 4)

                debt = {
                    'Debt Type': debt_type,
                    'Amount Owed': amount_owed,
                    'Interest Rate': interest_rate
                }
                customer_debts.append(debt)

            customer_data.append(customer_debts)
        return customer_data

    # Generate debt data for 100 different customers with 5 debts each
    num_customers = 100
    num_debts_per_customer = 5
    customers_data = generate_customer_data(num_customers, num_debts_per_customer)

    # Create a DataFrame for each customer and concatenate them
    dataframes = []
    for i, customer_debts in enumerate(customers_data):
        df = pd.DataFrame(customer_debts)
        df['Customer ID'] = f'Customer_{i+1}'
        dataframes.append(df)

    final_dataframe = pd.concat(dataframes, ignore_index=True)

    # Label debts based on interest rate
    final_dataframe['Priority'] = final_dataframe['Interest Rate'].apply(lambda x: 'High' if x > 0.1 else 'Low')

    # Prepare data for model training
    X = final_dataframe[['Amount Owed', 'Interest Rate']]
    y = final_dataframe['Priority']

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a decision tree classifier
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # # Make predictions
    # y_pred = clf.predict(X_test)

    # Evaluate the model
    def predict_debt_priority(amount_owed, interest_rate):
        # Assuming 'clf' is your trained decision tree classifier

        # Make predictions for a single new data point
        new_data = [[amount_owed, interest_rate]]
        prediction = clf.predict(new_data)

        # Returning the predicted priority
        return prediction[0]

    predicted_priority = predict_debt_priority(new_amount_owed, new_interest_rate)
    print(f"Priority: {predicted_priority}")
    return f"Priority: {predicted_priority}"

# if __name__ == '__main__':
#     prioritize_debt(300,12)
