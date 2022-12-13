class Car:
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def brandmodel(self):
        return self.brand + " " + self.model

car_1 = Car("Bmw", "x5", 2010) # Car sınıfından car_1 nesnesi oluşturduk.
car_2 = Car("Audi", "Q5", 2012) # Car sınıfından car_2 nesnesi oluşturduk

print(car_1.model)
print(car_2.brandmodel())



    