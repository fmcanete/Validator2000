import tkinter as tk
from tkinter import *
import wx
import wx.grid as gridlib
import pandas as pd
########################################################################
class MyForm(wx.Frame):
	
	def __init__(self):
		#Se inicializa el Frame dónde va el título y el tamaño de la ventana
		wx.Frame.__init__(self, parent=None, title="Lector MOV2000 - VALIDATOR",size=(900,300))
		panel = wx.Panel(self)
		
		itera = 0
		#Se colocan los nombres de las columnas
		nombres =['Numtar','NumEst','NumAut','PlanCuot','NumCuot','Moneda','Importe','CodPais','ImporteOrig','BinTarjeta'
		,'NombreComercio','BancoEstab','NumtarMov2000','planGob','Token','NumToken','PosDataCode','VisaRelease'] 
		rango = len(nombres)   #Se toma la dimensión de la lista anterior
		LecturaCamposBasicos = pd.read_csv('CSV_MOV2000.CSV',sep=';', index_col=0)   #Se abre el CSV creado anteriormente
		CantidadTranasacciones = len(LecturaCamposBasicos) #Se obtiene la cantidad de transacciones
		
		myGrid = gridlib.Grid(panel)        #Se crea la grilla
		myGrid.CreateGrid(CantidadTranasacciones + 1, rango)  #Se crea la grilla con la cantidad de filas del num de trx y los campos

		def rellenaColumnaCondPositiva(grilla,im,jm,iteram,posicion,condicion,colores): #El metodo se rellena por la grilla/ i y j del for / el iterador / posicion a modificar /condicion del campo /color de WX

			if iteram != posicion:
				grilla.SetCellValue(im+1,iteram, str(jm[iteram]))
			else:
				if jm[iteram] == condicion:
					grilla.SetCellValue(im+1,iteram, str(jm[iteram]))
					grilla.SetCellBackgroundColour(im+1,iteram,colores)
				else:
					grilla.SetCellValue(im+1,iteram, str(jm[iteram]))

		
		#ACA ES UN FOR DONDE SE VAN RELLENANDO LA GRILLA CREADA ANTERIORMENTE

		for itera in range(rango):
			
			for i, j in LecturaCamposBasicos.iterrows():
					
					
					if i == 0:
						############ NOMBRES COLUMNAS ##################
						myGrid.SetCellValue(i,itera, str(nombres[itera])) #Se le agrega el valor (fila,columna,dato)
						myGrid.SetCellTextColour(i, itera, wx.WHITE)
						myGrid.SetCellBackgroundColour(i,itera,wx.BLACK)
						################################################
						
						rellenaColumnaCondPositiva(myGrid,i,j,itera,11,998,wx.YELLOW)   #Emisión no Prisma
						
						

					else:   

						rellenaColumnaCondPositiva(myGrid,i,j,itera,11,998,wx.YELLOW)   #Emisión no Prisma
						
							

	   
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(myGrid, 1, wx.EXPAND)
		panel.SetSizer(sizer)
		

# class MainFrame(wx.Frame):
# 	""""""
# 	#----------------------------------------------------------------------
# 	def __init__(self):
# 		"""Constructor"""
# 		Lectura = 0
# 		wx.Frame.__init__(self, None, title="LectorMOV2000 - VALIDATOR",size=(800,600))
# 		#self.boton = wx.Button(self, -1, u"Botón")
# 		#Prueba = MyForm().Show()
# 		self.Show()

# if __name__ == "__main__":
# 	app = wx.App()
# 	display = MyForm().Show()
# 	#frame = MainFrame()
# 	app.MainLoop()