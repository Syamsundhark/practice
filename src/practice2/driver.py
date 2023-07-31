from src.practice2.util import *
if __name__ == "_main_":
    emp = Employee(1, "sunny", 50000)
    print(f"{emp.get_name()} (ID: {emp.get_emp_id()}) earns ${emp.get_salary()} per year.")
