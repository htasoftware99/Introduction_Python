class Calculator():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def addition(self):
        return f"{self.x} + {self.y} = {self.x + self.y}"

    def substraction(self):
        return f"{self.x} - {self.y} = {self.x - self.y}"

    def multiply(self):
        return f"{self.x} * {self.y} = {self.x * self.y}"
    
    def divide(self):
        if self.y == 0:
            return "You cannot divide a number to 0"
        else:
            return f"{self.x} / {self.y} = {self.x} / {self.y}"
    
    def power(self):
        return f"{self.x} ^ {self.y} = {self.x ** self.y}"
    
    def root(self):
        return f"{self.x} ^ {(1/self.y)} = {self.x ** (1/self.y)}"

print("""

Choose Operation:

1 - Addition
2 - Substraction
3 - Multiply
4 - Divide
5 - Power
6 - Root
q - Quit Program

""")

operation = input("Chosee Operation: ")
number1 = int(input("First value: "))
number2 = int(input("Second value: "))

calculator = Calculator(number1, number2)

if operation == 1:
    print(calculator.addition(number1, number2))
elif operation == 2:
    print(calculator.substraction())
elif operation == 3:
    print(calculator.multiply())
elif operation == 4:
    print(calculator.divide())
elif operation == 5:
    print(calculator.power())
elif operation == 6:
    print(calculator.root())
else:
    print("Enter a valid value")