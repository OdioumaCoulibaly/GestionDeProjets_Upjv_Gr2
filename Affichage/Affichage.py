import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


class Affichage:
    #def __init__(self,fenetre):

    # def Exemple(self, fenetre):

       

    #     #Processus

    #     # Process = tk.Label(fenetre)
    #     # ft = tkFont.Font(family='Times',size=20)
    #     # Process["font"] = ft
    #     # Process["fg"] = "#FFFFFF"
    #     # Process["bg"] = "#2F5496"
    #     # Process["anchor"] = "nw"
    #     # Process["text"] = "Processus"
    #     # Process.place(x=screenwidth/2+25,y=hauteur/9+15,width=screenwidth/2-50,height=100)

    #     # ProcessSep1 = tk.Label(fenetre)
    #     # ProcessSep1["bg"] = "#2F5496"
    #     # ProcessSep1["text"] = "111111111111"
    #     # ProcessSep1.place(x=screenwidth/2+25,y=hauteur/9+115,width=15,height=400)

    #     # ProcessSep2 = tk.Label(fenetre)
    #     # ProcessSep2["bg"] = "#2F5496"
    #     # ProcessSep2["text"] = "2222222222222"
    #     # ProcessSep2.place(x=screenwidth/2+(screenwidth/2)/2,y=hauteur/9+115,width=15,height=400)

    #     # ProcessSep3 = tk.Label(fenetre)
    #     # ProcessSep3["bg"] = "#2F5496"
    #     # ProcessSep3["text"] = "3333333333333"
    #     # ProcessSep3.place(x=screenwidth/2+largeur/2-40,y=hauteur/9+115,width=15,height=400)
        
    #     PourTantque = tk.Label(fenetre)
    #     ft = tkFont.Font(family='Times',size=20)
    #     PourTantque["font"] = ft
    #     PourTantque["fg"] = "#FFFFFF"
    #     PourTantque["bg"] = "#2F5496"
    #     PourTantque["anchor"] = "nw"
    #     PourTantque["text"] = "Pour / Tant Que"
    #     PourTantque.place(x=largeur/2+25,y=hauteur/9+15,width=largeur/2-50,height=50)

    #     ligne = tk.Label(fenetre)
    #     ligne["bg"] = "#2F5496"
    #     ligne["text"] = "idhzidihzl"
    #     ligne.place(x=largeur/2+25,y=hauteur/9+65,width=15,height=300)

    #     #Si = tk.Label(fenetre) idem pour tant que


    
    #     #Corps = tk.Label(fenetre)
    def base(self, fenetre, largeur, hauteur):

        Fondheader = tk.Label(fenetre)
        Fondheader["bg"] = "#022D59"
        Fondheader.place(x=0,y=0,width=largeur,height=hauteur/9)

        TitreLabelPython=tk.Label(fenetre)
        ft = tkFont.Font(family='Times',size=36)
        TitreLabelPython["font"] = ft
        TitreLabelPython["fg"] = "#FFFFFF"
        TitreLabelPython["bg"] = "#2F5496"
        TitreLabelPython["justify"] = "center"
        TitreLabelPython["text"] = "Code Python"
        TitreLabelPython["borderwidth"] = 10
        TitreLabelPython.place(x=5,y=5,width=largeur/2-10,height=hauteur/9-10)

        TitreLabelCodeSimple=tk.Label(fenetre)
        TitreLabelCodeSimple["font"] = ft
        TitreLabelCodeSimple["fg"] = "#FFFFFF"
        TitreLabelCodeSimple["bg"] = "#2F5496"
        TitreLabelCodeSimple["justify"] = "center"
        TitreLabelCodeSimple["text"] = "Code Simplifié"
        TitreLabelCodeSimple.place(x=largeur/2+5,y=5,width=largeur/2-10,height=hauteur/9-10) 

        fichierimg = Image.open("Images/Coucou.png")
        imageResize = fichierimg.resize(((largeur//2),(hauteur-hauteur//9)), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imageResize)

        ImageCode = tk.Label(image=image)
        ImageCode.image = image

        ft = tkFont.Font(family='Times',size=10)
        ImageCode["font"] = ft
        ImageCode["fg"] = "#333333"
        ImageCode["bg"] = "#9FA6AD"
        ImageCode["anchor"] = "nw"
        ImageCode["text"] = "label"
        ImageCode.place(x=0,y=hauteur/9-1,width=largeur/2,height=(hauteur-(hauteur/9)))

        
        SeparationV=tk.Label(fenetre)
        SeparationV["bg"] = "#022D59"
        SeparationV.place(x=(largeur/2),y=0,width=5,height=hauteur)

        SeparationL=tk.Label(fenetre)
        SeparationL["bg"] = "#022D59"
        SeparationL.place(x=0,y=(hauteur/9)-1,width=largeur,height=2)

    def coucouSimple(self, fenetre, largeur, hauteur):
        self.base(fenetre, largeur, hauteur)
        
        #Déclaration de la police
        ft = tkFont.Font(family='Oxygen',size=20)

        # Fond = tk.Label(fenetre)
        # Fond["bg"] = "#9FA6AD"
        # Fond.place(x=largeur/2+25,y=hauteur/9+25,width=largeur/2-50,height=hauteur-(hauteur/9) - 25 )


        I1 = tk.Label(fenetre)
        I1["font"] = ft
        I1["fg"] = "#FFFFFF"
        I1["bg"] = "#2F5496"
        I1["text"] = "Démarrage du moteur controllant le bras gauche"
        I1.place(x=largeur/2+30,y=hauteur/9+170,width=largeur/2-60,height=50)

        I2 = tk.Label(fenetre)
        I2["font"] = ft
        I2["fg"] = "#FFFFFF"
        I2["bg"] = "#2F5496"
        I2["anchor"] = "nw"
        I2["text"] = "Le bras gauche se lève"
        I2.place(x=largeur/2+30,y=hauteur/9+240,width=largeur/2-300,height=50)

        I3 = tk.Label(fenetre)
        I3["font"] = ft
        I3["fg"] = "#FFFFFF"
        I3["bg"] = "#2F5496"
        I3["anchor"] = "nw"
        I3["text"] = "Pause d'une seconde ou moins"
        I3.place(x=largeur/2+30,y=hauteur/9+310,width=largeur/2-300,height=50)

        I4 = tk.Label(fenetre)
        I4["font"] = ft
        I4["fg"] = "#FFFFFF"
        I4["bg"] = "#2F5496"
        I4["anchor"] = "nw"
        I4["text"] = "Le bras gauche se baisse"
        I4.place(x=largeur/2+30,y=hauteur/9+380,width=largeur/2-300,height=50)

        I5 = tk.Label(fenetre)
        I5["font"] = ft
        I5["fg"] = "#FFFFFF"
        I5["bg"] = "#2F5496"
        I5["text"] = "Arrêt du moteur controllant le bras gauche"
        I5.place(x=largeur/2+30,y=hauteur/9+450,width=largeur/2-50,height=50)

        ft = tkFont.Font(family='Oxygen',size=25)

        Multiplicateur = tk.Label(fenetre)
        Multiplicateur["font"] = ft
        Multiplicateur["fg"] = "#FFFFFF"
        Multiplicateur["bg"] = "#4C687A"
        Multiplicateur["text"] = "x4"
        Multiplicateur.place(x=largeur/2+largeur/2-250,y=hauteur/9+300,width=80,height=80)

fenetre = tk.Tk()
fenetre.title("LearnoBot") #Titre
fenetre.attributes("-fullscreen",True) #Plein Ecran
fenetre["bg"] = "#FFFFFF"
fenetre.resizable(width=False, height=False)#redimensionnement de la fenetre interdit
screenwidth = fenetre.winfo_screenwidth() #Largeur écran
screenheight = fenetre.winfo_screenheight()#hauteur écran
aff = Affichage()
aff.coucouSimple(fenetre, screenwidth, screenheight)
fenetre.mainloop()
