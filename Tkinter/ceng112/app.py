print("Imported module __name__ is set to: {}".format(__name__))
def functione_One():
    print("Function One")
def functione_Two():
    print("Function Two")

if __name__ == "__main__":
    print("the imported module executed when ran direcly")
else:
    print("the imported module executed when imported")