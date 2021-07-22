#-----VALIDATOR-------#
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import os
import Grilla
import wx
import wx.grid as gridlib
from timeit import timeit
import time as time
# IMPORTAR LOS ARCHIVOS
import tkinter as tk
import archivos
from tkinter import *
from tkinter.ttk import *
import time



class OpenForms(): 

	def abrirFormulario():
		window = tk.Tk() #Inicia el Formulario
		window.title("Lector MOV2000 - VALIDATOR")  #Pone el título
		window.geometry('400x150') #Dimension el tamaño
		mensaje = Label(window,text="HACER CLICK EN EL BOTÓN PARA VER MOV2000")
		mensaje.pack()
		
		#METODO QUE OBTIENE LA RUTA DONDE ESTA EL ARCHIVO MOV2000
		def abrir_archivo():
			archivo_abierto=filedialog.askopenfilename(initialdir = "/",
                title = "Seleccione archivo",filetypes = (("txt files","*.txt"),
                ("all files","*.*")))
			return(archivo_abierto)

		#BOTÓN LEER QUE LLAMA AL MÉTODO CLICKED
		def clicked():
			window.destroy()
			import ventanaProgress			
			

			
			mov2000Plano = "a"
			listaArchivo = []
			contadorArchivo = 0
			CSV_MOV2000 = "a"
			listaCompleta = []
			ruta= ""

			ruta = abrir_archivo() #SE LLAMA EL MÉTODO DONDE SE CONSIGUE LA RUTA

			#window.destroy()


			

			mov2000Plano = archivos.manejoDeLosArchivosTXT.abrirArchivo(mov2000Plano,ruta)

			listaArchivo, contadorArchivo = archivos.manejoDeLosArchivosTXT.recorrerArchivoMov2000(mov2000Plano, listaArchivo, contadorArchivo)

			listaCompleta = archivos.manejoDeLosArchivosTXT.subStringLista(listaArchivo, contadorArchivo, listaCompleta)

			archivos.manejoDeLosArchivosTXT.cerrarArchivo(mov2000Plano)


			app = wx.App()
			
			
			ventanaProgress.start1()
			display = Grilla.MyForm().Show()
			ventanaProgress.ventana.destroy()

	
			app.MainLoop()

			
		btn = Button(window, text="Leer", command=clicked)
		btn.pack(expand= "True",fill="x")


		
			
		window.mainloop()
		
		return window