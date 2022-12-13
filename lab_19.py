def printRow(j):
    for i in range(j):
        if i % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()

for i in range(5,0,-1):
    printRow(i)