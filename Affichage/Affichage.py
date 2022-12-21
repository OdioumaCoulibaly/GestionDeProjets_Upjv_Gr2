import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


class Affichage:
    #def __init__(self,fenetre):
        

    def Exemple(self, fenetre):

        screenwidth = fenetre.winfo_screenwidth() #Largeur écran
        screenheight = fenetre.winfo_screenheight()#hauteur écran

        Fondheader = tk.Label(fenetre)
        Fondheader["bg"] = "#022D59"
        Fondheader.place(x=0,y=0,width=screenwidth,height=screenheight/9)

        TitreLabelPython=tk.Label(fenetre)
        ft = tkFont.Font(family='Times',size=36)
        TitreLabelPython["font"] = ft
        TitreLabelPython["fg"] = "#FFFFFF"
        TitreLabelPython["bg"] = "#2F5496"
        TitreLabelPython["justify"] = "center"
        TitreLabelPython["text"] = "Code Python"
        TitreLabelPython["borderwidth"] = 10
        TitreLabelPython.place(x=5,y=5,width=screenwidth/2-10,height=screenheight/9-10)

        TitreLabelCodeSimple=tk.Label(fenetre)
        TitreLabelCodeSimple["font"] = ft
        TitreLabelCodeSimple["fg"] = "#FFFFFF"
        TitreLabelCodeSimple["bg"] = "#2F5496"
        TitreLabelCodeSimple["justify"] = "center"
        TitreLabelCodeSimple["text"] = "Code Simplifié"
        TitreLabelCodeSimple.place(x=screenwidth/2+5,y=5,width=screenwidth/2-10,height=screenheight/9-10)

        fichierimg = Image.open("Images/testCapture.png")
        imageResize = fichierimg.resize(((screenwidth//2),(screenheight-screenheight//9)), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imageResize)

        ImageCode = tk.Label(image=image)
        ImageCode.image = image

        ft = tkFont.Font(family='Times',size=10)
        ImageCode["font"] = ft
        ImageCode["fg"] = "#333333"
        ImageCode["bg"] = "#9FA6AD"
        ImageCode["anchor"] = "nw"
        ImageCode["text"] = "label"
        ImageCode.place(x=0,y=screenheight/9-1,width=screenwidth/2,height=(screenheight-(screenheight/9)))

        
        SeparationV=tk.Label(fenetre)
        SeparationV["bg"] = "#022D59"
        SeparationV.place(x=(screenwidth/2),y=0,width=5,height=screenheight)

        SeparationL=tk.Label(fenetre)
        SeparationL["bg"] = "#022D59"
        SeparationL.place(x=0,y=(screenheight/9)-1,width=screenwidth,height=2)

        #faire une indentation à la scratch
        #faire une indentation à la scratch
        #faire une indentation à la scratch
        #faire une indentation à la scratch
        #faire une indentation à la scratch
        #faire une indentation à la scratch
    
fenetre = tk.Tk()
fenetre.title("LearnoBot") #Titre
fenetre.attributes("-fullscreen",True) #Plein Ecran
fenetre["bg"] = "#FFFFFF"
fenetre.resizable(width=False, height=False)#redimensionnement de la fenetre interdit
aff = Affichage()
aff.Exemple(fenetre)
fenetre.mainloop()
