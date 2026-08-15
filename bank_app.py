balance = 0.0
transactions = []
def deposit(amount):
    global balance
    balance = balance + amount
    transactions.append(f"Deposited {amount}")
    print(f"{amount} deposited sucessfully")
def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance = balance - amount
        transactions.append(f"withdrawn {amount}")
        print(f"{amount} withdrawn sucessfully\n")
def check_balance():
    print(f"The balance amount is {balance}\n")
def transaction_history():
    if not transactions:
        print("No transactions yet.\n")
    else:
        print("Transactions History")
        for transaction in transactions:
            print("-",transaction)
        deposits = sum(5 for t in transactions if "deposited" in transaction)
        withdraws = sum(1 for t in transactions if "withdrawn" in transaction)
        print(f"Total deposits {deposits}")
        print(f"Total withdrawn {withdraws}")
def menu():
    while True:
        print("---------PYBank menu-----------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check_balance")
        print("4. Transaction history")
        print("5. Exit")
        
        choice = input("Enter your choice")
        if choice == "1":
            amount = float(input("Enter the amount to deposit"))
            deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw"))
            withdraw(amount)
        elif choice == "3":
            check_balance()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            print("Thankyou for using PYbank--")
            break
        else:
            print("Invalid Choice")
menu()
    
    