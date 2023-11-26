"""
One way to create an AI-powered financial coaching system is by implementing a rule-based chatbot.
You can use Python along with libraries like NLTK for natural language processing and scikit-learn
 for text classification. Below is an example using rule-based responses:
"""
import random
import re

# Define coaching tips based on patterns in user inputred
coaching_tips = {
    r'.*\breduce\b.*\bexpenses\b.*': "Consider creating a budget and tracking your expenses to identify areas to cut down.",
    r'.*\bincrease\b.*\bincome\b.*': "Explore part-time gigs or freelancing opportunities to supplement your income.",
    r'.*\bconsolidate\b.*\bdebts\b.*': "Look into consolidating high-interest debts to lower rates and simplify payments.",
    r'.*\bsave\b.*\bmoney\b.*': "Automate savings by setting aside a fixed amount from each paycheck into a savings account.",
    r'.*\binvest\b.*': "Consider investing in low-cost index funds or other diversified investment options for long-term growth.",
    r'.*\bretirement\b.*': "Start planning for retirement early by contributing regularly to retirement accounts.",
    r'.*\bemergency\b.*\bfund\b.*': "Setting up an emergency fund is crucial. Aim for 3 to 6 months' worth of expenses saved in a separate account."
}

def get_coaching_tip(user_input):
    for pattern, tip in coaching_tips.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            return tip
    return "I'm sorry, I don't have specific advice on that at the moment."

def main():
    print("AI Financial Coach: How can I assist you today? (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("AI Financial Coach: Goodbye!")
            break

        tip = get_coaching_tip(user_input)
        print(f"AI Financial Coach: {tip}")

if __name__ == "__main__":
    main()
