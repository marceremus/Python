import os
import random
import shutil


if os.path.exists("meals.txt"):

    with open("meals.txt", "r+") as fichier:
        mealsList = fichier.readlines()
        mealRandomMeals = random.choice(mealsList)
        print("Je vous propose aujoud'hui, le repas suivant :", mealRandomMeals )
        fichier.close()

else:
    print("Attention le document n'existe pas ")


    # fichier = open("students.txt", "w+")
    # fichier.write("Carla\n")
    # fichier.write("Paul\n")
    # fichier.write("Kevin\n")

    # fichier.close()

    #studentsList = ["Paule", "Mathieu", "Eduard"]

    #with open("students.txt", "a+") as fichier:

    #    for student in studentsList:
    #        fichier.write(student + "\n")

    #    fichier.close()
        # fichier.write("Pauline\n")
        # fichier.write("Maxime\n")
        # fichier.write("Sami\n")
