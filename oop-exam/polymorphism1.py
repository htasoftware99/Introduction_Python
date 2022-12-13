class Person:
    def __init__(self,name):
        self.name = name
    def designation(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Employee(Person):
    def designation(self):
        return "software engineer"

class Doctor(Person):
    def designation(self):
        return "Cardiologist"

class Student(Person):
    def designation(self):
        return "Graduate Engineer"

persons = [Employee("hasan"), Doctor("mehmet"), Student("alp")]
for person in persons:
    print(person.name + ":" + person.designation())