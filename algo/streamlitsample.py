import streamlit as st
import pandas as pd
from PIL import Image
from debt_analysis1 import prioritize_debt
from debtconsolidation4 import debtconsolidation
from financialcoachingusingchatGPT import financialliteracy
from progresstracking5 import progresstracking
from datetime import datetime

username = "Customer 1"
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
if username:
    col1, col2 = st.columns([0.65, 0.35])
    with col1:
        icon_path = r"C:\Users\GT953WB\PycharmProjects\Canarahackathon\algo\canara.png"  # Replace with your image file path
        with open(icon_path, 'rb') as f:
            icon_bytes = f.read()
        st.image(icon_bytes, caption='Icon', width = 100)
    with col2:
        st.write("")  # Empty space for alignment
        st.write(f"Logged in as:: <span style='color: blue;'>{username}</span>", unsafe_allow_html=True)
        st.write(f"Logged in time: <span style='color: blue;'>{current_time}</span>", unsafe_allow_html=True)


# Title of the app
st.markdown(
    """
    <h1 style='color: darkblue;'>Smart Financial Health Assistant</h1>
    """,
    unsafe_allow_html=True
)
# st.title('Smart Financial Health Assistant')

st.header('Debt Priority Planner: Organize Your Financial Focus')
# Input fields for user to enter data
user_input1 = st.text_input("Enter your Debt amount:", "")
user_input2 = st.text_input("Rate of interest:", "")
if user_input1 and user_input2:
    # Get response from the function
    response = prioritize_debt(user_input1, user_input2)
    # Display the response
    st.write("Response:")
    st.write(response)

st.header('Debt Consolidation Opportunities:')
# debts_in_cluster,current_interest_rate,consolidated_interest_rate =
debtdf = debtconsolidation()
debtdf = debtdf.drop(['Current Interest Rate'], axis=1)
st.table(debtdf)


st.title("Loan Reduction Process")
st.write("This app visualizes the progress of reducing a loan over time.")
# progress tracking
initial_loan_amount = st.text_input("initial_loan_amount:", "")
monthly_payment = st.text_input("monthly_payment:", "")
# initial_loan_amount = 10000
# monthly_payment = 500
if initial_loan_amount and monthly_payment:
    plt = progresstracking(int(initial_loan_amount), int(monthly_payment))
    st.pyplot(plt)




# financial coaching
st.title('financial coaching chatbot')
# User input for chatting
user_input = st.text_input("You:", "")

if user_input:
    # Get the bot's response based on user input
    bot_response = financialliteracy(user_input)

    # Display the bot's response

    st.markdown("""
    <style>
        .wide-textarea {
            width: 1000px;
            height: 10000px; /* Adjust height as needed */
        }
    </style>
    """, unsafe_allow_html=True)
    st.text_area("Bot:", bot_response)

