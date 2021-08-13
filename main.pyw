 
# #Importar las librerias
import tkinter as tk
from tkinter import *
import pandas as pd

# IMPORTAR LOS ARCHIVOS
import setUp,archivos

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

Inicializar(setUp)

