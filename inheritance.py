class Employee():
    def __init__(self,name,salary,departmant):
        self. name = name
        self.salary = salary
        self.departmant = departmant

    def show_info(self):
        print("Name: {}\nSalary : {} \nDepartmant: {}\n".format(self.name,self.salary,self.departmant))

    def change_departmant(self,new_departmant):
         self.departmant = new_departmant

class Maneger(Employee):
       pass