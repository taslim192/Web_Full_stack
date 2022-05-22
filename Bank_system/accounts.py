from logging import exception
from customer_imp import Customer


class Savings_accounts(Customer):
    def __init__(self,name, age, nid, address,account_no,open_bal):
        super().__init__(name, age, nid, address)
        self.__account_no = account_no
        self.__open_bal = open_bal
        self.__current_bal = self.__open_bal
        self.__dep_amount = 0
        self.__with_amount = 0

    def get_account(self):
        return self.__account_no

    def get_account(self):
        return self.__open_bal

    def deposit(self,dep_amount):
        self.__dep_amount = dep_amount
        self.__current_bal = self.__current_bal + dep_amount
        return self.__current_bal,self.__dep_amount

    def withdraw(self,with_amount):
        self.__with_amount = with_amount
        if self.__current_bal >= with_amount:
            self.__current_bal = self.__current_bal - with_amount
            return self.__current_bal,self.__with_amount
        else:
            exception("Invalid Amount")

    def print_adata(self):
        print(f"            Accounts Information")
        print(f"Account No: {self.__account_no}")
        print(f"Opening Balance: {self.__open_bal}")
        print(f"Current Balance: {self.__current_bal}")
        print(f"Last Deposit Amount: {self.__dep_amount}")
        print(f"Last Withdrw Amount: {self.__with_amount}")

account1 = Savings_accounts("Taslim",30,117786,"Dhaka",10001,5050)
account1.print_info()
account1.deposit(1000)
account1.withdraw(1050)
account1.print_adata()


account1 = Savings_accounts("Tuhin",25,217786,"Magura",20001,3050)
account1.print_info()
account1.deposit(1000)
account1.withdraw(1050)
account1.print_adata()

account1 = Savings_accounts("Tanvir",23,317786,"Khulna",30001,1050)
account1.print_info()
account1.deposit(1000)
account1.withdraw(1050)
account1.print_adata()
    
    
