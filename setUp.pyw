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
			mov2000Plano = "a"
			listaArchivo = []
			contadorArchivo = 0
			CSV_MOV2000 = "a"
			listaCompleta = []
			ruta= ""

#			loading = tk.Tk() #Inicia el Formulario
#			loading.title("Aguarde y será atendido por Jose")  #Pone el título
#			loading.geometry('100x50') #Dimension el tamaño
			window.progressbar = ttk.Progressbar(window, mode="indeterminate")
			window.progressbar.pack()
			window.progressbar.start()

			ruta = abrir_archivo() #SE LLAMA EL MÉTODO DONDE SE CONSIGUE LA RUTA
			#window.destroy()


			

			mov2000Plano = archivos.manejoDeLosArchivosTXT.abrirArchivo(mov2000Plano,ruta)
			print("1")
			print(time.strftime("%H:%M:%S"))

			listaArchivo, contadorArchivo = archivos.manejoDeLosArchivosTXT.recorrerArchivoMov2000(mov2000Plano, listaArchivo, contadorArchivo)
			print("2")			
			print(time.strftime("%H:%M:%S"))
			listaCompleta = archivos.manejoDeLosArchivosTXT.subStringLista(listaArchivo, contadorArchivo, listaCompleta)
			print("3")			
			print(time.strftime("%H:%M:%S"))
			archivos.manejoDeLosArchivosTXT.cerrarArchivo(mov2000Plano)
			print("4")			
			print(time.strftime("%H:%M:%S"))
			window.progressbar.destroy()
			app = wx.App()
			display = Grilla.MyForm().Show()


			
			#frame = MainFrame()
			app.MainLoop()
			
		btn = Button(window, text="Leer", command=clicked)
		btn.pack(expand= "True",fill="x")


		
			
		window.mainloop()
		
		return window