# CONEXION A BD SQL

import pyodbc
import tkinter as tk


def llamado():

    server = 'wapp-ttpm025'
    bd = 'CapturaStratus'
    usuario = 'Captura'
    contrasena = 'Captura'

    try:
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD='+contrasena+'')
        print("Conexion OK")
    except :
        print("Fallo Conexion")
        pass

