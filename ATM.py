from datetime import datetime

PIN = 12345
balance = 65650
history = []

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_pin = int(input("Enter PIN: "))

    if user_pin == PIN:
        print("PIN Verified\n")

        while True:
            print("\n1. Withdraw")
            print("2. Check Balance")
            print("3. Deposit")
            print("4. Transaction History")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            # ---- WITHDRAW ----
            if choice == 1:
                amount = int(input("Enter withdrawal amount: "))
                if amount > 0 and amount <= balance:
                    balance -= amount
                    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    history.append(f"{time} | Withdraw: {amount} | Balance: {balance}")
                    print("Withdrawal Successful")
                else:
                    print("Invalid or Insufficient Balance")

            # ---- CHECK BALANCE ----
            elif choice == 2:
                time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                history.append(f"{time} | Balance Checked | Balance: {balance}")
                print("Current Balance:", balance)

            # ---- DEPOSIT ----
            elif choice == 3:
                amount = int(input("Enter deposit amount: "))
                if amount > 0:
                    balance += amount
                    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    history.append(f"{time} | Deposit: {amount} | Balance: {balance}")
                    print("Deposit Successful")
                else:
                    print("Invalid deposit amount")

            # ---- TRANSACTION HISTORY ----
            elif choice == 4:
                print("\n--- Transaction History ---")
                if not history:
                    print("No transactions yet.")
                else:
                    for h in history:
                        print(h)

            # ---- EXIT ----
            elif choice == 5:
                print("Thank you for using ATM")
                break

            else:
                print("Invalid choice")

        break

    else:
        attempts += 1
        print(f"Invalid PIN. Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Card Blocked. Too many wrong attempts.")