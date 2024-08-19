# ATM Machine Software NON GUI Based
class ATM:
    
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        User_input = int(input("""HOW WOULD YOU LIKE TO PROCEED:
        1.ENTER 1 TO CREATE PIN
        2.ENTER 2 TO DEPOSIT MONEY
        3.ENTER 3 TO WITHDRAW MONEY
        4.ENTER 4 TO CHECK BALANCE
        5.ENTER 5 TO EXIT
         """))
        if User_input == 1:
            self.create_pin()
        elif User_input == 2:
            self.deposit_money()
        elif User_input == 3:
            self.withdraw()
        elif User_input == 4:
            self.Balance_check()
        else:
            print("EXIT")
    def create_pin(self):
        self.pin = int(input("ENTER PIN:-"))
        print("PIN GENERATED SUCCESSFULLY :)")
        self.menu()
    def deposit_money(self):
        Pin = int(input("ENTER THE PIN TO PROCEED:-"))
        if Pin == self.pin:
            amount = int(input("ENTER THE AMOUNT TO BE DEPOSITED :-"))
            self.balance += amount
            print("MONEY DEPOSITED SUCCESSFULLY :)")
        else:
            print("INVALID PIN")

        self.menu()
    def withdraw(self):
        Pin = int(input("ENTER THE PIN TO PROCEED:-"))
        if Pin == self.pin:
            amount = int(input("ENTER THE AMOUNT TO BE WITHDRAWN :-"))
            if amount <= self.balance:
                self.balance -= amount
                print("MONEY WITHDRAWN SUCCESSFULLY :)")
            else:
                print("INSUFFICIENT FUNDS :)")
        else:
            print("INVALID PIN")
        self.menu()
    
    def Balance_check(self):
        Pin = int(input("ENTER THE PIN TO PROCEED:-"))
        if Pin == self.pin:
            print("THE CURRENT BALANCE IS :-",self.balance)
        else:
            print("INVALID PIN")
        self.menu()


sbi = ATM()





