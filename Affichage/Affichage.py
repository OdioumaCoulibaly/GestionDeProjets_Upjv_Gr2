import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


class Affichage:

    def For(self,fenetre, x, y, largeur, hauteur, contenu):
        LabelFor = tk.Label(fenetre)
        ft = tkFont.Font(family='Times',size=20)
        LabelFor["font"] = ft
        LabelFor["fg"] = "#FFFFFF"
        LabelFor["bg"] = "#2F5496"
        LabelFor["anchor"] = "w"
        LabelFor["text"] = "Pour "+ contenu
        LabelFor.place(x=x,y=y,width=largeur,height=hauteur)

    def FinFor(self,fenetre, x, y, largeur, hauteur):
        LabelFor = tk.Label(fenetre)
        ft = tkFont.Font(family='Times',size=20)
        LabelFor["font"] = ft
        LabelFor["fg"] = "#FFFFFF"
        LabelFor["bg"] = "#2F5496"
        LabelFor["anchor"] = "w"
        LabelFor["text"] = "Fin du Pour"
        LabelFor.place(x=x,y=y,width=largeur,height=hauteur)

    def If(self,fenetre, x, y, largeur, hauteur, contenu):
        LabelIf = tk.Label(fenetre)
        ft = tkFont.Font(family='Times',size=20)
        LabelIf["font"] = ft
        LabelIf["fg"] = "#FFFFFF"
        LabelIf["bg"] = "#2F5496"
        LabelIf["anchor"] = "w"
        LabelIf["text"] = "Si "+ contenu +" Alors"
        LabelIf.place(x=x,y=y,width=largeur,height=hauteur)

    def FinIf(self,fenetre, x, y, largeur, hauteur):
        LabelIf = tk.Label(fenetre)
        ft = tkFont.Font(family='Times',size=20)
        LabelIf["font"] = ft
        LabelIf["fg"] = "#FFFFFF"
        LabelIf["bg"] = "#2F5496"
        LabelIf["anchor"] = "w"
        LabelIf["text"] = "Fin du Si"
        LabelIf.place(x=x,y=y,width=largeur,height=hauteur) 

    def Corps(self,fenetre, x, y, largeur, hauteur, contenu):
        LabelIf = tk.Label(fenetre)
        ft = tkFont.Font(family='Times',size=20)
        LabelIf["font"] = ft
        LabelIf["fg"] = "#FFFFFF"
        LabelIf["bg"] = "#2F5496"
        LabelIf["anchor"] = "nw"
        LabelIf["text"] = contenu
        LabelIf.place(x=x,y=y,width=largeur,height=hauteur)

    def __init__(self, fenetre):

        screenwidth = fenetre.winfo_screenwidth() #Largeur écran
        screenheight = fenetre.winfo_screenheight()#hauteur écran

        TitreLabelPython=tk.Label(fenetre)
        ft = tkFont.Font(family='Times',size=20)
        TitreLabelPython["font"] = ft
        TitreLabelPython["fg"] = "#FFFFFF"
        TitreLabelPython["bg"] = "#2F5496"
        TitreLabelPython["justify"] = "center"
        TitreLabelPython["text"] = "Code Python"
        TitreLabelPython["borderwidth"] = 10
        TitreLabelPython.place(x=0,y=0,width=screenwidth/2,height=screenheight/9)

        TitreLabelCodeSimple=tk.Label(fenetre)
        TitreLabelCodeSimple["font"] = ft
        TitreLabelCodeSimple["fg"] = "#FFFFFF"
        TitreLabelCodeSimple["bg"] = "#2F5496"
        TitreLabelCodeSimple["justify"] = "center"
        TitreLabelCodeSimple["text"] = "Code Simplifié"
        TitreLabelCodeSimple.place(x=screenwidth/2,y=0,width=screenwidth/2,height=screenheight/9)

        fichierimg = Image.open("Images/testCapture.png")
        image = ImageTk.PhotoImage(fichierimg)

        ImageCode = tk.Label(image=image)
        ImageCode.image = image

        ft = tkFont.Font(family='Times',size=10)
        ImageCode["font"] = ft
        ImageCode["fg"] = "#333333"
        ImageCode["bg"] = "#9FA6AD"
        ImageCode["anchor"] = "nw"
        ImageCode["text"] = "label"
        ImageCode.place(x=0,y=screenheight/9,width=screenwidth/2,height=(screenheight-(screenheight/9)))

        
        SeparationV=tk.Label(fenetre)
        SeparationV["bg"] = "#022D59"
        SeparationV.place(x=(screenwidth/2)-1,y=0,width=2,height=screenheight)

        SeparationL=tk.Label(fenetre)
        SeparationL["bg"] = "#022D59"
        SeparationL.place(x=0,y=(screenheight/9)-1,width=screenwidth,height=2)

        self.For(fenetre, screenwidth/2+25, (screenheight/10)+25, screenwidth/2-50, 50, 'faire un test')
        self.If(fenetre, screenwidth/2+50, (screenheight/10)+100, screenwidth/2-75, 50, 'quelque chose se produit')
        self.Corps(fenetre, screenwidth/2+75, (screenheight/10)+175, screenwidth/2-100, 400, "Le contenu peut être très et est vraiment \n Lonnnnnnnnnnnnnn\nnnnnnnnnnnnnnnnn\nnnnnnnnnnnnnnnnnnnnnnnnn\nnnnnnnnnnnnnnnnnnnnnnnnn\nnn\nnnnnnnnnnnnnnnnnnnn\nnnnnnnnnnnnnnnnnn\nnnnnnnnnnnn\nnnnnnnnnnnng ^^")
        self.FinIf(fenetre, screenwidth/2+50, screenheight-screenheight/10-75, screenwidth/2-75, 50)
        self.FinFor(fenetre, screenwidth/2+25, screenheight-screenheight/10, screenwidth/2-50, 50)
    
fenetre = tk.Tk()
fenetre.title("LearnoBot") #Titre
fenetre.attributes("-fullscreen",True) #Plein Ecran
fenetre["bg"] = "#FFFFFF"
fenetre.resizable(width=False, height=False)#redimensionnement de la fenetre interdit
Affichage(fenetre)
fenetre.mainloop()
