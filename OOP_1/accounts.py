from  student import  StudentMain


class Account(StudentMain):

    def __init__(self, name, dept, sem, credit, per_credit_fees, waiver):
        super(Account, self).__init__(name=name, dept=dept)
        self.__sem = sem
        self.__credit = credit
        self.__per_credit_fees = per_credit_fees
        self.__total_fees = 0.0
        self.__isreg = False
        self.__haveWaiver = waiver

    def chk_waiver(self, amount=0.0):
        if self.__haveWaiver == True:
            self.__total_fees = self.__total_fees - amount

    def first_payble_amount(self):
        return (self.__total_fees*40)/100

    def get_registration(self,payment):
        if self.first_payble_amount() >= payment:
            print(f"Amount {payment} is smaller than {self.first_payble_amount()}")
        else:
            print(f"Weldone,amount{self.first_payble_amount()} have been paid")
            self.__total_fees = self.__total_fees - payment
            self.__isreg = True

    def chk_registered(self):
        return self.__isreg



    def total_amount(self):
        self.__total_fees = self.__credit * self.__per_credit_fees
        return  self.__total_fees






