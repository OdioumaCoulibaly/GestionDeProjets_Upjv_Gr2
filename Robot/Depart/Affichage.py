import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


class Affichagefen:

    #Méthode pour la base de chaque affichage
    def base(self, fenetre, largeur, hauteur, cheminImgCode):

        #création des en-tête
        Fondheader = tk.Label(fenetre)
        Fondheader["bg"] = "#022D59"
        Fondheader.place(x=0,y=0,width=largeur,height=hauteur/9)

        TitreLabelPython=tk.Label(fenetre)
        ft = tkFont.Font(family='Oxygen',size=36)
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

        #création de l'image et recadrage de celle-ci

        fichierimg = Image.open(cheminImgCode)
        imageResize = fichierimg.resize(((largeur//2),(hauteur-hauteur//9)), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imageResize)

        ImageCode = tk.Label(image=image)
        ImageCode.image = image

        ft = tkFont.Font(family='Oxygen',size=10)
        ImageCode["font"] = ft
        ImageCode["fg"] = "#333333"
        ImageCode["bg"] = "#9FA6AD"
        ImageCode["anchor"] = "nw"
        ImageCode["text"] = ""
        ImageCode.place(x=0,y=hauteur/9-1,width=largeur/2,height=(hauteur-(hauteur/9)+10))

        #Bande de séparation entre les différentes zones

        SeparationV=tk.Label(fenetre)
        SeparationV["bg"] = "#022D59"
        SeparationV.place(x=(largeur/2),y=0,width=5,height=hauteur)

        SeparationL=tk.Label(fenetre)
        SeparationL["bg"] = "#022D59"
        SeparationL.place(x=0,y=(hauteur/9)-1,width=largeur,height=2)


    #Méthode similaire à base mais celle-ci permet de changer la hauteur de l'image (utile pour les humeurs qui sont de petites fonction)
    def baseAlt(self, fenetre, largeur, hauteur, cheminImgCode, hautimg):

        Fondheader = tk.Label(fenetre)
        Fondheader["bg"] = "#022D59"
        Fondheader.place(x=0,y=0,width=largeur,height=hauteur/9)

        TitreLabelPython=tk.Label(fenetre)
        ft = tkFont.Font(family='Oxygen',size=36)
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
        imageResize = fichierimg.resize(((largeur//2),hautimg), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imageResize)

        ImageCode = tk.Label(image=image)
        ImageCode.image = image

        ft = tkFont.Font(family='Oxygen',size=10)
        ImageCode["font"] = ft
        ImageCode["fg"] = "#C9D1D9"
        ImageCode["bg"] = "#000000"
        ImageCode["text"] = ""
        ImageCode.place(x=0,y=hauteur/9-1,width=largeur/2,height=(hauteur-(hauteur/9))+10)

        
        SeparationV=tk.Label(fenetre)
        SeparationV["bg"] = "#022D59"
        SeparationV.place(x=(largeur/2),y=0,width=5,height=hauteur)

        SeparationL=tk.Label(fenetre)
        SeparationL["bg"] = "#022D59"
        SeparationL.place(x=0,y=(hauteur/9)-1,width=largeur,height=2)

    #Méthode créant l'affichage de la structure avec trois processus 
    def Processus3(self, fenetre, largeur, hauteur):

        #le processus
        ft = tkFont.Font(family='Oxygen',size=20)
        Process = tk.Label(fenetre)
        Process["font"] = ft
        Process["fg"] = "#FFFFFF"
        Process["bg"] = "#4C687A"
        Process["text"] = "En simultané"
        Process.place(x=screenwidth/2+30,y=hauteur/9+100,width=screenwidth/2-60,height=50)

        #les trois séparateurs
        ProcessSep1 = tk.Label(fenetre)
        ProcessSep1["bg"] = "#4C687A"
        ProcessSep1.place(x=screenwidth/2+125,y=hauteur/9+150,width=10,height=600)

        ProcessSep2 = tk.Label(fenetre)
        ProcessSep2["bg"] = "#4C687A"
        ProcessSep2.place(x=screenwidth/2+380,y=hauteur/9+150,width=10,height=600)

        ProcessSep3 = tk.Label(fenetre)
        ProcessSep3["bg"] = "#4C687A"
        ProcessSep3.place(x=screenwidth/2+635,y=hauteur/9+150,width=10,height=600)

    #Comme processus3 mais avec 2 séparateurs
    def Processus2(self, fenetre, largeur, hauteur):

        #le processus
        ft = tkFont.Font(family='Oxygen',size=20)
        Process = tk.Label(fenetre)
        Process["font"] = ft
        Process["fg"] = "#FFFFFF"
        Process["bg"] = "#4C687A"
        Process["text"] = "En simultané"
        Process.place(x=largeur/2+30,y=hauteur/9+100,width=largeur/2-60,height=50)

        #les séparateurs
        ProcessSep1 = tk.Label(fenetre)
        ProcessSep1["bg"] = "#4C687A"
        ProcessSep1.place(x=largeur/2+125,y=hauteur/9+150,width=10,height=550)

        ProcessSep2 = tk.Label(fenetre)
        ProcessSep2["bg"] = "#4C687A"
        ProcessSep2.place(x=largeur/2+635,y=hauteur/9+150,width=10,height=550)

    #L'action coucou simplifié
    def coucouSimple(self, fenetre, largeur, hauteur):
        self.base(fenetre, largeur, hauteur, "./Images/Coucou.png")
        
        #Déclaration de la police
        ft = tkFont.Font(family='Oxygen',size=20)

        I0 = tk.Label(fenetre)
        I0["font"] = ft
        I0["fg"] = "#FFFFFF"
        I0["bg"] = "#4C687A"
        I0["text"] ="Détection vocale ou appel depuis l'application mobile"
        I0.place(x=largeur/2+30,y=hauteur/9+170,width=largeur/2-60,height=50)

        I1 = tk.Label(fenetre)
        I1["font"] = ft
        I1["fg"] = "#FFFFFF"
        I1["bg"] = "#2F5496"
        I1["text"] = "Démarrage du moteur controllant le bras gauche"
        I1.place(x=largeur/2+30,y=hauteur/9+240,width=largeur/2-60,height=50)

        I2 = tk.Label(fenetre)
        I2["font"] = ft
        I2["fg"] = "#FFFFFF"
        I2["bg"] = "#2F5496"
        I2["anchor"] = "nw"
        I2["text"] = "Le bras gauche se lève"
        I2.place(x=largeur/2+30,y=hauteur/9+310,width=largeur/2-300,height=50)

        I3 = tk.Label(fenetre)
        I3["font"] = ft
        I3["fg"] = "#FFFFFF"
        I3["bg"] = "#2F5496"
        I3["anchor"] = "nw"
        I3["text"] = "Pause d'une seconde ou moins"
        I3.place(x=largeur/2+30,y=hauteur/9+380,width=largeur/2-300,height=50)

        I4 = tk.Label(fenetre)
        I4["font"] = ft
        I4["fg"] = "#FFFFFF"
        I4["bg"] = "#2F5496"
        I4["anchor"] = "nw"
        I4["text"] = "Le bras gauche se baisse"
        I4.place(x=largeur/2+30,y=hauteur/9+450,width=largeur/2-300,height=50)

        I5 = tk.Label(fenetre)
        I5["font"] = ft
        I5["fg"] = "#FFFFFF"
        I5["bg"] = "#2F5496"
        I5["text"] = "Arrêt du moteur controllant le bras gauche"
        I5.place(x=largeur/2+30,y=hauteur/9+520,width=largeur/2-60,height=50)

        ft = tkFont.Font(family='Oxygen',size=25)

        Multiplicateur = tk.Label(fenetre)
        Multiplicateur["font"] = ft
        Multiplicateur["fg"] = "#FFFFFF"
        Multiplicateur["bg"] = "#4C687A"
        Multiplicateur["text"] = "x4"
        Multiplicateur.place(x=largeur/2+largeur/2-250,y=hauteur/9+310,width=80,height=190)
        
    def reset(self, fenetre, largeur, hauteur):
        I0 = tk.Label(fenetre)
        I0["bg"] = "#FFFFFF"
        I0.place(x=0,y=0,width=largeur,height=hauteur)
        
    #L'action danse simplifié
    def danseSimple(self, fenetre, largeur, hauteur):
        
        self.base(fenetre,largeur, hauteur, "./Images/Danse.png")
        self.Processus3(fenetre,largeur,hauteur)

        ft = tkFont.Font(family='Oxygen',size=20)

        I0 = tk.Label(fenetre)
        I0["font"] = ft
        I0["fg"] = "#FFFFFF"
        I0["bg"] = "#4C687A"
        I0["text"] ="Détection vocale ou appel depuis l'application mobile"
        I0.place(x=largeur/2+30,y=hauteur/9+30,width=largeur/2-60,height=50)

        I11 = tk.Label(fenetre)
        I11["font"] = ft
        I11["fg"] = "#FFFFFF"
        I11["bg"] = "#2F5496"
        I11["text"] = "Bras Gauche"
        I11.place(x=largeur/2+30,y=hauteur/9+175,width=200,height=50)

        I12 = tk.Label(fenetre)
        I12["font"] = ft
        I12["fg"] = "#FFFFFF"
        I12["bg"] = "#2F5496"
        I12["text"] = "Bassin"
        I12.place(x=largeur/2+285,y=hauteur/9+175,width=200,height=50)

        I13 = tk.Label(fenetre)
        I13["font"] = ft
        I13["fg"] = "#FFFFFF"
        I13["bg"] = "#2F5496"
        I13["text"] = "Bras Droit"
        I13.place(x=largeur/2+540,y=hauteur/9+175,width=200,height=50)

        I2 = tk.Label(fenetre)
        I2["font"] = ft
        I2["fg"] = "#FFFFFF"
        I2["bg"] = "#2F5496"
        I2["text"] = "Démarrage des moteurs"
        I2.place(x=largeur/2+30,y=hauteur/9+250,width=screenwidth/2-60,height=50)

        I3 = tk.Label(fenetre)
        I3["font"] = ft
        I3["fg"] = "#FFFFFF"
        I3["bg"] = "#2F5496"
        I3["text"] = "4 fois les mouvements :"
        I3.place(x=largeur/2+30,y=hauteur/9+325,width=screenwidth/2-60,height=50)

        I11 = tk.Label(fenetre)
        I11["font"] = ft
        I11["fg"] = "#FFFFFF"
        I11["bg"] = "#6495ED"
        I11["text"] = "Mouvement\nen haut\npuis en bas"
        I11.place(x=largeur/2+50,y=hauteur/9+400,width=160,height=150)

        I12 = tk.Label(fenetre)
        I12["font"] = ft
        I12["fg"] = "#FFFFFF"
        I12["bg"] = "#6495ED"
        I12["text"] = "Rotation\naléatoire"
        I12.place(x=largeur/2+305,y=hauteur/9+425,width=160,height=100)

        I13 = tk.Label(fenetre)
        I13["font"] = ft
        I13["fg"] = "#FFFFFF"
        I13["bg"] = "#6495ED"
        I13["text"] = "Mouvement\n à droite\npuis à gauche"
        I13.place(x=largeur/2+560,y=hauteur/9+400,width=160,height=150)

        I4 = tk.Label(fenetre)
        I4["font"] = ft
        I4["fg"] = "#FFFFFF"
        I4["bg"] = "#6495ED"
        I4["text"] = "Pause aléatoire 1 seconde"
        I4.place(x=largeur/2+50,y=hauteur/9+565,width=screenwidth/2-100,height=50)

        I5 = tk.Label(fenetre)
        I5["font"] = ft
        I5["fg"] = "#FFFFFF"
        I5["bg"] = "#2F5496"
        I5["text"] = "Fin si CTRL+C OU fin de la boucle"
        I5.place(x=largeur/2+30,y=hauteur/9+635, width=screenwidth/2-60,height=50)

        I6 = tk.Label(fenetre)
        I6["font"] = ft
        I6["fg"] = "#FFFFFF"
        I6["bg"] = "#2F5496"
        I6["text"] = "Arrêt des moteurs"
        I6.place(x=largeur/2+30,y=hauteur/9+705,width=screenwidth/2-60,height=50)

    #L'action tektonic simplifié
    def tektonikSimple(self, fenetre, largeur, hauteur):
        
        self.base(fenetre,largeur, hauteur, "./Images/Tektonik.png")
        self.Processus3(fenetre,largeur,hauteur)

        ft = tkFont.Font(family='Oxygen',size=20)

        I0 = tk.Label(fenetre)
        I0["font"] = ft
        I0["fg"] = "#FFFFFF"
        I0["bg"] = "#4C687A"
        I0["text"] ="Détection vocale ou appel depuis l'application mobile"
        I0.place(x=largeur/2+30,y=hauteur/9+30,width=largeur/2-60,height=50)

        I11 = tk.Label(fenetre)
        I11["font"] = ft
        I11["fg"] = "#FFFFFF"
        I11["bg"] = "#2F5496"
        I11["text"] = "Bras Gauche"
        I11.place(x=largeur/2+30,y=hauteur/9+175,width=200,height=50)

        I12 = tk.Label(fenetre)
        I12["font"] = ft
        I12["fg"] = "#FFFFFF"
        I12["bg"] = "#2F5496"
        I12["text"] = "Bassin"
        I12.place(x=largeur/2+285,y=hauteur/9+175,width=200,height=50)

        I13 = tk.Label(fenetre)
        I13["font"] = ft
        I13["fg"] = "#FFFFFF"
        I13["bg"] = "#2F5496"
        I13["text"] = "Bras Droit"
        I13.place(x=largeur/2+540,y=hauteur/9+175,width=200,height=50)

        I2 = tk.Label(fenetre)
        I2["font"] = ft
        I2["fg"] = "#FFFFFF"
        I2["bg"] = "#2F5496"
        I2["text"] = "Démarrage des moteurs"
        I2.place(x=largeur/2+30,y=hauteur/9+250,width=screenwidth/2-60,height=50)

        I3 = tk.Label(fenetre)
        I3["font"] = ft
        I3["fg"] = "#FFFFFF"
        I3["bg"] = "#2F5496"
        I3["text"] = "4 fois les mouvements :"
        I3.place(x=largeur/2+30,y=hauteur/9+325,width=screenwidth/2-60,height=50)

        I11 = tk.Label(fenetre)
        I11["font"] = ft
        I11["fg"] = "#FFFFFF"
        I11["bg"] = "#6495ED"
        I11["text"] = "Mouvement\naléatoire\nde haut\nen bas"
        I11.place(x=largeur/2+50,y=hauteur/9+400,width=160,height=150)

        I12 = tk.Label(fenetre)
        I12["font"] = ft
        I12["fg"] = "#FFFFFF"
        I12["bg"] = "#6495ED"
        I12["text"] = "Rotation\naléatoire"
        I12.place(x=largeur/2+305,y=hauteur/9+425,width=160,height=100)

        I13 = tk.Label(fenetre)
        I13["font"] = ft
        I13["fg"] = "#FFFFFF"
        I13["bg"] = "#6495ED"
        I13["text"] = "Mouvement\naléatoire\nde haut\nen bas"
        I13.place(x=largeur/2+560,y=hauteur/9+400,width=160,height=150)

        I4 = tk.Label(fenetre)
        I4["font"] = ft
        I4["fg"] = "#FFFFFF"
        I4["bg"] = "#6495ED"
        I4["text"] = "Pause aléatoire comprise entre 0.5 et 1 seconde"
        I4.place(x=largeur/2+50,y=hauteur/9+565,width=screenwidth/2-100,height=50)

        I5 = tk.Label(fenetre)
        I5["font"] = ft
        I5["fg"] = "#FFFFFF"
        I5["bg"] = "#2F5496"
        I5["text"] = "Fin si CTRL+C OU fin de la boucle"
        I5.place(x=largeur/2+30,y=hauteur/9+635,width=screenwidth/2-60,height=50)

        I6 = tk.Label(fenetre)
        I6["font"] = ft
        I6["fg"] = "#FFFFFF"
        I6["bg"] = "#2F5496"
        I6["text"] = "Arrêt des moteurs"
        I6.place(x=largeur/2+30,y=hauteur/9+705,width=screenwidth/2-60,height=50)

    #L'action youpi simplifié
    def youpiSimple(self, fenetre, largeur, hauteur):
        
        self.base(fenetre, largeur, hauteur, "./Images/Youpi.png")
        
        self.Processus2(fenetre, largeur, hauteur)
        #Déclaration de la police
        ft = tkFont.Font(family='Oxygen',size=20)

        I0 = tk.Label(fenetre)
        I0["font"] = ft
        I0["fg"] = "#FFFFFF"
        I0["bg"] = "#4C687A"
        I0["text"] ="Détection vocale ou appel depuis l'application mobile"
        I0.place(x=largeur/2+30,y=hauteur/9+30,width=largeur/2-60,height=50)

        I0G = tk.Label(fenetre)
        I0G["font"] = ft
        I0G["fg"] = "#FFFFFF"
        I0G["bg"] = "#2F5496"
        I0G["text"] = "Bras gauche"
        I0G.place(x=largeur/2+50,y=hauteur/9+170,width=200,height=50)

        I0D = tk.Label(fenetre)
        I0D["font"] = ft
        I0D["fg"] = "#FFFFFF"
        I0D["bg"] = "#2F5496"
        I0D["text"] = "Bras droit"
        I0D.place(x=largeur/2+520,y=hauteur/9+170,width=200,height=50)

        I1 = tk.Label(fenetre)
        I1["font"] = ft
        I1["fg"] = "#FFFFFF"
        I1["bg"] = "#2F5496"
        I1["text"] = "Démarrage des moteurs controllant les bras"
        I1.place(x=largeur/2+30,y=hauteur/9+240,width=largeur/2-60,height=50)

        I2G = tk.Label(fenetre)
        I2G["font"] = ft
        I2G["fg"] = "#FFFFFF"
        I2G["bg"] = "#2F5496"
        I2G["text"] = "Le bras\nse lève"
        I2G.place(x=largeur/2+50,y=hauteur/9+310,width=200,height=100)

        I2D = tk.Label(fenetre)
        I2D["font"] = ft
        I2D["fg"] = "#FFFFFF"
        I2D["bg"] = "#2F5496"
        I2D["text"] = "Le bras\nse lève"
        I2D.place(x=largeur/2+520,y=hauteur/9+310,width=200,height=100)

        ft = tkFont.Font(family='Oxygen',size=25)

        Multiplicateur = tk.Label(fenetre)
        Multiplicateur["font"] = ft
        Multiplicateur["fg"] = "#FFFFFF"
        Multiplicateur["bg"] = "#4C687A"
        Multiplicateur["text"] = "x4\n\n\n\n\nx4"
        Multiplicateur.place(x=largeur/2+(largeur/4)-50,y=hauteur/9+315,width=80,height=280)

        ft = tkFont.Font(family='Oxygen',size=20)

        I3 = tk.Label(fenetre)
        I3["font"] = ft
        I3["fg"] = "#FFFFFF"
        I3["bg"] = "#2F5496"
        I3["text"] = "Pause d'une seconde ou moins"
        I3.place(x=largeur/2+30,y=hauteur/9+430,width=largeur/2-60,height=50)

        I4G = tk.Label(fenetre)
        I4G["font"] = ft
        I4G["fg"] = "#FFFFFF"
        I4G["bg"] = "#2F5496"
        I4G["text"] = "Le bras\nse baisse"
        I4G.place(x=largeur/2+50,y=hauteur/9+500,width=200,height=100)

        I4D = tk.Label(fenetre)
        I4D["font"] = ft
        I4D["fg"] = "#FFFFFF"
        I4D["bg"] = "#2F5496"
        I4D["text"] = "Le bras\nse baisse"
        I4D.place(x=largeur/2+520,y=hauteur/9+500,width=200,height=100)

        I5 = tk.Label(fenetre)
        I5["font"] = ft
        I5["fg"] = "#FFFFFF"
        I5["bg"] = "#2F5496"
        I5["text"] = "Arrêt des moteurs controllant les bras"
        I5.place(x=largeur/2+30,y=hauteur/9+625,width=largeur/2-60,height=50)

    #Les humeurs simplifiés (regroupé toutes dans la même fonction car similaire)
    def humeurSimple(self, fenetre, largeur, hauteur, typeH):

        # 0 = Amour, 1 = Base, 2 = Masque, 3 = clin d'oeil, 4 = colère, 5 = fatigué, 6 = riz, 7 = surpris, 8 = triste 

        if typeH == 0:
            humeur = "Amour"
            cheminImgCode = "./Images/Amoureux.png"
            hautImg = 500 

        if typeH == 1:
            humeur = "Base"
            cheminImgCode = "./Images/Base.png"
            hautImg = 750 
        
        if typeH == 2:
            humeur = "Masque"
            cheminImgCode = "./Images/Masque.png"
            hautImg = 150 
        
        if typeH == 3:
            humeur = "Clin d'oeil"
            cheminImgCode = "./Images/ClinDOeil.png"
            hautImg = 400 
        
        if typeH == 4:
            humeur = "Colère"
            cheminImgCode = "./Images/Colère.png"
            hautImg = 400 
        
        if typeH == 5:
            humeur = "Fatigué"
            cheminImgCode = "./Images/Fatigué.png"
            hautImg = 400 
        
        if typeH == 6:
            humeur = "riz"
            cheminImgCode = "./Images/Rire.png"
            hautImg = 350 
        
        if typeH == 7:
            humeur = "surpris"
            cheminImgCode = "./Images/Surpris.png"
            hautImg = 400 
        
        if typeH == 8:
            humeur = "triste"
            cheminImgCode = "./Images/Triste.png"
            hautImg = 400 

        self.baseAlt(fenetre, largeur, hauteur,cheminImgCode, hautImg)

        ft = tkFont.Font(family='Oxygen',size=20)

        I0 = tk.Label(fenetre)
        I0["font"] = ft
        I0["fg"] = "#FFFFFF"
        I0["bg"] = "#4C687A"
        I0["anchor"] = "nw"
        I0["text"] = "Détection vocale ou appel depuis l'application mobile"
        I0.place(x=largeur/2+30,y=hauteur/9+170,width=largeur/2-60,height=50)

        I1 = tk.Label(fenetre)
        I1["font"] = ft
        I1["fg"] = "#FFFFFF"
        I1["bg"] = "#2F5496"
        I1["anchor"] = "nw"
        I1["text"] = "Si Humeur = "+humeur
        I1.place(x=largeur/2+30,y=hauteur/9+240,width=largeur/2-60,height=50)

        I2 = tk.Label(fenetre)
        I2["font"] = ft
        I2["fg"] = "#FFFFFF"
        I2["bg"] = "#6495ED"
        I2["text"] = "Choix d'un Gif aléatoire\nparmis ceux disponible"
        I2.place(x=largeur/2+80,y=hauteur/9+310,width=largeur/2-300,height=100)

        I3 = tk.Label(fenetre)
        I3["font"] = ft
        I3["fg"] = "#FFFFFF"
        I3["bg"] = "#6495ED"
        I3["text"] = "Affichage du Gif choisi"
        I3.place(x=largeur/2+80,y=hauteur/9+430,width=largeur/2-300,height=50)

        I4 = tk.Label(fenetre)
        I4["font"] = ft
        I4["fg"] = "#FFFFFF"
        I4["bg"] = "#2F5496"
        I4["anchor"] = "nw"
        I4["text"] = "Fin du si"
        I4.place(x=largeur/2+30,y=hauteur/9+500,width=largeur/2-60,height=50)

    #Page d'accueil
    def accueil(self, fenetre, largeur, hauteur):
        
        fichierimg = Image.open("Images/upjv.png")
        imageResize = fichierimg.resize((210,250), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imageResize)

        ImageUpjv = tk.Label(image=image)
        ImageUpjv.image = image
        ImageUpjv["bg"] = "#FFFFFF"
        ImageUpjv.place(x=50,y=50,width=300,height=300)

        fichierimg = Image.open("Images/logo.png")
        imageResize = fichierimg.resize((250,250), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imageResize)

        ImageLogo = tk.Label(image=image)
        ImageLogo.image = image
        ImageLogo["bg"] = "#FFFFFF"
        ImageLogo.place(x=largeur-360,y=50,width=300,height=300)

        TitreLabel=tk.Label(fenetre)
        ft = tkFont.Font(family='Oxygen',size=60)
        TitreLabel["font"] = ft
        TitreLabel["fg"] = "#2F5496"
        TitreLabel["bg"] = "#FFFFFF"
        TitreLabel["justify"] = "center"
        TitreLabel["text"] = "Learnobot"
        TitreLabel.place(x=largeur/2-210,y=hauteur/2-60,width=400,height=120)

        TitreLabel=tk.Label(fenetre)
        ft = tkFont.Font(family='Oxygen',size=20)
        TitreLabel["font"] = ft
        TitreLabel["fg"] = "#6495ED"
        TitreLabel["bg"] = "#FFFFFF"
        TitreLabel["justify"] = "center"
        TitreLabel["text"] = "Coulibaly Odiouma\nFelix Jonathan\nGuermane Fadwa\nJoyat Keryann"
        TitreLabel.place(x=largeur/2-160,y=hauteur/2+80,width=300,height=150)


#fenetre = tk.Tk()
#fenetre.title("LearnoBot") #Titre
#fenetre.attributes("-fullscreen",True) #Plein Ecran
#fenetre["bg"] = "#FFFFFF"
#fenetre.resizable(width=False, height=False)#redimensionnement de la fenetre interdit
#screenwidth = fenetre.winfo_screenwidth() #Largeur écran
#screenheight = fenetre.winfo_screenheight()#hauteur écran

#aff = Affichage()
#aff.accuei   l(fenetre, screenwidth, screenheight)
#aff.coucouSimple(fenetre, screenwidth, screenheight)
#aff.danseSimple(fenetre, screenwidth, screenheight)
#aff.tektonikSimple(fenetre, screenwidth, screenheight)
#aff.youpiSimple(fenetre, screenwidth, screenheight)
#aff.humeurSimple(fenetre, screenwidth, screenheight, 8)

#fenetre.mainloop()

