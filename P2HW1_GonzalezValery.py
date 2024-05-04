# Valery Gonzalez
# April 14, 2024
# P2HW1
# This program calculates and displays travel expenses based on user input.
 
# Ask user to enter their budget
budget = float(input("Enter your budget: "))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask user for amount they will spend on gas
gas_expense = float(input("Enter the amount you will spend on gas: "))

# Ask user for amount they will need for accommodation/hotel
accommodation_expense = float(input("Enter the amount you will spend on accommodation: "))

# Ask user for amount they will spend on food
food_expense = float(input("Enter the amount you will spend on food: "))

# Calculate total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display results
print("---------- Travel Expenses ----------")
 
print("Location:\t        {}".format(destination))

print("Initial Budget:\t        ${:.2f}".format(budget))

print("Fuel:\t                ${:.2f}".format(gas_expense))

print("Accommodation:\t        ${:.2f}".format(accommodation_expense))

print("Food:\t                ${:.2f}".format(food_expense))
print("-------------------------------------")
 

print("Remaining Balance:\t${:.2f}".format(remaining_budget))
