# #Importar las librerias
import tkinter as tk
import ventanaProgress	
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
# IMPORTAR LOS ARCHIVOS
from mcap import archivos, Grilla,setUp_MASTER, logicaBD

def graficoTipoDeTarjetas(a,b,c,d):
    cantidad=[a,c]
    tipoTarjetas=[b,d]
    colores = ["#FFD97D","#FF9B85"]
    plt.pie(cantidad, labels=tipoTarjetas,autopct="%0.1f %%", colors=colores)
    plt.axis("equal")
    plt.show()
    

def graficoMarcaSegmento(a,b,c,d):
    cantidad=[a,c]
    tipoTarjetas=[b,d]
    colores = ["#FFD97D","#FF9B85"]
    plt.pie(cantidad, labels=tipoTarjetas,autopct="%0.1f %%", colors=colores)
    plt.axis("equal")
    plt.show()

def generarReportePDF():

    ventana = ventanaProgress.start1()
       
    x=np.linspace(-3,3,100)
    y1=np.sin(x)
    y2=np.cos(x)
    y3=1/(1+np.exp(-x))
    y4=np.exp(x)

    def retFig(x, y):
        fig = plt.figure()
        a= plt.plot(x, y)
        return fig

    fig1 = retFig(x, y1)
    fig2 = retFig(x, y2)
    fig3 = retFig(x, y3)   
    fig4 = retFig(x, y4)

    pp = PdfPages('Save multiple plots as PDF.pdf')
    pp.savefig(fig1)
    pp.savefig(fig2)
    pp.savefig(fig3)
    pp.savefig(fig4)
    pp.close()
    
    #cierra el "CARGANDO"
    ventana.destroy()
