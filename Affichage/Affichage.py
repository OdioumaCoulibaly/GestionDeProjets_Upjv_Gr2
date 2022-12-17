import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


class Affichage:
    def __init__(self, fenetre):
        #setting title

        fenetre.title("LearnoBot")
        fenetre.attributes("-fullscreen",True)
        screenwidth = fenetre.winfo_screenwidth()
        screenheight = fenetre.winfo_screenheight()
        fenetre.resizable(width=False, height=False)

       

        TitreLabelPython=tk.Label(fenetre)
        ft = tkFont.Font(family='Times',size=20)
        TitreLabelPython["font"] = ft
        TitreLabelPython["fg"] = "#FFFFFF"
        TitreLabelPython["bg"] = "#2F5496"
        TitreLabelPython["justify"] = "center"
        TitreLabelPython["text"] = "Code Python"
        TitreLabelPython.place(x=0,y=0,width=screenwidth/2,height=screenheight/9)

        TitreLabelCodeSimple=tk.Label(fenetre)
        ft = tkFont.Font(family='Times',size=20)
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
        ImageCode["bg"] = "#3E3E40"
        ImageCode["justify"] = "center"
        ImageCode["text"] = "label"
        ImageCode.place(x=0,y=screenheight/9,width=screenwidth/2,height=(screenheight-(screenheight/9)))

if __name__ == "__main__":
    fenetre = tk.Tk()
    app = Affichage(fenetre)
    fenetre.mainloop()
