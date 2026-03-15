import random
import json

def save_data(accounts, PATH):
    with open(PATH, "w") as file:
        json.dump(accounts, file , indent=4)

def delete_account(accounts, PATH):
    print("\n------ Delete Account ------")

    number = int(input("Enter Account Number: "))
    pin = int(input("Enter PIN: "))

    if number in accounts and accounts[number]["pin"] == pin:
        confirm = input("Are you sure you want to delete this account? (yes/no): ")

        if confirm.lower() == "yes":
            del accounts[number]   # remove account
            save_data(accounts, PATH)
            print("Account deleted successfully.")
        else:
            print("Deletion cancelled.")

    else:
        print("Invalid account number or PIN.")

def atm():
    PATH=r"E:\ATM MEACHIN PROJECT\Data/accounts.json.txt"
    # Load accounts from file
    try:
        with open(PATH, "r") as file:
            accounts = json.load(file)
            accounts = {int(k): v for k, v in accounts.items()}
    except:
        accounts = {}
    
    while True:
        
        print("\n------ ATM MENU ------")
        print("1. Create Account")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Balance Enquiry")
        print("5. Delete Account")
        print("6. Exit")
        A1=input("Enter here:")
        A=int(A1)
        if A==1:
            print("Enter your details:")
            Account_name=input("Enter your name: ")
            age=int(input("Enter your age:"))
            id_proof=int(input("Enter your Id Number:"))
            account_number = random.randint(100000000000, 999999999999)
            print(F"Your account no: {account_number}")
            while True:
                create_pin = input("Create 4 digit PIN: ")
                if len(create_pin) == 4 and create_pin.isdigit():
                    create_pin = int(create_pin)
                    break
                else:
                    print("PIN must be exactly 4 digits.")
            balance=int(input("Enter your first balance:"))
            accounts[account_number] = {
                "name": Account_name,
                "age": age,
                "pin": create_pin,
                "balance": balance
            }
            # Save to file
            save_data(accounts, PATH)

            print("Account created successfully!")
        elif A==2:
                if not accounts:
                    print("Please create account first.")
                else:
                    while True:
                        B=input("Press 1 to continue or type exit: ").lower()

                        if B=="exit":
                            break
                        else:
                            account_numbers=int(input("Enter your account no: "))
                            pin = int(input("Enter your PIN: "))
                            if account_numbers in accounts and accounts[account_numbers]["pin"] == pin:
                                amount=int(input("Enter amount:"))
                                if amount <= accounts[account_numbers]["balance"]:
                                    accounts[account_numbers]["balance"] -= amount
                                    save_data(accounts, PATH)
                                    print(f"Now your available balance: {accounts[account_numbers]['balance']}")
                                else:
                                    print("Insufficient balance in your account.")

                            else:
                                print("Incorrect PIN")
        elif A==3:
                if not accounts:
                    print("Please create account first.")
                else:
                    while True:
                        B=input("Press 1 to continue or type exit: ").lower()
                        
                    
                        if B=="exit":
                            break
                        else:
                            account_numbers=int(input("Enter your account no: "))
                            pin = int(input("Enter your PIN: "))
                            if account_numbers in accounts and accounts[account_numbers]["pin"] == pin:
                                amount=int(input("Enter amount:"))
                                accounts[account_numbers]["balance"] += amount
                                save_data(accounts, PATH)
                                print(f"Now available balance in your account: {accounts[account_numbers]['balance']}")
                            else:
                                print("Incorrect PIN")
        elif A==4:
                if not accounts:
                    print("Please create account first.")
                else:
                    account_numbers=int(input("Enter your account no: "))
                    pin = int(input("Enter your PIN: "))

                    if account_numbers in accounts and accounts[account_numbers]["pin"] == pin:
                        print(f"Your balance is {accounts[account_numbers]['balance']}")
                    else:
                        print("Incorrect PIN")
        elif A==5:
            delete_account(accounts, PATH)
        elif A==6:
             break
        else:
             print("Invalid option.")
atm()