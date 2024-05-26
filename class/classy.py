# classes allow to logically group the 
# data and functions in a way that is easy 
# to reuse and easy to build upon

class Employee_Pass:
    pass

# emp1 = Employee_Pass()
# emp2 = Employee_Pass()

# print(emp1)
# print(emp2)

# emp1.first = 'Rainbow'
# emp1.last = 'Dash'

# emp2.first = 'Pinkie'
# emp2.last = 'Pie'

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}{last}@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Rainbow', 'Dash', 50000)
emp2 = Employee_Pass('Pinkie', 'Pie', 60000)

print(emp1.first)
print(emp2.last)