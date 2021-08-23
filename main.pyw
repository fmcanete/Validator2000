 # #Importar las librerias
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pandas as pd
# IMPORTAR LOS ARCHIVOS
import vicap 
from vicap import archivos, Grilla, archivoMkpriv, GrillaMkpriv,setUp_VISA
from mcap import archivos, Grilla,setUp_MASTER


########################### Imagen Fantastica ###########################
window = Tk()  
window.overrideredirect(True)
window.wm_attributes("-topmost", True)
window.geometry("+450+150")
canvas = Canvas(window, width = 800, height = 800)   
canvas.configure(bg='black')        
img = PhotoImage(file="validator2.png") 
img = img.subsample(2)
canvas.create_image(1,1, anchor=NW, image=img)
canvas.pack()     
canvas.config(width="400", height="400") 
window.after(3000, window.destroy)
window.mainloop()
##########################################################################


def Inicializar(parametro):
    parametro.OpenForms.abrirFormulario()


def formularioGeneral():
    VentanaSELECCION = tk.Tk() #Inicia el Formulario
    VentanaSELECCION.title("VALIDATOR")  #Pone el título
    VentanaSELECCION.geometry('380x185') #Dimension el tamaño
    VentanaSELECCION.eval('tk::PlaceWindow . center')
    VentanaSELECCION.iconbitmap('validator_icono.ico')
    mensaje = Label(VentanaSELECCION,text="SELECCIONE ADQUIRENCIA")
    mensaje.pack()

    def clickedVicap():
        VentanaSELECCION.destroy()
        Inicializar(setUp_VISA)
        formularioGeneral()
    
    def clickedMcap():
        VentanaSELECCION.destroy()
        Inicializar(setUp_MASTER)
        formularioGeneral()

    def clickedMulti():
        #VentanaSELECCION.destroy()
        #Inicializar(setUp_MASTER)
        messagebox.showinfo(message="¡En construcción!", title="Error")
        #formularioGeneral()

#####################LOGO DE ADQUIRENCIAS###################################################
   
    visaimg = Image.open('img\\Visa.jpg')
    visaimg = visaimg.resize((100, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    visaimg = ImageTk.PhotoImage(visaimg)

    masterimg = Image.open('img\\MasterCard.png')
    masterimg = masterimg.resize((100, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    masterimg = ImageTk.PhotoImage(masterimg)

    multiimg = Image.open('img\\Multi.png')
    multiimg = multiimg.resize((130, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    multiimg = ImageTk.PhotoImage(multiimg)

############################################################################################

    BOTON_VICAP = Button(VentanaSELECCION,image=visaimg, bg = "grey",command=clickedVicap)
    BOTON_VICAP.pack(expand= "True",fill="x")

    BOTON_MCAP = Button(VentanaSELECCION,image=masterimg,bg = "grey",command=clickedMcap)
    BOTON_MCAP.pack(expand= "True",fill="x")

    BOTON_MULTI = Button(VentanaSELECCION,image=multiimg,bg = "grey",command=clickedMulti)
    BOTON_MULTI.pack(expand= "True",fill="x")

    VentanaSELECCION.mainloop()


formularioGeneral()
