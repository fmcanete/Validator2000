 
# #Importar las librerias
import tkinter as tk
from tkinter import *
import pandas as pd

# IMPORTAR LOS ARCHIVOS
import setUp,archivos


########################################################################
#####################VARIABLES GLOBALES#################################
########################################################################

mov2000Plano = "a"
listaArchivo = []
contadorArchivo = 0
CSV_MOV2000 = "a"
listaCompleta = []

########################################################################
##################### INVOCAR METODOS #################################
########################################################################

	

mov2000Plano = archivos.manejoDeLosArchivosTXT.abrirArchivo(mov2000Plano)

listaArchivo, contadorArchivo = archivos.manejoDeLosArchivosTXT.recorrerArchivoMov2000(mov2000Plano, listaArchivo, contadorArchivo)

listaCompleta = archivos.manejoDeLosArchivosTXT.subStringLista(listaArchivo, contadorArchivo, listaCompleta)

archivos.manejoDeLosArchivosTXT.cerrarArchivo(mov2000Plano)

window = setUp.OpenForms.abrirFormulario
setUp.OpenForms.abrirFormulario()