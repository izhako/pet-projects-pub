# classes allow to logically group the 
# data and functions in a way that is easy 
# to reuse and easy to build upon
import datetime
# Class method as alternative constructor
# e.g. from str
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
    raise_amount = 1.04
    num_of_employees = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}{last}@company.com"
        Employee.num_of_employees += 1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_str_1 = 'Ruby-Rod-777777'
emp_str_2 = 'Super Woman 1000000'

new_emp_1 = Employee.from_string(emp_str_1)

print(Employee.num_of_employees)
emp1 = Employee('Rainbow', 'Dash', 50000)
emp2 = Employee('Pinkie', 'Pie', 60000)
emp3 = Employee('Cookie', 'Monster', 800000)

print(emp1.first)
print(emp2.last)

emp2.fullname()
Employee.set_raise_amt(1.05)
print(emp2.raise_amount)

emp1.fullname()
Employee.fullname(emp1)

print(Employee.num_of_employees)
print(emp3)

print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

# To increase the raise amount for all instances
Employee.raise_amount = 1.05
print(emp1.__dict__) # namespace of the instance
# Class variables - variables that are shared among all the instances of a class
print(emp1.raise_amount)
print(emp2.raise_amount)

emp1.raise_amount = 1.07
print(emp1.raise_amount)
print(emp2.raise_amount)

my_date = datetime.date(2024, 5, 26)
print(Employee.is_workday(my_date))