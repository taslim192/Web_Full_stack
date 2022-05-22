from customer_abstract import Cust_abs


class Customer(Cust_abs):
    def __init__(self,name,age,nid,address):
        self.__name = name
        self.__age = age
        self.__nid = nid
        self.__address = address

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
        
    def get_nid(self):
        return self.__nid
        
    def get_address(self):
        return self.__address

    def print_info(self):
        print(f"             User Information")
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"NID: {self.__nid}")
        print(f"Address: {self.__address}")


# custtomer1 = Customer("ABC",19,117786,"Dhaka")
# name = custtomer1.get_name()
# age = custtomer1.get_age()
# nid = custtomer1.get_nid()
# address = custtomer1.get_address()
# custtomer1.print_info()
# print(f"{name}--{age}--{nid}--{address}")

