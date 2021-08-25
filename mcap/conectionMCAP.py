# CONEXION A BD SQL

import pyodbc
import tkinter as tk
from tkinter import messagebox


def llamado():

    server = 'wapp-ttpm025'
    bd = 'CapturaStratus'
    usuario = 'Captura'
    contrasena = 'Captura'

    try:
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD='+contrasena+'')
        print("Conexion OK")
        messagebox.showinfo(message="¡Conexión OK!", title="OK")
    except :
        messagebox.showinfo(message="¡Fallo en Conexión!", title="Error")
        print("Fallo Conexion")
        pass

