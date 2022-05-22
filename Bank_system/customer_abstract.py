from abc import  ABC,abstractmethod
class Cust_abs(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def get_nid(self):
        pass
    
    @abstractmethod
    def get_address(self):
        pass

