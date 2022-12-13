class Student:

    school_name = "x School"
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def average(self):
        return sum(self.grade) / len(self.grade)

    def schoolName(self):
        return self.school_name

student_1 = Student("John", 20, [100, 10, 80]) # student_1 aynı zamanda instance(örnekleme nedir)
student_2 = Student("Jane", 19, [90, 10, 80]) # student_2 aynı zamanda instance(örnekleme nedir)

for student in [student_1, student_2]:
    print(student.name, student.age, "Average: " ,student.average())

print(Student.school_name)
print(student_1.school_name)
print(student_2.school_name)
print(student_1.__dict__) # __dict__ nesnesi örnekleme nesnesinin özelliklerini listeler.



