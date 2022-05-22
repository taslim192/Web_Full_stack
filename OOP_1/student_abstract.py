from abc import ABC, abstractmethod


class StudentAbstract:

    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_dept(self):
        pass

    @abstractmethod
    def get_sem(self):
        pass

