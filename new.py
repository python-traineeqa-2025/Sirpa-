# import keyword
#
# print(keyword.kwlist)
#
# snake_case=0
# camelCase=2
#
# #int
# c='4'
# #list
# a=[1,2,3]
#
# #tuple
# a=(3,4,5)
#
# #dictionary values
# d={'a':'1'}
#
class Employee:
    def __init__(self,fname,lname,email):
        self.firstN=fname
        self.lastN=lname
        self.email=email

    def greet_person(self):
        print("Hello"+self.firstN)

emp1=Employee('manish','verma','manish@gmail.com')
print(emp1.firstN)
emp1.greet_person()
