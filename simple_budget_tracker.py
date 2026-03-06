# Monthly Budget Program with Multiple Expenses

budget = float(input("Enter your total monthly budget: "))

total_expenses = 0

while True:
    expense = input("Enter an expense (type 'done' to finish): ")
    
    if expense.lower() == "done":
        break
    
    try:
        expense_amount = float(expense)
        total_expenses += expense_amount
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

remaining_balance = budget - total_expenses

print("---------------------------")
print("Total Budget      :", budget)
print("Total Expenses    :", total_expenses)
print("Remaining Balance :", remaining_balance)

if remaining_balance < 500:
    print("Warning: Low Funds")
    
print("---------------------------")