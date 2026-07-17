

#This logic for ATM mechine

def  ATM( Balance):
    #Balance = 5000
    print("""
            ===ATM===
          1.Check Balance
          2.Diposit
          3.Withdraw
          4.Exit
          """)
    print("Select What you Want to do ?")
    a =int(input("Reply only integer numbers :"))
    if a == 1:
        print("Your Balance is :",Balance,"TK")

    elif a == 2:
        b = int(input("Enter your Ammount:"))
        Balance = Balance + b
        print("Your Deposit is Succesfull")
        print("Your current Balance is",Balance,"TK")

    elif a == 3:
        withdraw = int(input("Enter your Withdrawal ammount:"))
        if withdraw > Balance:
            print("Your Balance is Low, please try Again")
        else:
            print("Your Withdraw is Succesfull")
            Balance = Balance - withdraw
            print("Your Curent Balance is:",Balance,"TK")

    elif a ==4:
        print("Exit Succesfull")

    else:
        print("Invalid Input")

ATM(1000)
ATM(444)