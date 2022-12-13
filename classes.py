class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def brandmodel(self):
        return f'Araba markası: {self.brand} ve modeli: {self.model}'

car_1 = Car("bmw", "i5", "2010")
car_2 = Car("audi","a5","2011")

print(car_1.brand)
print(car_2)
print(car_1.brandmodel())

print("-----------------------------------------------")

class Movie:
    def __init__(self,name,director):
        self.name = name
        self.director = director

movie_1 = Movie("Money heist","Hasan")
movie_2 = Movie("Walking dead", "Hasan")
print(movie_1.name)
print(movie_1.director)
