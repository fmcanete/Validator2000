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
from tkinter import messagebox

class OpenForms(): 

	def abrirFormulario():
		window = tk.Tk() #Inicia el Formulario
		window.title("Lector MOV2000 - VALIDATOR")  #Pone el título
		window.geometry('400x150') #Dimension el tamaño
		window.eval('tk::PlaceWindow . center')
		window.iconbitmap('validator.ico')
		mensaje = Label(window,text="SELECCIONE OPCION PARA MOV2000")
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

			ruta = abrir_archivo() #SE LLAMA EL MÉTODO DONDE SE CONSIGUE LA RUTA


			if ruta != '':  #Si la ruta no está vacía proceso.
	
				mov2000Plano = archivos.manejoDeLosArchivosTXT.abrirArchivo(mov2000Plano,ruta)
				listaArchivo, contadorArchivo = archivos.manejoDeLosArchivosTXT.recorrerArchivoMov2000(mov2000Plano, listaArchivo, contadorArchivo)

				if listaArchivo !=11: #Si el método listaArchivo no dió excepción de memoria entro

					if listaArchivo != 10: #Si el método listaArchivo no dió otra excepcion entro
						listaCompleta = archivos.manejoDeLosArchivosTXT.subStringLista(listaArchivo, contadorArchivo, listaCompleta)
						archivos.manejoDeLosArchivosTXT.cerrarArchivo(mov2000Plano)

						if listaCompleta != 10: #Si el método listaCompleta no dió excepcion entro
							
							if len(listaArchivo) < 100000: #Si el MOV2000 es muy grande no carga la grilla
								window.destroy()
								import ventanaProgress	
								app = wx.App()
								print("Tamaño Lista: ", len(listaArchivo))
								ventana = ventanaProgress.start1()
								display = Grilla.MyForm().Show()
								ventana.destroy()						
								app.MainLoop()
								timestamp = time.strftime('%Y%m%d%H%M%S')
								os.rename('CSV_MOV2000.CSV', 'TOTAL_MOV2000_'+timestamp+'.CSV')
								OpenForms.abrirFormulario()
							else:
								messagebox.showinfo(message="¡Archivo muy grande para mostrar en grilla!", title="Error")
								print("Formato de muy grande vuelvo a iterar")


						else:
							messagebox.showinfo(message="¡Error en formato de Archivo!", title="Error")
							print("Formato de Archivo erroneo, vuelvo a iterar")
					else:
						print("Formato de Archivo erroneo, vuelvo a iterar")
						messagebox.showinfo(message="¡Error en formato de Archivo!", title="Error")

				else:
					print("Formato de Archivo erroneo, vuelvo a iterar")
					messagebox.showinfo(message="¡Error en memoria, archivo muy grande!", title="Error")
			else:
				print("Vuelvo a iterar")
		
		

		def clicked2():
	
					
			mov2000Plano = "a"
			listaArchivo = []
			contadorArchivo = 0
			CSV_MOV2000 = "a"
			listaCompleta = []
			ruta= ""

			ruta = abrir_archivo() #SE LLAMA EL MÉTODO DONDE SE CONSIGUE LA RUTA


			if ruta != '':  #Si la ruta no está vacía proceso.
	
				mov2000Plano = archivos.manejoDeLosArchivosTXT.abrirArchivo(mov2000Plano,ruta)
				listaArchivo, contadorArchivo = archivos.manejoDeLosArchivosTXT.recorrerArchivoMov2000(mov2000Plano, listaArchivo, contadorArchivo)
				
				if listaArchivo != 10: #Si el método listaArchivo no dió excepcion entro
					listaCompleta = archivos.manejoDeLosArchivosTXT.subStringListaCasos(listaArchivo, contadorArchivo, listaCompleta)
					archivos.manejoDeLosArchivosTXT.cerrarArchivo(mov2000Plano)
					

					
					if listaCompleta != 10: #Si el método listaCompleta no dió excepcion entro
						window.destroy()
						import ventanaProgress	
						app = wx.App()
						ventana = ventanaProgress.start1()
						display = Grilla.MyForm().Show()
						ventana.destroy()
						app.MainLoop()
						timestamp = time.strftime('%Y%H%M%S')
						os.rename('CSV_MOV2000.CSV', 'CASOS_MOV2000_'+timestamp+'.CSV')
						OpenForms.abrirFormulario()

					else:
						messagebox.showinfo(message="¡Error en formato de Archivo!", title="Error")
						
						print("Formato de Archivo erroneo, vuelvo a iterar")
				else:
					print("Formato de Archivo erroneo, vuelvo a iterar")
					messagebox.showinfo(message="¡Error en formato de Archivo!", title="Error")

			else:
				print("Vuelvo a iterar")


			
		btn = Button(window, text="Casos Particulares", command=clicked2)
		btn.pack(expand= "True",fill="x")
		btn2 = Button(window, text="Lectura Total", command=clicked)
		btn2.pack(expand= "True",fill="x")

	
		window.mainloop()
		
		return window