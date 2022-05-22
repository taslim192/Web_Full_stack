from student_abstract import  StudentAbstract


class StudentMain(StudentAbstract):

    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept

    def get_name(self):
        return self.__name

    def get_dept(self):
        return self.__dept

    def get_semister(self):
        sem = "6th"
        return sem


student = StudentMain("Taslim", "CSE")
print(student.get_name())
print(student.get_dept())

