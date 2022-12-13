class Turkey():
    def capital(self):
        print("Ankara")
    def language(self):
        print("Turkish")
    def type(self):
        print("developing")

class USA():
    def capital(self):
        print("Washington DC")
    def language(self):
        print("English")
    def type(self):
        print("developed")

obj_turkey = Turkey()
obj_usa = USA()

for country in (obj_turkey, obj_usa):
    country.capital()
    country.language()
    country.type()