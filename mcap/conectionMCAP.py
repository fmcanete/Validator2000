# CONEXION A BD SQL

import pyodbc
import tkinter as tk
from tkinter import messagebox,filedialog
import configparser
import time,os

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
        #Conexion a la BDD
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD='+contrasena+'')
        print("Conexion OK")
        #Se arma el cursos para ejecutar el truncate y el Bulk Insert del primer MOV2000 

        def accion(connection,query):
            cursor = connection.cursor()
            cursor.execute(query)

        def consulta(connection,query):
            cursor = connection.cursor()
            cursor.execute(query)
            dato = cursor.fetchone()

            while dato:
                total = str(dato[0])
                dato = cursor.fetchone()
            return total   

        truncate = accion(conexion,'TRUNCATE TABLE CapturaStratus.dbo.MOV2000_V1') 
        bulk = accion (conexion,elbulk)
        
        #Se agregan los select para consultas
        total = consulta(conexion,"Select count(*) from CapturaStratus.dbo.MOV2000_V1 where SUBSTRING(Info,1,1) = 'D'")        
        emisionNP = consulta(conexion,"Select count(*) from CapturaStratus.dbo.MOV2000_V1 where SUBSTRING(Info,397,3) = '998'")
        planesGob = consulta(conexion,"Select count(*) from CapturaStratus.dbo.MOV2000_V1 where SUBSTRING(Info,593,1) = '7'")

        #print('El MOV2000 tiene: ' + total + ' transacciones')



        conexion.commit()
        conexion.close()

        def loggeador(log,ruta,total,mensaje):
            log.write(mensaje + total + ' transacciones')
            log.write('\n')

        logDatosBDD = open('mcap\\BDD\\logDatosBDD.txt', "w") 
        logDatosBDD.write('MOV2000 subido: '+ruta)
        logDatosBDD.write('\n')
        logDatosBDD.write('\n')
        loggeador(logDatosBDD,ruta,total,'- El MOV2000 tiene: ')
        loggeador(logDatosBDD,ruta,planesGob,'- Cantidad Planes Gob: ')
        loggeador(logDatosBDD,ruta,emisionNP,'- Cantidad EnP: ')
        logDatosBDD.close()
        
        timestamp = time.strftime('%Y%m%d%H%M%S')
        os.rename('mcap\\BDD\\logDatosBDD.txt', 'mcap\\BDD\\logDatosBDD_'+timestamp+'.txt')



        messagebox.showinfo(message='¡Subida OK al '+server+', verificar MOV2000_V1 en CapturaStratus!', title="OK")
        #messagebox.showinfo(message='El MOV2000 tiene: ' + total + ' transacciones', title="Cantidad")

    
    except :
        messagebox.showinfo(message="¡Fallo en Conexión!", title="Error")
        print("Fallo Conexion")
        pass

