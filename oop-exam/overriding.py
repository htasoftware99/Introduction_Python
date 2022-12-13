class Employee:
    def raisee(self):
        raise_rate = 0.1
        return 100+100*raise_rate

class CENG(Employee):
    def raisee(self):
        raise_rate = 0.2
        return 100 + 100*raise_rate

class EEE(Employee):
    def raisee(self):
        raise_rate = 0.3
        return 100+100*raise_rate

e1 = Employee()
ce = CENG()
eee = EEE()

print("Employee: ", e1.raisee())
print("Computer Engineer: ", ce.raisee())
print("Electrical Engineer: ", eee.raisee())