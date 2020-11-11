import tkinter as tk
from tkinter import *
import wx
import wx.grid as gridlib
import pandas as pd
########################################################################
class MyForm(wx.Frame):
	
	def __init__(self):
		"""Constructor"""
		wx.Frame.__init__(self, parent=None, title="Lector MOV2000 - VALIDATOR",size=(900,300))
		panel = wx.Panel(self)
		itera = 0
		nombres =['Numtar','NumEst','NumAut','PlanCuot','NumCuot','Moneda','Importe','CodPais','ImporteOrig','BinTarjeta','NombreComercio','BancoEstab','NumtarMov2000','Token','NumToken','PosDataCode','VisaRelease']
		rango = len(nombres)
		LecturaCamposBasicos = pd.read_csv('CSV_MOV2000.CSV', index_col=0)
		CantidadTranasacciones = len(LecturaCamposBasicos)
		myGrid = gridlib.Grid(panel)
		myGrid.CreateGrid(CantidadTranasacciones + 1, rango)

		
		#print(LecturaCamposBasicos)

		for itera in range(rango):
			
			for i, j in LecturaCamposBasicos.iterrows():
					
					
					if i == 0:
						
						myGrid.SetCellValue(i,itera, str(nombres[itera]))
						myGrid.SetCellTextColour(i, itera, wx.WHITE)
						myGrid.SetCellBackgroundColour(i,itera,wx.BLACK)
						myGrid.SetCellValue(i+1,itera, str(j[itera]))
					

					else:   
						#print("esto es itera:",j[2 + itera])
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

if __name__ == "__main__":
	app = wx.App()
	display = MyForm().Show()
	#frame = MainFrame()
	app.MainLoop()