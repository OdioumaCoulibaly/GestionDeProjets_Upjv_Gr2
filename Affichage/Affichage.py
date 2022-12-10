#from tkinter import *
import tkinter as tk

class Affichage:

        fenetre = tk.Tk()

        #print(rcpath('../Images/logo.ico'))
        #icone = tk.PhotoImage(file='..\Images\logo.ico')
        #fenetre.tk.call('wm', 'iconphoto', fenetre._w, icone)

        fenetre.geometry('800x600')

        fenetre.title('Learnobot')

        fenetre.config(bg = '#FFFFFF')

        fenetre.columnconfigure(0, weight=1)
        fenetre.columnconfigure(1, weight=3)

        headerCodeBrut = tk.Label(fenetre, text="Python")
        headerCodeBrut.grid(column=0, row=0, padx=5, pady=5)

        headerCodeSimple= tk.Label(fenetre, text="Code Simplifié")
        headerCodeSimple.grid(column=1, row=0, padx=5, pady=5)

        CodePython = tk.Label(fenetre, text="Ici du code Python")
        CodePython.grid(column=0, row=1, padx=5, pady=5)

        CodeSimple = tk.Label(fenetre, text="Ici des briques de codes simplifié")
        CodeSimple.grid(column=1, row=1, padx=5, pady=5)

        fenetre.mainloop()