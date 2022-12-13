class Employee:
    def raisee(self):
        raise_rate = 0.1
        result = 100+100*raise_rate
        print("Employee: ", result)

class CompEng(Employee):
    def raisee(self):
        raise_rate = 0.2
        result = 100+100*raise_rate
        print("Computer Engineer: ", result)

class EEE(Employee):
    def raisee(self):
        raise_rate = 0.3
        result = 100+100*raise_rate
        print("Electrical Engineer: ", result)

e1 = Employee()
ce = CompEng()
eee = EEE()

employee_list = [ce, eee]
for employee in employee_list:
    employee.raisee()
