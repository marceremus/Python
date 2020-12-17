#!/usr/bin/env python3


# le mot def pour indiquer qu'il s'agit d'une fonction

# if __name__ == '__main__':

def welcome():
   print("Welcome")

# appel de la fonction

welcome()

def nextYear():
    global year
    print("Fin de l'année ", year)
    year +=1
    print("Début de l'année ", year)


year = 2018

nextYear()
nextYear()
