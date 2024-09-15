def ATM_Machine():
    balance = 1000
    print("Welcome to ATM")
    PIN = 1234
    attempts = 3
    transactions = []  # List to store transaction history

    while attempts > 0:
        try:
            Enter_PIN = int(input("Enter PIN: "))
            if Enter_PIN == PIN:
                print("PIN verified")
                flag = True
                break
            else:
                attempts -= 1
                print(f"Invalid PIN. You have {attempts} attempts left.")
        except ValueError:
            print("Please enter a valid integer for the PIN.")

    if attempts == 0:
        print("Too many invalid attempts. Exiting.")
        return

    while flag:
        print("\n1. Balance Enquiry\n2. Withdraw\n3. Deposit\n4. PIN Change\n5. Transaction History\n6. Exit\n")
        try:
            option = int(input("Enter Your operation: "))
            if option == 1:
                print(f"Your current balance is {balance}")
                transactions.append(f"Balance Check")
            elif option == 2:
                Withdraw_Amount = int(input("Enter amount to withdraw: "))
                if 0 < Withdraw_Amount <= balance:
                    balance -= Withdraw_Amount
                    transactions.append(f"Withdrawn: {Withdraw_Amount}")  # Add withdrawal to transaction history
                    print(f"After withdrawal, your balance is {balance}")
                else:
                    print("Invalid withdrawal amount.")
            elif option == 3:
                Deposit_Amount = int(input("Enter amount to deposit: "))
                if Deposit_Amount > 0:
                    balance += Deposit_Amount
                    transactions.append(f"Deposited: {Deposit_Amount}")  # Add deposit to transaction history
                    print(f"After deposit, your balance is {balance}")
                else:
                    print("Invalid deposit amount.")
            elif option == 4:
                new_pin = int(input("Enter new PIN: "))
                PIN = new_pin
                transactions.append(f"PIN changed")
                print("PIN changed successfully.")
            elif option == 5:
                print("Transaction History:")
                for transaction in transactions:
                    print(transaction)
            elif option == 6:
                print("Thank you! Visit again.")
                flag = False
            else:
                print("Invalid operation. Please try again.")
        except ValueError:
            print("Please enter a valid integer for the operation.")

ATM_Machine()