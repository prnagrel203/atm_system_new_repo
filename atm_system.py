""" ATM System """
class ATM:
    """
    create class ATM
    """
    def __init__(self, name, account_no, balance=2000):
        """
        This Method Create Account
        """
        self.name = name
        self.account_no = account_no
        self.balance = balance
        if account_no:
            number = len(str(account_no)) == 12
            print("Your Balance Is:", number)
        else:
            print("Enter Proper Account No")

    def account_details(self):
        """
        Account Details shows details of account holders
        """
        print("Account Holder:", self.name)
        print("Account Number:", self.account_no)
        print("Initial Balance:", self.balance)

    def withdraw(self, amount):
        """
        Withdraw Method shows withdraw amount of account holder
        """
        self.amount = amount
        if self.balance >= self.amount:
            print("Withdraw Amount:", self.amount)
            self.balance = self.balance - self.amount
            print("Balance After Withdraw Amount:", self.balance)
        else:
            print(" InValid Amount")

    def deposit(self, amount):
        """
        Deposit Method for calculating account holder balance after deposit amount
        """
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Balance After Amount Deposit:", self.balance)

    def balance_check(self):
        """
        This Method For Checking The Method
        """
        print("Your Account Balance Is:", self.balance)

    def transaction_exit(self):
        """
        This Method is for exist from Transaction
        """
        print("Transaction Is Over")

    def option_details(self):
        """
        Different option according people need in system
        """
        while True:
            try:
                print("MENU: \n 1.Account Details \n 2.Withdraw \n 3.Deposit \n 4.BalanceCheck \n 5.Exit")
                option = int(input("Select Option:"))
                if option == 1:
                    A1.account_details()
                elif option == 2:
                    pin = int(input("ENTER THE 4-DIGIT PIN:"))
                    amount = int(input("Enter Withdraw Amount:"))
                    if 1000 <= pin <= 9999:
                        A1.withdraw(amount)
                elif option == 3:
                    amount = int(input("Enter Deposit Amount:"))
                    A1.deposit(amount)
                elif option == 4:
                    A1.balance_check()
                elif option == 5:
                    A1.transaction_exit()
                else:
                    print("ERROR: select between 1 to 5")
            except TypeError:
                print("OOPS:Something Went Wrong In System")
NAME = input("Enter The Name:")
ACCOUNT_NO = int(input("Enter The Account Number:"))

A1 = ATM(NAME, ACCOUNT_NO)
A1.option_details()
