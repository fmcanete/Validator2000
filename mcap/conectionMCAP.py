# CONEXION A BD SQL

import pyodbc
import tkinter as tk
from tkinter import messagebox,filedialog
import configparser
import time,os
import json
from json2html import *
import subprocess
from mcap import logicaBD

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

def consultaSP(connection,query):
    cursor = connection.cursor()
    cursor.execute(query)
    dato = cursor.fetchall()

    return dato       

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

            logicaBD.spCamposBasicos(bd, conexion)

            #PARA PLAN GOBIERNO
            tipoTarjetas = logicaBD.spTipoTarjetas(bd, conexion)
            filas = len(tipoTarjetas)
            columna = len(tipoTarjetas[0])
            a, b, c, d = logicaBD.splitearCamposParaJsonPG(tipoTarjetas, filas, columna)
            jsonParametroPG = logicaBD.armadoBasicoJsonPG(a,b, c, d)
            print("jsonParametro = ", jsonParametroPG)

            #PARA EMISION NO PRISMA
            tipoENP = logicaBD.sp_TotalENP(bd, conexion)
            a1, b1 = logicaBD.splitearCamposParaJsonENP(tipoENP)
            jsonParametroENP = logicaBD.armadoBasicoJsonENP(a1, b1)


            #Se agregan los select para consultas
            total = consulta(conexion,"Select count(*) from "+bd+".dbo.MOV2000_V1 where SUBSTRING(Info,1,1) = 'D'")        
            planesGob = consulta(conexion,"Select count(*) from "+bd+".dbo.MOV2000_V1 where SUBSTRING(Info,593,1) = '7'")
            
            #emisionNP = consulta(conexion,"Select count(*) from "+bd+".dbo.MOV2000_V1 where SUBSTRING(Info,397,3) = '998'")
            
            ###YA ESTA HECHO###
            #trxDebito = consulta(conexion,"Select count(*) from "+bd+".dbo.MOV2000_V1 where SUBSTRING(Info,319,1) = 'E'")
            #trxCredito = consulta(conexion,"Select count(*) from "+bd+".dbo.MOV2000_V1 where SUBSTRING(Info,319,1) = '1'")
            
            #print('El MOV2000 tiene: ' + total + ' transacciones')

            conexion.commit()
            conexion.close()

            ####JSON####
            logicaBD.reporteJson(jsonParametroPG, jsonParametroENP)
            #logicaBD.reporteJson(jsonParametroENP)
            ####JSON####

            logDatosBDD = open('mcap\\BDD\\logDatosBDD.txt', "w") 
            logDatosBDD.write('MOV2000 subido: '+ruta)
            logDatosBDD.write('\n')
            logDatosBDD.write('\n')
            loggeador(logDatosBDD,ruta,total,'- El MOV2000 tiene: ')
            loggeador(logDatosBDD,ruta,planesGob,'- Cantidad Planes Gob: ')
            #loggeador(logDatosBDD,ruta,emisionNP,'- Cantidad EnP: ')
            #loggeador(logDatosBDD,ruta,trxDebito,'- Cantidad Debito: ')
            #loggeador(logDatosBDD,ruta,trxCredito,'- Cantidad Credito: ')
            logDatosBDD.close()
            
            timestamp = time.strftime('%Y%m%d%H%M%S')
            os.rename('mcap\\BDD\\logDatosBDD.txt', 'mcap\\BDD\\logDatosBDD_'+timestamp+'.txt')

            ####################################RESULTADOS JSON-HTML##############################################
            #      #json_PlanGob = json2html.convert(json = result_json_PlanGob)
            
            '''input = {
                "Archivo ":ruta,
                "Cantidad de Transacciones ":total,
                "Transacciones de Crédito ":trxCredito,
                "Transacciones de Débito ":trxDebito,
                "Planes Gobierno ": planesGob
            }'''
            #           test = json2html.convert(json = input)
            #           print(test)
            '''    print(json_PlanGob)
            archivo_HTML = open('Resultados.html', "w")
            archivo_HTML.write("""<h2><span class="text"></span><span class="span">
            <img class="goldT" src="validator2.png"  WIDTH=200 HEIGHT=50>
            </span></h2>""")
            #           archivo_HTML.write(test)
            archivo_HTML.write(json_PlanGob)
            archivo_HTML.close()
            os.system("Resultados.html")'''

            ####################################RESULTADOS JSON-HTML##############################################      


            messagebox.showinfo(message='¡Subida OK al '+server+', verificar MOV2000_V1 en '+bd+'!', title="OK")
            #os.rename('Resultados.html', 'mcap\\BDD\\Resultados_'+timestamp+'.html')
            #messagebox.showinfo(message='El MOV2000 tiene: ' + total + ' transacciones', title="Cantidad")        
        except:
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

