class Employee:
    def __init__(self,name,age,salary,gender):#_init_acts as a constructor
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def employee_details(self):
        print("Name of Employee is ",self.name)
        print("Age of Employee is ",self.age)
        print("Salary of employee is ",self.salary)
        print("Gender of Employee is ",self.gender)
e1=Employee('Sam',45,50000,"Male")
e1.employee_details()