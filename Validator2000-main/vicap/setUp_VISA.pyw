 # #Importar las librerias
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from tkinter.ttk import *
from tkinter import *
import time as time
import os
#import Grilla
import wx
import wx.grid as gridlib
from timeit import timeit
#import archivos
from vicap import *
from vicap import archivos, Grilla, archivoMkpriv, GrillaMkpriv, archivoM240, GrillaM240

class OpenForms(): 

	def abrirFormulario():
		window = tk.Tk() #Inicia el Formulario
		window.title("VICAP - VALIDATOR")  #Pone el título
		window.geometry('400x150') #Dimension el tamaño
		window.eval('tk::PlaceWindow . center')
		window.iconbitmap('validator_icono.ico')
		mensaje = Label(window,text="SELECCIONE OPCION PARA VICAP")
		mensaje.pack()
		
		#METODO QUE OBTIENE LA RUTA DONDE ESTA EL ARCHIVO MOV2000
		def abrir_archivo():
			archivo_abierto=filedialog.askopenfilename(initialdir = "/", #esto abre en el raiz. ver de mejorar y poner donde esta el proyecto
                title = "Seleccione archivo",filetypes = (("txt files","*.txt"),
                ("all files","*.*")))
			return(archivo_abierto)

		
		def clickedTotal(): #casos totales
						
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
								os.rename('CSV_MOV2000.CSV', 'vicap\\EvidenciasMOV2000\\VISA_TOTAL_MOV2000_'+timestamp+'.CSV')
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
				print("Vuelvo a iterar")	#esto es cuando se abre y se cierra la ventana con cancelar				

		def clickedParticular(): #casos particulares
	
					
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
						os.rename('CSV_MOV2000.CSV', 'vicap\\EvidenciasMOV2000\\VISA_CASOS_MOV2000_'+timestamp+'.CSV')
						OpenForms.abrirFormulario()

					else:
						messagebox.showinfo(message="¡Error en formato de Archivo! AAA", title="Error")
						
						print("Formato de Archivo erroneo, vuelvo a iterar")
				else:
					print("Formato de Archivo erroneo, vuelvo a iterar")
					messagebox.showinfo(message="¡Error en formato de Archivo! BBB", title="Error")

			else:
				print("Vuelvo a iterar")

		def clickedMkpriv(): #casos marcas privadas
						
			mkprivPlano = "a"
			listaArchivo = []
			contadorArchivo = 0
			CSV_MKPRIV = "a"
			listaCompleta = []
			ruta= ""

			ruta = abrir_archivo() #SE LLAMA EL MÉTODO DONDE SE CONSIGUE LA RUTA

			if ruta != '':  #Si la ruta no está vacía proceso.
	
				mkprivPlano = archivoMkpriv.manejoDeLosArchivosTXT.abrirArchivo(mkprivPlano,ruta)
				listaArchivo, contadorArchivo = archivoMkpriv.manejoDeLosArchivosTXT.recorrerArchivoMkpriv(mkprivPlano, listaArchivo, contadorArchivo)

				if listaArchivo !=11: #Si el método listaArchivo no dió excepción de memoria entro

					if listaArchivo != 10: #Si el método listaArchivo no dió otra excepcion entro
						listaCompleta = archivoMkpriv.manejoDeLosArchivosTXT.subStringLista(listaArchivo, contadorArchivo, listaCompleta)
						archivoMkpriv.manejoDeLosArchivosTXT.cerrarArchivo(mkprivPlano)

						if listaCompleta != 10: #Si el método listaCompleta no dió excepcion entro
							
							if len(listaArchivo) < 100000: #Si el MOV2000 es muy grande no carga la grilla
								window.destroy()
								import ventanaProgress	
								app = wx.App()
								print("Tamaño Lista: ", len(listaArchivo))
								ventana = ventanaProgress.start1()
								display = GrillaMkpriv.MyForm().Show()
								ventana.destroy()						
								app.MainLoop()
								timestamp = time.strftime('%Y%m%d%H%M%S')
								os.rename('CSV_MKPRIV.CSV', 'vicap\\EvidenciasMKPRIV\\TOTALMKPRIV_'+timestamp+'.CSV')
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
				print("Vuelvo a iterar")	#esto es cuando se abre y se cierra la ventana con cancelar				
			
		###################################################
		def clickedM240(): #casos marcas privadas
			m240Plano = "a"
			listaArchivo = []
			contadorArchivo = 0
			CSV_M240 = "a"
			listaCompleta = []
			ruta= ""

			ruta = abrir_archivo() #SE LLAMA EL MÉTODO DONDE SE CONSIGUE LA RUTA

			if ruta != '':  #Si la ruta no está vacía proceso.
	
				m240Plano = archivoM240.manejoDeLosArchivosTXT.abrirArchivo(m240Plano,ruta)
				listaArchivo, contadorArchivo = archivoM240.manejoDeLosArchivosTXT.recorrerArchivoM240(m240Plano, listaArchivo, contadorArchivo)

				if listaArchivo !=11: #Si el método listaArchivo no dió excepción de memoria entro

					if listaArchivo != 10: #Si el método listaArchivo no dió otra excepcion entro
						listaCompleta = archivoM240.manejoDeLosArchivosTXT.subStringLista(listaArchivo, contadorArchivo, listaCompleta)
						archivoM240.manejoDeLosArchivosTXT.cerrarArchivo(m240Plano)

						if listaCompleta != 10: #Si el método listaCompleta no dió excepcion entro
							
							if len(listaArchivo) < 100000: #Si el MOV2000 es muy grande no carga la grilla
								window.destroy()
								import ventanaProgress	
								app = wx.App()
								print("Tamaño Lista: ", len(listaArchivo))
								ventana = ventanaProgress.start1()
								display = GrillaM240.MyForm().Show()
								ventana.destroy()						
								app.MainLoop()
								timestamp = time.strftime('%Y%m%d%H%M%S')
								os.rename('CSV_M240.CSV', 'vicap\\EvidenciasM240\\TOTALM240_'+timestamp+'.CSV')
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
				print("Vuelvo a iterar")	#esto es cuando se abre y se cierra la ventana con cancelar	
		###################################################
		
		
		
		
		
		btn = Button(window, text="Casos Particulares - MOV2000", command=clickedParticular)
		btn.pack(expand= "True",fill="x")
		btn2 = Button(window, text="Lectura Total  - MOV2000", command=clickedTotal)
		btn2.pack(expand= "True",fill="x")		
		btn3 = Button(window, text="Marcas Privadas", command=clickedMkpriv)
		btn3.pack(expand= "True",fill="x")
		####
		btn4 = Button(window, text="M240", command=clickedM240)
		btn4.pack(expand= "True",fill="x")


	
		window.mainloop()
		
		return window