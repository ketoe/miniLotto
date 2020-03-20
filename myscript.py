import random

"""Random miniLottto
"""

rangeNumber = 49

print("Randint - Lotto Game\n")

while True:
    print("Give me a number from the range 1 - ", rangeNumber, "\n")
    numberUser = input("Number: ")
    randNumber = random.randint(1, rangeNumber)
    if (randNumber == int(numberUser)):
        print("You Won!\n")
    else:
        print("You Lost!\n number sought is ", randNumber, "\n")
