class Employee:
    def _init_(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id


    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

