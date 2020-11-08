#-----VALIDATOR-------#
import tkinter as tk
from tkinter import *


class OpenForms(): 

	def abrirFormulario():
		window = tk.Tk() #Inicia el Formulario
		window.title("Lector de MOV2000 - VALIDATOR")  #Pone el título
		window.geometry('900x700') #Dimension el tamaño
		window.mainloop()
		return window