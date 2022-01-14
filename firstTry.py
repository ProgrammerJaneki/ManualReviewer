import random
import sqlite3
from time import sleep
import os
import sys


def printHW():
    print("Hello World")
    print("This is running..")
    print(1 + 1)


printHW()

for count in range(1, 11):
    print(f"No: {count}")
thisList = [1, 10]
print(thisList)

# separate


class Person:
    def __init__(self, fname, age):
        self.fname = fname
        self.age = age

    def __repr__(self):
        return f"Name: {self.fname} || Age: {self.age}"


fperson = Person("Jannel", 21)
print(fperson)


class Subjects:
    questions = {}

    def __init__(self, term="", definition=""):
        self.term = term
        self.definition = definition

    def addTD(self, term, definition):
        self.questions.update({term: definition})

    def printTD(self):
        for i in self.questions:
            print(f"TERM: {i} \nDEFINITION: {self.questions[i]}\n")


subj1 = Subjects()
subj1.addTD("Integers", "Words")
subj1.addTD("Strings", "Words")
subj1.addTD("Sampaguita", "Flower")
subj1.printTD()

table = "Computer Architecture"
print(table.replace(" ", ""))

thisTable = "try Table"
print(thisTable.replace(" ", ""))


def returnFalse():
    return True


if returnFalse() == True:
    print("True")
else:
    print("False")


def getOut():
    out = False
    while not out:
        choice = int(input("\n\t\t1.) Exit the program\t\t2.) Back\n>> "))
        if choice == 1:
            out = True
            return True
        elif choice == 2:
            out = True
            return False
        sleep(0.5)
        os.system('clear')


print("====")
# print(getOut())


def tryMain():
    print("First Module's Name: {}".format(__name__))


if __name__ == '__main__':
    tryMain()

#import dbase
sampleString = "ThIs iS sO BEautIfuL"
print(sampleString.lower())
