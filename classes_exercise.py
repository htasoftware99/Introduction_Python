class Student:
    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades

student_1 = Student("Hasan", "22", 100)
Student_2 = Student("Mehmet", "18", 50)

print(student_1.grades)
print(Student_2.grades)