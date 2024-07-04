import random

def Main():

    print("Who are you?")
    names = input()
    print("Hello, {0}!".format(names))

    heads = 0
    tails = 0

    print("Tossing a coin...")

    for i in range(3):
        print("Round" + " " + str(i+1) + ":" + " ",end=" ")
        if random.randint(0,100) % 2 == 0:
            print("Heads")
            heads += 1
        else :
            print("Tails")
            tails += 1
    print("Heads: {0}, Tails: {1}".format(heads,tails))

    if heads > tails:
        print("{0} won!".format(names))
    else :
        print("{0} Lose!".format(names))

Main()