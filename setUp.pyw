#-----VALIDATOR-------#
import tkinter as tk
from tkinter import *
import os
import Grilla
import wx
import wx.grid as gridlib

class OpenForms(): 

	def abrirFormulario():
		window = tk.Tk() #Inicia el Formulario
		window.title("Lector MOV2000 - VALIDATOR")  #Pone el título
		window.geometry('400x50') #Dimension el tamaño
		mensaje = Label(window,text="HACER CLICK EN EL BOTÓN PARA VER MOV2000")
		mensaje.pack()
		#BOTÓN LEER QUE LLAMA AL MÉTODO CLICKED
		def clicked():
			window.destroy()
			
			app = wx.App()
			display = Grilla.MyForm().Show()
			#frame = MainFrame()
			app.MainLoop()
			
		btn = Button(window, text="Leer", command=clicked)
		btn.pack(expand= "True",fill="x")

		
			
		window.mainloop()
		
		return window