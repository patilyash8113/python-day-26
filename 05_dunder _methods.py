# # # dunder methods are short form of double undercores (also called as magic method)
# # class Emloyee:
# #     def __init__(self,name,salary):
# #         self.name=name
# #         self.salary=salary

# #     def __str__(self):
# #         return f"The name of the Employee is {self.name} And the salary of the Employee is {self.salary}"
# #     def __repr__(self):
# #         return f"Name: {self.name}\nSalary:{self.salary}"
# #     def __len__(self):
# #         return len(self.name)

        
        
    

# # e=Emloyee("Yash patil",50000)

# # print(e.name,e.salary)
# # print(str(e))
# # print(repr(e))
# # print(len(e))

# class employee:
#     def __init__(self,name,salary,years):
#         self.name=name
#         self.salary=salary
#         self.years=years
#     def __str__(self):
#         return f"The name of the employee is {self.name} And the salary of the Employee is {self.salary} and the bond of the employee in company is {self.years}"
#     def __repr__(self):
#         return f"Name:{self.name}\nSalary:{self.salary}\nyears:{self.years}"
#     def __len__(self):
#         return len(self.name)
      
         
# e=employee("Yash",500000,4)
# print(e.name,e.salary,e.years)
# print(str(e))
# print(repr(e))
# print(len(e))

class student:
    def __init__(self,first_name,middle_name,last_name):
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
    def __str__(self):
        return f"The first name of the student is {self.first_name} The middle name of the student is {self.middle_name} and the last name of the student is {self.last_name}"
    
    def __repr__(self):
        return f"First name:{self.first_name}\nMiddle name:{self.middle_name}\nLast name{self.last_name}"
    
    def __len__(self):
        return len(self.first_name)

e=student("Yash","Umesh","Patil")
print(e.first_name,e.middle_name,e.last_name)
print(str(e))
print(repr(e))
print(len(e))