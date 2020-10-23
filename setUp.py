#Importar Librerias
import tkinter as tk
from tkinter import *

class OpenForms(): 

	def abrirFormulario():
		window = tk.Tk() #Inicia el Formulario
	window.title("Lector de MOV2000 - VALIDATOR")  #Pone el título
		window.geometry('900x700') #Dimension el tamaño
		#root = tk.Tk()
		window.mainloop()
		#txtArchivo.write("Se abrió el Formulario\n")
		
		#label = tk.Label(root, text="Hello World!") # Create a text label
		#label.pack(padx=20, pady=20) # Pack it into the windo
		return window


