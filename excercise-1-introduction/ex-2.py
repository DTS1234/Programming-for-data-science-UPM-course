# I Create a program for printing
# *
# ***
# *****
# *******
# *********

from importlib.machinery import FrozenImporter

def printLevel(level):
    for i in range (0, level):
        print("*", end="")

def printStairsOfLevel(level:int):
    for i in range (1, level*2, 2):
        printLevel(i)
        print('')

printStairsOfLevel(5)
