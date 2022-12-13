from abc import ABC, abstractmethod
class Players(ABC):
    def __init__(self, name, surname, team):
        self.name = name
        self.surname = surname
        self.team = team

    @abstractmethod
    def health(self):
        return 100

    @abstractmethod
    def use_bomb(self):
        print("I'm throwing a bomb")

class Enemies(Players):
    def __init__(self, name, surname, team, weapon):
        super().__init__(name, surname, team)
        self.weapon = weapon
    
    def health(self):
        return 100

    def use_bomb(self):
        print("I'm throwing a bomb")

class Friends(Players):
    def __init__(self, name,surname, team, weapon):
        super().__init__(name, surname, team)
        self.weapon = weapon

    def health(self):
        return 100

    def use_bomb(self):
        print("I'm throwing a bomb")

enemy1 = Enemies("John", "Hans", "Enemy", "Ak-47")
print(enemy1.name)
print(enemy1.surname)
print(enemy1.team)
print(enemy1.weapon)
print(enemy1.health())
print(enemy1.use_bomb())
print("------------------------")
friend1 = Friends("Hasan", "Tugra", "Friend", "MPT-76")
print(friend1.name)
print(friend1.surname)
print(friend1.team)
print(friend1.weapon)
print(friend1.health())
print(friend1.use_bomb())