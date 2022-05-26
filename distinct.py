class Student():

    def check(self,list):
        list2 = list.copy()
        y=0
        for x in list:
            if x in list2[y+1:len(list)]:
                return True
                print(list2[y+1:len(list)])
            else:
                pass
            y = y + 1


nums =  [1,4,6,8,3,55,88]

student = Student()

print(student.check(nums))