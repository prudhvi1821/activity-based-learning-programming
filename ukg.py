balance = 5000
transactions = []
n = int(input("Enter number of transactions: "))
for i in range(n):
    choice = input("Enter deposit or withdraw: ").lower()
    amount = float(input("Enter amount: "))
    if amount <= 0: print("Invalid amount")
    elif choice == "deposit": balance += amount; transactions.append(("Deposit", amount))
    elif choice == "withdraw" and amount <= balance and amount <= 20000: balance -= amount; transactions.append(("Withdrawal", amount))
    else: print("Transaction rejected")
print("\nTransaction Summary:", transactions, "\nFinal Balance: Rs.", balance)