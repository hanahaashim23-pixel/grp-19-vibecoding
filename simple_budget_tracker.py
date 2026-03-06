# Monthly Budget Program with Low Funds Warning

budget = float(input("Enter your total monthly budget: "))

expense1 = float(input("Enter expense 1: "))
expense2 = float(input("Enter expense 2: "))
expense3 = float(input("Enter expense 3: "))

total_expenses = expense1 + expense2 + expense3
remaining_balance = budget - total_expenses

print("---------------------------")
print("Total Budget      :", budget)
print("Total Expenses    :", total_expenses)
print("Remaining Balance :", remaining_balance)

if remaining_balance < 500:
    print("Warning: Low Funds")
    
print("---------------------------")