#-----VALIDATOR-------#
import tkinter as tk
from tkinter import *
import os
import Grilla
import wx
import wx.grid as gridlib
# IMPORTAR LOS ARCHIVOS
import archivos



class OpenForms(): 

	def abrirFormulario():
		window = tk.Tk() #Inicia el Formulario
		window.title("Lector MOV2000 - VALIDATOR")  #Pone el título
		window.geometry('400x50') #Dimension el tamaño
		mensaje = Label(window,text="HACER CLICK EN EL BOTÓN PARA VER MOV2000")
		mensaje.pack()
		#BOTÓN LEER QUE LLAMA AL MÉTODO CLICKED
		def clicked():
			mov2000Plano = "a"
			listaArchivo = []
			contadorArchivo = 0
			CSV_MOV2000 = "a"
			listaCompleta = []
			#window.destroy()
			mov2000Plano = archivos.manejoDeLosArchivosTXT.abrirArchivo(mov2000Plano)

			listaArchivo, contadorArchivo = archivos.manejoDeLosArchivosTXT.recorrerArchivoMov2000(mov2000Plano, listaArchivo, contadorArchivo)

			listaCompleta = archivos.manejoDeLosArchivosTXT.subStringLista(listaArchivo, contadorArchivo, listaCompleta)

			archivos.manejoDeLosArchivosTXT.cerrarArchivo(mov2000Plano)
			app = wx.App()
			display = Grilla.MyForm().Show()
			#frame = MainFrame()
			app.MainLoop()
			
		btn = Button(window, text="Leer", command=clicked)
		btn.pack(expand= "True",fill="x")

		
			
		window.mainloop()
		
		return window