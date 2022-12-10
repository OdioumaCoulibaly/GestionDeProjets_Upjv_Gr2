from tkinter import *
from tkinter import ttk

class Affichage:

        fenetre = Tk()

        fenetre.title('Learnobot')

        #fenetre.iconbitmap('/Code/logo.ico')

        fenetre.config(bg = '#FFFFFF')

        fenetre.geometry('800x600')

        fenetre.columnconfigure(0, weight=1)
        fenetre.columnconfigure(1, weight=3)

        headerCodeBrut = ttk.Label(fenetre, text="Python")
        headerCodeBrut.grid(column=0, row=0, padx=5, pady=5)

        headerCodeSimple= ttk.Entry(fenetre)
        headerCodeSimple.grid(column=1, row=0, padx=5, pady=5)

        password_label = ttk.Label(fenetre, text="Simplifié")
        password_label.grid(column=0, row=1, padx=5, pady=5)

        password_entry = ttk.Entry(fenetre,  show="*")
        password_entry.grid(column=1, row=1, padx=5, pady=5)

        login_button = ttk.Button(fenetre, text="Login")
        login_button.grid(column=1, row=3, padx=5, pady=5)


        fenetre.mainloop()