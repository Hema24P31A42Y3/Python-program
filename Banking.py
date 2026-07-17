balance = 1000

while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Deposit Successful!")
            print("Current Balance:", balance)
        else:
            print("Invalid amount!")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            print("Withdrawal Successful!")
            print("Current Balance:", balance)

    elif choice == 3:
        print("Current Balance:", balance)

    elif choice == 4:
