from tkinter import *
import webbrowser


# création de la fenetre

def openSiteWeb():
    webbrowser.open_new("https://approom.io")


window = Tk()

# titre
window.title("My application")
window.geometry("1200x900")
window.minsize(900, 600)
window.iconbitmap("logo.ico")
window.config(background="#3e3f42")

# frame = Frame(window, bg="#3e3f42", bd=1, relief=SUNKEN)
frame = Frame(window, bg="#3e3f42")

# texte
labelTitle = Label(frame, text="Mon premier application", font=("Arial", 40), bg="#3e3f42", fg="white")
labelTitle.pack()

# texte
labelTitleSubTitle = Label(frame, text="Lorem ipsum", font=("Arial", 18), bg="#3e3f42", fg="white")
labelTitleSubTitle.pack()

frame.pack(expand=YES)

ytButton = Button(frame, text="Open YouTube", bg="white", fg="#3e3f42", pady=20, padx=20, command=openSiteWeb)
ytButton.pack(pady=250, fill=X)

# affichage de la fenetre
window.mainloop()
