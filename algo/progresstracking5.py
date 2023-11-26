import matplotlib.pyplot as plt

def progresstracking(initial_loan_amount, monthly_payment):


    # List to track remaining loan amount over time
    remaining_loan = [initial_loan_amount]

    # Calculate the remaining loan amount for each month
    while remaining_loan[-1] > 0:
        remaining = remaining_loan[-1] - monthly_payment
        if remaining < 0:
            remaining = 0
        remaining_loan.append(remaining)

    # Generate x-axis (months)
    months = list(range(len(remaining_loan)))

    # Plotting the loan reduction progress
    plt.figure(figsize=(10, 6))
    plt.plot(months, remaining_loan, marker='o', linestyle='-')
    plt.title('Loan Reduction Progress')
    plt.xlabel('Months')
    plt.ylabel('Remaining Loan Amount ($)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('progress.png')
    return plt

# if __name__ == '__main__':
#     # Initial loan amount and monthly payment
#     initial_loan_amount = 10000
#     monthly_payment = 500
#     progresstracking(initial_loan_amount, monthly_payment)
