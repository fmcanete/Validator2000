# CONEXION A BD SQL

import pyodbc
import tkinter as tk
from tkinter import messagebox,filedialog
import configparser

def abrir_archivo():
    archivo_abierto=filedialog.askopenfilename(initialdir = "/", #esto abre en el raiz. ver de mejorar y poner donde esta el proyecto
    title = "Seleccione archivo",filetypes = (("txt files","*.txt"),
    ("all files","*.*")))
    return(archivo_abierto)


def llamado():
    config = configparser.ConfigParser()
    config.read('mcap\\Aconfig.ini')

    server = config['DEFAULT']['SERVER_NAME']
    bd = config['DEFAULT']['DB_NAME']
    usuario = config['DEFAULT']['DB_USER']
    contrasena = config['DEFAULT']['DB_PASSWORD']

    ruta = abrir_archivo()
    elbulk = 'BULK INSERT CapturaStratus.dbo.MOV2000_V1 FROM' + " '" + ruta + "'"


    try:
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD='+contrasena+'')
        print("Conexion OK")
        cursor = conexion.cursor()
        cursor.execute('TRUNCATE TABLE CapturaStratus.dbo.MOV2000_V1')
        cursor.execute(elbulk)
        
        conexion.commit()
        conexion.close()


        messagebox.showinfo(message='¡Subida OK al '+server+', verificar MOV2000_V1 en CapturaStratus!', title="OK")
        #conexion.close()
        #cursor.close()
    
    except :
        messagebox.showinfo(message="¡Fallo en Conexión!", title="Error")
        print("Fallo Conexion")
        pass

