from tkinter import *
import os
#import tkinter as tk

class Affichage:

        fenetre = Tk()
        canvas = Canvas(fenetre, width=200, height=600)
       
        imgCode = PhotoImage(file="Images/capture.png")
        imgCode = imgCode.zoom(25)
        imgCode = imgCode.subsample(32)

        canvas.create_image(0, 0, anchor=NW, image=imgCode)


        fenetre.iconbitmap("Images/logo.ico")
        fenetre.geometry('800x600')
        fenetre.title('Learnobot')
        fenetre.config(bg = '#FFFFFF')

        ''' 

        panelP.add(Label(fenetre, text="Python", background="blue", anchor=NW))
        panelP.add(Label(fenetre, text="Python", background="red", anchor=NE))
        
        panelP.add(Label(fenetre, image=imgCode)
        panelP.add(LabelFrame(fenetre, text="Pour"))

        '''

        p1 = PanedWindow()
        p1.pack(fill=BOTH, expand=1)

        left = Label(fenetre, image=imgCode)
        p1.add(left)

        p2 = PanedWindow(p1, orient=VERTICAL)
        p1.add(p2)

        top = Label(p2, text="Top Panel")
        p2.add(top)

        codeSimple = LabelFrame(fenetre, text="type mouvement/humeur")
        frameFor = LabelFrame(codeSimple, text="Pour .....").pack()
        frameIf = LabelFrame(codeSimple, text="Si ...").pack()

        p2.add(codeSimple)
                
        p1.pack()

        fenetre.mainloop()      