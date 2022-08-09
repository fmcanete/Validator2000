# #Importar las librerias
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pandas as pd
# IMPORTAR LOS ARCHIVOS
import vicap 
from vicap import archivos, Grilla, archivoMkpriv, GrillaMkpriv,setUp_VISA,archivoMOVRECHAZOS,GrillaMOVRECHAZOS
from mcap import archivos, Grilla,setUp_MASTER, logicaBD, graficas
from Multicap import setUp_MULTICAP 

########################### Imagen Fantastica ################################################
window = Tk()  
window.overrideredirect(True)
window.wm_attributes("-topmost", True)
window.geometry("+600+250")
canvas = Canvas(window, width = 200, height = 200)   
canvas.configure(bg='black')        
img = PhotoImage(file="validator2.png") 
img = img.subsample(2)
canvas.create_image(1,1, anchor=NW, image=img)
canvas.pack()     
canvas.config(width="350", height="100") 
window.after(3000, window.destroy)
window.mainloop()
###############################################################################################

def Inicializar(parametro):
    parametro.OpenForms.abrirFormulario()

def formularioGeneral():
    VentanaSELECCION = tk.Tk() #Inicia el Formulario
    VentanaSELECCION.title("VALIDATOR")  #Pone el título
    VentanaSELECCION.geometry('600x100') #Dimension el tamaño
    VentanaSELECCION.geometry("+450+250")
    #VentanaSELECCION.geometry('300x185') #Dimension el tamaño para botones juntos
    #VentanaSELECCION.eval('tk::PlaceWindow . center')
    VentanaSELECCION.iconbitmap('validator_icono.ico')
    VentanaSELECCION.configure(bg='grey77')
    mensaje = Label(VentanaSELECCION,text="SELECCIONE ADQUIRENCIA")
    mensaje.configure(bg='grey77',fg="black",font='arial 12 bold')
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
        VentanaSELECCION.destroy()
        Inicializar(setUp_MULTICAP)
        formularioGeneral()

#####################LOGO DE ADQUIRENCIAS###################################################
   
    visaimg = Image.open('img\\Visa.png')
    visaimg = visaimg.resize((100, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    visaimg = ImageTk.PhotoImage(visaimg)

    masterimg = Image.open('img\\MasterCard.png')
    masterimg = masterimg.resize((100, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    masterimg = ImageTk.PhotoImage(masterimg)

    multiimg = Image.open('img\\Multi.png')
    multiimg = multiimg.resize((100, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    multiimg = ImageTk.PhotoImage(multiimg)

############################################################################################


######################################BOTONES########################################################
#royalblue4
    BOTON_VICAP = Button(VentanaSELECCION,image=visaimg, bg = "royalblue4",command=clickedVicap)
    BOTON_VICAP.place(x=100, y=30)
    #BOTON_VICAP.pack(expand= "True",fill="x")

    BOTON_MCAP = Button(VentanaSELECCION,image=masterimg,bg = "royalblue4",command=clickedMcap)
    BOTON_MCAP.place(x=250, y=30)

    BOTON_MULTI = Button(VentanaSELECCION,image=multiimg,bg = "royalblue4",command=clickedMulti)
    BOTON_MULTI.place(x=400, y=30)

######################################################################################################


    VentanaSELECCION.mainloop()


formularioGeneral()
