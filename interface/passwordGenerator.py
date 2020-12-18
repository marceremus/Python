from random import randint, choice
from tkinter import *
import string


def generatePassword():
    passMin = 8
    passMax = 15
    allChars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(allChars) for x in range(randint(passMin, passMax)))
    passwordEntry.delete(0, END)
    passwordEntry.insert(0, password)

# création de la fenetre
window = Tk();
colorBg = "#3e3f42"
window.title("Générateur de mot de passe")
window.geometry("900x600")
window.iconbitmap('logo.png')
window.config(background=colorBg)

# frame principale
frame = Frame(window, bg=colorBg)

# création d'image
width = 300
height = 300
image = PhotoImage(file="logo.png").zoom(35).subsample(32)

canvas = Canvas(frame, width=width, height=height, bg=colorBg, bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creation de la sous boite
rightFrame = Frame(frame, bg=colorBg)
# rightFrame.pack()

# creation d'un titre

label_titre = Label(rightFrame, text="Mot de passe", font=("Arial", 20), bg=colorBg, fg="white")
label_titre.pack()

# creation d'un input
passwordEntry = Entry(rightFrame, font=("Arial", 20), bg=colorBg, fg="white", bd=1, highlightthickness=0)
passwordEntry.pack()

# creatio nd'un btn
generatPasswordButton = Button(rightFrame, text="Générer", font=("Arial", 20), bg="white", fg=colorBg, command=generatePassword)
generatPasswordButton.pack(fill=X)

rightFrame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)

# creation de la barre du menu
menuBar = Menu(window)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Nouveau", command=generatePassword)
fileMenu.add_command(label="Fermer", command=window.quit)

menuBar.add_cascade(label="Fichier", menu=fileMenu)

# configuration de la fenetre
window.config(menu=menuBar)

window.mainloop()