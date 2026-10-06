from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        print("10000 per month")

class Full_time_employee(Employee):
    def calculate_salary(self):
        print("50000 per month")

class Contract_employee(Employee):
    def calculate_salary(self):
        print("30000 per month")

Inter = Intern()
full_time = Full_time_employee()
contract = Contract_employee()

Inter.calculate_salary()
full_time.calculate_salary()
contract.calculate_salary()