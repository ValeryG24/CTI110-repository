# Valery Gonzalez
# April 7, 2024
# P1HW2
# This program calculates and displays travel expenses based on user input.
 
# Ask user to enter their budget
budget = float(input("Enter your budget: "))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask user for amount they will spend on gas
gas_expense = float(input("Enter the amount you will spend on gas: "))

# Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Enter the amount you will spend on accommodation: "))

# Ask user for amount they will spend on food
food_expense = float(input("Enter the amount you will spend on food: "))

# Calculate total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display results
print("------Travel Expenses------")
 
print("Destination:", destination)

print("Initial Budget:", budget)

print("Gas Expense:", gas_expense)

print("Accommodation Expense:", accommodation_expense)

print("Food Expense:", food_expense)

print("Total Expenses:", total_expenses)

print("Remaining Budget:", remaining_budget)

