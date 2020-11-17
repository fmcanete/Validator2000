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
		,'NombreComercio','BancoEstab','NumtarMov2000','Token','NumToken','PosDataCode','VisaRelease'] 
		rango = len(nombres)   #Se toma la dimensión de la lista anterior
		LecturaCamposBasicos = pd.read_csv('CSV_MOV2000.CSV',sep=';', index_col=0)   #Se abre el CSV creado anteriormente
		CantidadTranasacciones = len(LecturaCamposBasicos) #Se obtiene la cantidad de transacciones
		
		myGrid = gridlib.Grid(panel)        #Se crea la grilla
		myGrid.CreateGrid(CantidadTranasacciones + 1, rango)  #Se crea la grilla con la cantidad de filas del num de trx y los campos

		
		#ACA ES UN FOR DONDE SE VAN RELLENANDO LA GRILLA CREADA ANTERIORMENTE

		for itera in range(rango):
			
			for i, j in LecturaCamposBasicos.iterrows():
					
					
					if i == 0:
						############ NOMBRES COLUMNAS ##################
						myGrid.SetCellValue(i,itera, str(nombres[itera])) #Se le agrega el valor (fila,columna,dato)
						myGrid.SetCellTextColour(i, itera, wx.WHITE)
						myGrid.SetCellBackgroundColour(i,itera,wx.BLACK)
						################################################
						
						if itera != 16 and itera != 11 and itera != 13: #Validación VISA RELEASE/EMISION NO PRISMA/TOKEN
							myGrid.SetCellValue(i+1,itera, str(j[itera]))
						elif itera == 16 :
							if j[itera] != ' '	: 
								myGrid.SetCellValue(i+1,itera, str(j[itera]))
								myGrid.SetCellBackgroundColour(i+1,itera,wx.GREEN)
							else:
								myGrid.SetCellValue(i+1,itera, str(j[itera]))
						elif itera == 11 :
							if j[itera] == 998: 
								myGrid.SetCellValue(i+1,itera, str(j[itera]))
								myGrid.SetCellBackgroundColour(i+1,itera,wx.YELLOW)
							else:
								myGrid.SetCellValue(i+1,itera, str(j[itera]))
						elif itera == 13 :
							if j[itera] == 'S': 
								myGrid.SetCellValue(i+1,itera, str(j[itera]))
								myGrid.SetCellBackgroundColour(i+1,itera,wx.BLUE)
								myGrid.SetCellTextColour(i+1, itera, wx.WHITE)
							else:
								myGrid.SetCellValue(i+1,itera, str(j[itera]))
						
						

					else:   
						if itera != 16 and itera != 11 and itera != 13: #Validación VISA RELEASE/EMISION NO PRISMA/TOKEN
							myGrid.SetCellValue(i+1,itera, str(j[itera]))
						elif itera == 16 :
							if j[itera] != ' '	: 
								myGrid.SetCellValue(i+1,itera, str(j[itera]))
								myGrid.SetCellBackgroundColour(i+1,itera,wx.GREEN)
							else:
								myGrid.SetCellValue(i+1,itera, str(j[itera]))
						elif itera == 11 :
							if j[itera] == 998: 
								myGrid.SetCellValue(i+1,itera, str(j[itera]))
								myGrid.SetCellBackgroundColour(i+1,itera,wx.YELLOW)
							else:
								myGrid.SetCellValue(i+1,itera, str(j[itera]))
						elif itera == 13 :
							if j[itera] == 'S': 
								myGrid.SetCellValue(i+1,itera, str(j[itera]))
								myGrid.SetCellBackgroundColour(i+1,itera,wx.BLUE)
								myGrid.SetCellTextColour(i+1, itera, wx.WHITE)
							else:
								myGrid.SetCellValue(i+1,itera, str(j[itera]))
						
							

	   
		
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