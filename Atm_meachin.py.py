import random
def atm():
    
    create_pin = None
    number = None
    balance = 0
    while True:
        print("\n------ ATM MENU ------")
        print("1. Create Account")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Balance Enquiry")
        print("5. Exit")
        
        A=int(input("Enter here: "))
        if A==1:
            print("Enter your details:")
            Account_name=input("Enter your name: ")
            age=int(input("Enter your age:"))
            id_proof=int(input("Enter your Id Number:"))
            number = random.randint(100000000000, 999999999999)
            print(F"Your account no: {number}")
            while True:
                create_pin = input("Create 4 digit PIN: ")
                if len(create_pin) == 4 and create_pin.isdigit():
                    create_pin = int(create_pin)
                    break
                else:
                    print("PIN must be exactly 4 digits.")
            balance=int(input("Enter your first balance:"))
            print("Account created successfully!")
        elif A==2:
                if number is None:
                    print("Please create account first.")
                else:
                    while True:
                        B=input("Press 1 to continue or type exit: ").lower()
                        account_number=int(input("Enter your account no: "))
                        pin = int(input("Enter your PIN: "))
                    
                        if B=="exit":
                            break
                        else:
                            if pin == create_pin and account_number == number:
                                amount=int(input("Enter amount:"))
                                if amount<=balance:
                                    balance-=amount
                                    print(f"Now your available balance:{balance} ")
                                else:
                                    print("Insufficient balance in your account.")

                            else:
                                print("Incorrect PIN")
        elif A==3:
                while True:
                    B=input("Press 1 to continue or type exit: ").lower()
                    account_number=int(input("Enter your account no: "))
                    pin = int(input("Enter your PIN: "))
                    
                    if B=="exit":
                         break
                    else:

                        if pin == create_pin and account_number == number:
                            amount=int(input("Enter amount:"))
                            balance+=amount
                            print(f"Now available balance in your account{balance}")
                        else:
                            print("Incorrect PIN")
        elif A==4:
                account_number=int(input("Enter your account no: "))
                pin = int(input("Enter your PIN: "))

                if pin == create_pin and account_number == number:
                    print(f"your balance is {balance}")
                else:
                    print("Incorrect PIN")
        elif A==5:
             break
        else:
             print("Invalid option.")
atm()