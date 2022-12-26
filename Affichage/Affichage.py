import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


class Affichage:
    #def __init__(self,fenetre):

    # def Exemple(self, fenetre):

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
    def base(self, fenetre, largeur, hauteur, cheminImgCode):

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

        fichierimg = Image.open(cheminImgCode)
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




    def Processus(self, fenetre, largeur, hauteur):

        ft = tkFont.Font(family='Times',size=20)
        Process = tk.Label(fenetre)
        Process["font"] = ft
        Process["fg"] = "#FFFFFF"
        Process["bg"] = "#4C687A"
        Process["text"] = "En simultané"
        Process.place(x=screenwidth/2+30,y=hauteur/9+30,width=screenwidth/2-60,height=50)

        ProcessSep1 = tk.Label(fenetre)
        ProcessSep1["bg"] = "#4C687A"
        ProcessSep1.place(x=screenwidth/2+125,y=hauteur/9+80,width=10,height=650)

        ProcessSep2 = tk.Label(fenetre)
        ProcessSep2["bg"] = "#4C687A"
        ProcessSep2.place(x=screenwidth/2+380,y=hauteur/9+80,width=10,height=650)

        ProcessSep3 = tk.Label(fenetre)
        ProcessSep3["bg"] = "#4C687A"
        ProcessSep3.place(x=screenwidth/2+635,y=hauteur/9+80,width=10,height=650)




    def coucouSimple(self, fenetre, largeur, hauteur):
        self.base(fenetre, largeur, hauteur, "Images/Coucou.png")
        
        #Déclaration de la police
        ft = tkFont.Font(family='Oxygen',size=20)

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
        I5.place(x=largeur/2+30,y=hauteur/9+450,width=largeur/2-60,height=50)

        ft = tkFont.Font(family='Oxygen',size=25)

        Multiplicateur = tk.Label(fenetre)
        Multiplicateur["font"] = ft
        Multiplicateur["fg"] = "#FFFFFF"
        Multiplicateur["bg"] = "#4C687A"
        Multiplicateur["text"] = "x4"
        Multiplicateur.place(x=largeur/2+largeur/2-250,y=hauteur/9+240,width=80,height=190)

    def danseSimple(self, fenetre, largeur, hauteur):

        self.base(fenetre,largeur, hauteur, "Images/Danse.png")

        self.Processus(fenetre,largeur,hauteur)

        ft = tkFont.Font(family='Oxygen',size=20)

        I11 = tk.Label(fenetre)
        I11["font"] = ft
        I11["fg"] = "#FFFFFF"
        I11["bg"] = "#2F5496"
        I11["text"] = "Bras Gauche"
        I11.place(x=largeur/2+30,y=hauteur/9+100,width=200,height=50)

        I12 = tk.Label(fenetre)
        I12["font"] = ft
        I12["fg"] = "#FFFFFF"
        I12["bg"] = "#2F5496"
        I12["text"] = "Bassin"
        I12.place(x=largeur/2+285,y=hauteur/9+100,width=200,height=50)

        I13 = tk.Label(fenetre)
        I13["font"] = ft
        I13["fg"] = "#FFFFFF"
        I13["bg"] = "#2F5496"
        I13["text"] = "Bras Droit"
        I13.place(x=largeur/2+540,y=hauteur/9+100,width=200,height=50)

        I2 = tk.Label(fenetre)
        I2["font"] = ft
        I2["fg"] = "#FFFFFF"
        I2["bg"] = "#2F5496"
        I2["text"] = "Démarrage des moteurs"
        I2.place(x=largeur/2+30,y=hauteur/9+175,width=screenwidth/2-60,height=50)

        I3 = tk.Label(fenetre)
        I3["font"] = ft
        I3["fg"] = "#FFFFFF"
        I3["bg"] = "#2F5496"
        I3["text"] = "Tant que l'utilisateur n'appuie pas sur le clavier"
        I3.place(x=largeur/2+30,y=hauteur/9+250,width=screenwidth/2-60,height=50)

        I11 = tk.Label(fenetre)
        I11["font"] = ft
        I11["fg"] = "#FFFFFF"
        I11["bg"] = "#6495ED"
        I11["text"] = "Mouvement\naléatoire\nde haut\nen bas"
        I11.place(x=largeur/2+50,y=hauteur/9+325,width=160,height=150)

        I12 = tk.Label(fenetre)
        I12["font"] = ft
        I12["fg"] = "#FFFFFF"
        I12["bg"] = "#6495ED"
        I12["text"] = "Rotation\naléatoire"
        I12.place(x=largeur/2+305,y=hauteur/9+350,width=160,height=100)

        I13 = tk.Label(fenetre)
        I13["font"] = ft
        I13["fg"] = "#FFFFFF"
        I13["bg"] = "#6495ED"
        I13["text"] = "Mouvement\naléatoire\nde haut\nen bas"
        I13.place(x=largeur/2+560,y=hauteur/9+325,width=160,height=150)

        I4 = tk.Label(fenetre)
        I4["font"] = ft
        I4["fg"] = "#FFFFFF"
        I4["bg"] = "#6495ED"
        I4["text"] = "Pause aléatoire comprise entre 0.5 et 1 seconde"
        I4.place(x=largeur/2+50,y=hauteur/9+495,width=screenwidth/2-100,height=50)

        I5 = tk.Label(fenetre)
        I5["font"] = ft
        I5["fg"] = "#FFFFFF"
        I5["bg"] = "#2F5496"
        I5["text"] = "Fin tant que (Appuie clavier)"
        I5.place(x=largeur/2+30,y=hauteur/9+565,width=screenwidth/2-60,height=50)

        I6 = tk.Label(fenetre)
        I6["font"] = ft
        I6["fg"] = "#FFFFFF"
        I6["bg"] = "#2F5496"
        I6["text"] = "Arrêt des moteurs"
        I6.place(x=largeur/2+30,y=hauteur/9+635,width=screenwidth/2-60,height=50)


fenetre = tk.Tk()
fenetre.title("LearnoBot") #Titre
fenetre.attributes("-fullscreen",True) #Plein Ecran
fenetre["bg"] = "#FFFFFF"
fenetre.resizable(width=False, height=False)#redimensionnement de la fenetre interdit
screenwidth = fenetre.winfo_screenwidth() #Largeur écran
screenheight = fenetre.winfo_screenheight()#hauteur écran
aff = Affichage()
aff.coucouSimple(fenetre, screenwidth, screenheight)
#aff.danseSimple(fenetre, screenwidth, screenheight)
fenetre.mainloop()
