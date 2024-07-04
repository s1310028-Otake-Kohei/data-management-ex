import random

def Main():
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

Main()