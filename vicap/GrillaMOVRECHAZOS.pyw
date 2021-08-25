import tkinter as tk
from tkinter import *
import wx
import wx.grid as gridlib
import pandas as pd
from vicap import *
#####################################################################
class MyForm(wx.Frame):
	
	def __init__(self):
		#Se inicializa el Frame dónde va el título y el tamaño de la ventana
		wx.Frame.__init__(self, parent=None, title="Lector MOVRECHAZOS - VALIDATOR",size=(900,300), style = wx.DEFAULT_FRAME_STYLE)
		panel = wx.Panel(self)
		self.SetIcon(wx.Icon("validator_icono.ico"))

		itera = 0
		#Se colocan los nombres de las columnas
		nombres =['NUMEST','TERMINAL'] 
		rango = len(nombres)   #Se toma la dimensión de la lista anterior
		LecturaCamposBasicos = pd.read_csv('CSV_MOVRECHAZOS.CSV',sep=';', index_col=0)   #Se abre el CSV creado anteriormente
		CantidadTranasacciones = len(LecturaCamposBasicos) #Se obtiene la cantidad de transacciones
		
		myGrid = gridlib.Grid(panel)        #Se crea la grilla
		myGrid.CreateGrid(CantidadTranasacciones + 1, rango)  #Se crea la grilla con la cantidad de filas del num de trx y los campos

		def rellenaColumnaCondPositiva(grilla,im,jm,iteram,posicion,condicion,colores): #El metodo se rellena por la grilla/ i y j del for / el iterador / posicion a modificar /condicion del campo /color de WX

			if iteram != posicion:
				grilla.SetCellValue(im+1,iteram, str(jm[iteram])) #Va llenando la grilla hasta que encuentra 1 trx a VALIDAR (ENP)
			else:
				if str(jm[iteram]) == str(condicion): #CUANDO LA ENCUENTRA
					grilla.SetCellValue(im+1,iteram, str(jm[iteram])) #LLENA ACA ENP
					grilla.SetCellBackgroundColour(im+1,iteram,colores) #PONE COLOR ENP
				else:
					grilla.SetCellValue(im+1,iteram, str(jm[iteram])) #SI ES DISTINTO A ENP (007, 999)

		
		#ACA ES UN FOR DONDE SE VAN RELLENANDO LA GRILLA CREADA ANTERIORMENTE
		
		for itera in range(rango):
			
			for i, j in LecturaCamposBasicos.iterrows():
					
					
					if i == 0:
						############ NOMBRES COLUMNAS ##################
						myGrid.SetCellValue(i,itera, str(nombres[itera])) #Se le agrega el valor (fila,columna,dato)
						myGrid.SetCellTextColour(i, itera, wx.WHITE)
						myGrid.SetCellBackgroundColour(i,itera,wx.BLACK)
						################################################
						
						
						rellenaColumnaCondPositiva(myGrid,i,j,itera,6,'STD',wx.Colour( 187, 100, 251 ))   #MARCA CUOTA A CUOTA						
						

					else:   

						rellenaColumnaCondPositiva(myGrid,i,j,itera,6,'STD',wx.Colour( 187, 100, 251 ))   #MARCA CUOTA A CUOTA		

	   
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(myGrid, 1, wx.EXPAND)
		panel.SetSizer(sizer)
		

