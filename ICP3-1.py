#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Employee:
    num_employees = 0
    
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.num_employees += 1
        
    def employeeInfomation(self):
        print(f"Name: {self.name}\nFamily: {self.family}\nSalary: {self.salary}\nDepartment: {self.department}")
        
    
    def averagesalary(employees):
        total_salary = sum(employee.salary for employee in employees)
        return total_salary / len(employees)

class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department, experience_years):
        super().__init__(name, family, salary, department)
        self.experience_years = experience_years


employee1 = Employee("ali", "khan", 50000, "HR")
employee2 = Employee("Janu", "jain", 60000, "IT")
fulltime_employee1 = FulltimeEmployee("Aravind", "rao", 100000, "software", 3)
fulltime_employee2 = FulltimeEmployee("nani", "reddy", 75000, "Finance", 5)

# Calling member functions
print("Employee 1 Info:")
employee1.employeeInfomation()

print("Fulltime Employee 2 Info:")
fulltime_employee2.employeeInfomation()
employees = [employee1, employee2, fulltime_employee1, fulltime_employee2]
avg_salary = Employee.averagesalary(employees)

print(f"Average Salary: {avg_salary:.2f}")
print(f"Total Number of Employees: {Employee.num_employees}")


# In[ ]:




