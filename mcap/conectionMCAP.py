# CONEXION A BD SQL

import pyodbc
import tkinter as tk
from tkinter import messagebox,filedialog
import configparser
import time,os

def abrir_archivo():
    #esto abre en el raiz. ver de mejorar y poner donde esta el proyecto
    archivo_abierto=filedialog.askopenfilename(initialdir = "/", 
    title = "Seleccione archivo",filetypes = (("txt files","*.txt"),
    ("all files","*.*")))
    return(archivo_abierto)

def configBD ():
    config = configparser.ConfigParser()
    config.read('mcap\\Aconfig.ini')

    server = config['DEFAULT']['SERVER_NAME']
    bd = config['DEFAULT']['DB_NAME']
    usuario = config['DEFAULT']['DB_USER']
    contrasena = config['DEFAULT']['DB_PASSWORD']

    return server, bd, usuario, contrasena

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

def loggeador(log,ruta,total,mensaje):
    log.write(mensaje + total + ' transacciones')
    log.write('\n')

def llamado():
    
    ruta = abrir_archivo()
    server, bd, usuario, contrasena = configBD()
    
    if ruta != '':

        elbulk = 'BULK INSERT '+bd+'.dbo.MOV2000_V1 FROM' + " '" + ruta + "'"

        try:
            #Conexion a la BDD
            conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD='+contrasena+'')
            print("Conexion OK")

                       
            queryTruncateBulk = 'TRUNCATE TABLE '+bd+'.dbo.MOV2000_V1'

            truncate = accion(conexion,queryTruncateBulk) 
            EjecutarBulk = accion (conexion,elbulk)

            ########################STORE PROCEDURE####################################
            sp_crearTablaCamposBasicos = 'exec ' +bd+ '.dbo.sp_crearTablaCamposBasicos' 
            llamada_sp_crearTablaCamposBasicos = accion(conexion, sp_crearTablaCamposBasicos)

            sp_insertarCamposBasicos = 'exec ' +bd+ '.dbo.sp_insertarCamposBasicos' 
            llamada_sp_insertarCamposBasicos = accion(conexion, sp_insertarCamposBasicos)         
            ########################STORE PROCEDURE####################################

            #Se agregan los select para consultas
            total = consulta(conexion,"Select count(*) from "+bd+".dbo.MOV2000_V1 where SUBSTRING(Info,1,1) = 'D'")        
            emisionNP = consulta(conexion,"Select count(*) from "+bd+".dbo.MOV2000_V1 where SUBSTRING(Info,397,3) = '998'")
            planesGob = consulta(conexion,"Select count(*) from "+bd+".dbo.MOV2000_V1 where SUBSTRING(Info,593,1) = '7'")
            trxDebito = consulta(conexion,"Select count(*) from "+bd+".dbo.MOV2000_V1 where SUBSTRING(Info,319,1) = 'E'")
            trxCredito = consulta(conexion,"Select count(*) from "+bd+".dbo.MOV2000_V1 where SUBSTRING(Info,319,1) = '1'")
            #print('El MOV2000 tiene: ' + total + ' transacciones')

            conexion.commit()
            conexion.close()

            logDatosBDD = open('mcap\\BDD\\logDatosBDD.txt', "w") 
            logDatosBDD.write('MOV2000 subido: '+ruta)
            logDatosBDD.write('\n')
            logDatosBDD.write('\n')
            loggeador(logDatosBDD,ruta,total,'- El MOV2000 tiene: ')
            loggeador(logDatosBDD,ruta,planesGob,'- Cantidad Planes Gob: ')
            loggeador(logDatosBDD,ruta,emisionNP,'- Cantidad EnP: ')
            loggeador(logDatosBDD,ruta,trxDebito,'- Cantidad Debito: ')
            loggeador(logDatosBDD,ruta,trxCredito,'- Cantidad Credito: ')
            logDatosBDD.close()
            
            timestamp = time.strftime('%Y%m%d%H%M%S')
            os.rename('mcap\\BDD\\logDatosBDD.txt', 'mcap\\BDD\\logDatosBDD_'+timestamp+'.txt')



            messagebox.showinfo(message='¡Subida OK al '+server+', verificar MOV2000_V1 en '+bd+'!', title="OK")
            #messagebox.showinfo(message='El MOV2000 tiene: ' + total + ' transacciones', title="Cantidad")

        
        except ZeroDivisionError:
            messagebox.showinfo(message="¡Fallo en Conexión!", title="Error")
            print("Fallo Conexion")
            pass

def llamadoComparador():

    ruta = abrir_archivo()
    server, bd, usuario, contrasena = configBD()

    
    #ruta = abrir_archivo()
    if ruta != '':
        ruta2 = abrir_archivo()
        elbulk = 'BULK INSERT '+bd+'.dbo.MOV2000_V1 FROM' + " '" + ruta + "'"
        elbulk2 = 'BULK INSERT '+bd+'.dbo.MOV2000_V2 FROM' + " '" + ruta2 + "'"

        try:
            #Conexion a la BDD
            conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD='+contrasena+'')
            print("Conexion OK")
            #Se arma el cursos para ejecutar el truncate y el Bulk Insert del primer MOV2000 

            #MOV2000_1
            truncate = accion(conexion,'TRUNCATE TABLE '+bd+'.dbo.MOV2000_V1') 
            bulk = accion (conexion,elbulk)

            #MOV2000_2
            truncate2 = accion(conexion,'TRUNCATE TABLE '+bd+'.dbo.MOV2000_V2') 
            bulk2 = accion (conexion,elbulk2)

            query = """SELECT  count(*) FROM """+bd+""".[dbo].[MOV2000_V2] v2 WHERE NOT EXISTS (SELECT * FROM [dbo].[MOV2000_V1] v1 WHERE SUBSTRING(v1.Info,26,4)=SUBSTRING(v2.Info,26,4)
            AND SUBSTRING(v1.Info,36,16)=SUBSTRING(v2.Info,36,16)
            AND SUBSTRING(v1.Info,52,10)=SUBSTRING(v2.Info,52,10)
            AND SUBSTRING(v1.Info,62,9)=SUBSTRING(v2.Info,62,9)
            AND SUBSTRING(v1.Info,319,1)=SUBSTRING(v2.Info,319,1))"""  

            #Se agregan los select para consultas
            comparacion = consulta(conexion,query)
            #print('El MOV2000 tiene: ' + total + ' transacciones')




            conexion.commit()
            conexion.close()

            logDatosBDD = open('mcap\\BDD\\logComparadorBDD.txt', "w") 
            logDatosBDD.write('MOV2000 1: '+ruta)
            logDatosBDD.write('\n')            
            logDatosBDD.write('MOV2000 2: '+ruta2)
            logDatosBDD.write('\n')
            logDatosBDD.write('\n')
            loggeador(logDatosBDD,ruta,comparacion,'- Transacciones de Diferencia: ')
            logDatosBDD.close()
            
            timestamp = time.strftime('%Y%m%d%H%M%S')
            os.rename('mcap\\BDD\\logComparadorBDD.txt', 'mcap\\BDD\\logComparadorBDD_'+timestamp+'.txt')


            if comparacion == '0':
                messagebox.showinfo(message='¡Conexión OK al '+server+', verificar MOV2000_V1 y MOV2000_V2 en '+bd+'! ¡NO HAY DIFERENCIAS!', title="OK")
            
            else:
                messagebox.showwarning(message='¡Conexión OK al '+server+', verificar MOV2000_V1 y MOV2000_V2 en '+bd+'! Hay ' +comparacion+' transacciones de diferencias', title="HAY DIFERENCIAS")                    
            
            #messagebox.showinfo(message='El MOV2000 tiene: ' + total + ' transacciones', title="Cantidad")

        
        except Exception:
            
            messagebox.showerror(message="¡Fallo en Conexión!", title="Error")
            print("Fallo Conexion")
            pass

