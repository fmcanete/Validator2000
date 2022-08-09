# CONEXION A BD SQL

import pyodbc
import tkinter as tk
from tkinter import messagebox,filedialog
import configparser
import time,os
import json
from json2html import *
import subprocess
from mcap import conectionMCAP

#######################################

def leerParametrosConexion(server, bd, usuario, contrasena):
    server, bd, usuario, contrasena = conectionMCAP.configBD(server, bd, usuario, contrasena)
    return server, bd, usuario, contrasena


########################STORE PROCEDURE####################################
def spCamposBasicos(bd, conexion):
    sp_crearTablaCamposBasicos = 'exec ' +bd+ '.dbo.sp_crearTablaCamposBasicos' 
    llamada_sp_crearTablaCamposBasicos = conectionMCAP.accion(conexion, sp_crearTablaCamposBasicos)

    sp_insertarCamposBasicos = 'exec ' +bd+ '.dbo.sp_insertarCamposBasicos' 
    llamada_sp_insertarCamposBasicos = conectionMCAP.accion(conexion, sp_insertarCamposBasicos) 


def spCamposBasicos_ParaComparar(bd, conexion):

    sp_crearTablaCamposBasicos = 'exec ' +bd+ '.dbo.sp_crearTablaCamposBasicos'
    llamada_sp_crearTablaCamposBasicos = conectionMCAP.accion(conexion, sp_crearTablaCamposBasicos)

    sp_insertarCamposBasicos = 'exec ' +bd+ '.dbo.sp_insertarCamposBasicos' 
    llamada_sp_insertarCamposBasicos = conectionMCAP.accion(conexion, sp_insertarCamposBasicos) 
    
    sp_crearTablaCamposBasicos_2 = 'exec ' +bd+ '.dbo.sp_crearTablaCamposBasicos_2' 
    llamada_sp_crearTablaCamposBasicos_2 = conectionMCAP.accion(conexion, sp_crearTablaCamposBasicos_2)

    sp_insertarCamposBasicos_2 = 'exec ' +bd+ '.dbo.sp_insertarCamposBasicos_2' 
    llamada_sp_insertarCamposBasicos_2 = conectionMCAP.accion(conexion, sp_insertarCamposBasicos_2)

def spTipoTarjetas(bd, conexion):
    sp_TipoTarjeta = 'exec ' +bd+ '.dbo.sp_TipoDeTarjetas' 
    llamada_sp_TipoTarjeta = conectionMCAP.accion(conexion, sp_TipoTarjeta)
    result_TipoTarjeta = conectionMCAP.consultaSP(conexion, sp_TipoTarjeta)
    return result_TipoTarjeta

def sp_TotalENP(bd, conexion):
    sp_TotalENP = 'exec ' +bd+ '.dbo.sp_TotalENP' 
    llamada_sp_TotalENP = conectionMCAP.accion(conexion, sp_TotalENP)
    result_TotalENP = conectionMCAP.consultaSP(conexion, sp_TotalENP)
    return result_TotalENP    

def sp_TotalPG(bd, conexion):
    sp_TotalPG = 'exec ' +bd+ '.dbo.sp_TotalPG' 
    llamada_sp_TotalPG = conectionMCAP.accion(conexion, sp_TotalPG)
    result_TotalPG = conectionMCAP.consultaSP(conexion, sp_TotalPG)
    return result_TotalPG

def comparacionMov2000(bd, conexion):
    sp_comparaMov2000 = 'exec ' +bd+ '.dbo.sp_comparaMov2000' 
    llamada_sp_comparaMov2000 = conectionMCAP.accion(conexion, sp_comparaMov2000)
    resultComparacionMov2000 = conectionMCAP.consultaSP(conexion, sp_comparaMov2000)
    print("SP COMPARACION: ",resultComparacionMov2000)
    return resultComparacionMov2000



################################## JSON'S #######################################  

def splitearCamposParaJsonTipTar(tipoTarjetas, filas, columna):
    canTrxDebito = tipoTarjetas[0][0]
    tipTarDeb = tipoTarjetas[0][1]
    canTrxCred = tipoTarjetas[1][0]
    tipTarCred = tipoTarjetas[1][1]
    total = tipoTarjetas[0][0] + tipoTarjetas[1][0]
    return canTrxDebito, tipTarDeb, canTrxCred, tipTarCred, total

def splitearCamposParaJsonENP(tipoENP):
    canTrxENP = tipoENP[0][0]
    codBanco = tipoENP[0][1] 
    return canTrxENP, codBanco    

def splitearCamposParaJsonPG(tipoPG):
    canTrxPG = tipoPG[0][0]
    cuotas = tipoPG[0][1] 
    return canTrxPG, cuotas 

def splitearCamposParaJsonComp2000(comparaMov2000):
    canTrx = comparaMov2000[0][0]
    tarjeta = comparaMov2000[0][1] 
    return canTrx, tarjeta 

def armadoBasicoJsonTipTar(canTrxDebito, tipTarDeb, canTrxCred, tipTarCred, total):
    dataTipTar = {"TIPO DE TARJETAS":[{"Tipo":tipTarDeb,"Cantidad":canTrxDebito},{"Tipo":tipTarCred ,"Cantidad":canTrxCred},]},{"Total de Transacciones":total}
    #dataTipTar = {"TIPO DE TARJETAS":[{"Tipo":tipTarDeb,"Cantidad":canTrxDebito},{"Tipo":tipTarCred ,"Cantidad":canTrxCred},{"Total de Transacciones":total}]}
    return dataTipTar

def armadoBasicoJsonENP(a1, b1):
    dataENP = {"TIPO DE EMISION": 	[  {"Tipo":"ENP","Cantidad":a1,"Codigo de banco":b1}] 	}
    return dataENP

def armadoBasicoJsonPG(c1, d1):
    dataPG = {"TIPO DE PLAN": 	[  {"Tipo":"Plan Gobierno","Cantidad":c1,"Cuotas":d1}] 	}
    return dataPG

def armadoBasicoJsonComparaMov2000(a1, b1):
    dataComparacion = {"COMPARACION": 	[  {"Tipo":"Mov2000","Cantidad":a1,"Tarjeta":b1}] 	}
    return dataComparacion    

def reporteJson(jsonParametroCompMov2000):
    archivo_HTML = open('Resultados.html', "w")
    #archivo_HTML.write("""<h2><span class="text"></span><span class="span">
    #<img class="goldT" src="validator2.png"  WIDTH=200 HEIGHT=50>
    #</span></h2>""")
    archivo_HTML.write("""
    <body bgcolor="5CCC52" style="background-repeat: no-repeat; background-position: down center;>
        div align="center">
            <img aligne="center" src="validator2.png"  WIDTH=175 HEIGHT=44>	
            <h1 align="center"> <strong>REPORTE DEL RESULTADO DE LAS PRUEBAS DEL MOV2000 </strong> </h1>
    </div>
    

    </body>""")
    
    comparacionMov2000 = json2html.convert(json = jsonParametroCompMov2000)
    
    ### TIPOS DE TARJETA + TOTAL###

    archivo_HTML.write("""<div>""")
    archivo_HTML.write(""" 
        <div style= float:left; margin-right: 50px>""")
    archivo_HTML.write(comparacionMov2000)
    archivo_HTML.write("<br>")
    #archivo_HTML.write(ENP)
    archivo_HTML.write("<br>")
    #archivo_HTML.write(PG)
    archivo_HTML.write("""</div>""")

    archivo_HTML.write(""" 
        <div style= float:right; margin-left: 50px>""")
    archivo_HTML.write(comparacionMov2000)
    archivo_HTML.write("<br>")
    #archivo_HTML.write(ENP)
    archivo_HTML.write("<br>")
    #archivo_HTML.write(PG)    
    archivo_HTML.write("""</div>""")
    '''
    archivo_HTML.write(""" 
        <div style= float:center>""")
    archivo_HTML.write(TipTar)
    archivo_HTML.write("<br>")
    archivo_HTML.write(ENP)
    archivo_HTML.write("<br>")
    archivo_HTML.write(PG)    
    archivo_HTML.write("""</div>""")
    '''


    archivo_HTML.write("""</div>""")

    '''
    archivo_HTML.write(""" 
        <div align="left">""")
    archivo_HTML.write(TipTar)
    archivo_HTML.write("<br>")
    archivo_HTML.write(ENP)
    archivo_HTML.write("<br>")
    archivo_HTML.write(PG)    
    archivo_HTML.write("""</div>""")
    
        ### TIPOS DE TARJETA + TOTAL###
    archivo_HTML.write(""" 
        <div align="center">""")
    archivo_HTML.write(TipTar)
    archivo_HTML.write("<br>")
    archivo_HTML.write(ENP)
    archivo_HTML.write("<br>") 
    archivo_HTML.write(PG)    
    archivo_HTML.write("""</div>""")
          



    ### EMISION NO PRISMA ###
    archivo_HTML.write(""" 
        <div align="left">""")
    archivo_HTML.write(ENP)
    archivo_HTML.write("""</div>""")
    ### EMISION NO PRISMA ###
    archivo_HTML.write(""" 
        <div align="right">""")
    archivo_HTML.write(PG)
    archivo_HTML.write("""</div>""")'''
    
    ###NO TOCAR QUE ANDA###
    #archivo_HTML.write(TipTar)
    #archivo_HTML.write("<br>")
    #archivo_HTML.write(ENP)
    #archivo_HTML.write("<br>")
    #archivo_HTML.write(PG)
    archivo_HTML.close()
    os.system("Resultados.html")
    ###NO TOCAR QUE ANDA### 



    ########################################## NO BORRAR  DESPUES ###############
def reporteJson2(jsonParametroTipTar, jsonParametroENP, jsonParametroPG, jsonParametroCompMov2000):
        archivo_HTML = open('Resultados.html', "w")
    #archivo_HTML.write("""<h2><span class="text"></span><span class="span">
    #<img class="goldT" src="validator2.png"  WIDTH=200 HEIGHT=50>
    #</span></h2>""")
        archivo_HTML.write("""
    <body bgcolor="5CCC52" style="background-repeat: no-repeat; background-position: down center;>
        div align="center">
            <img aligne="center" src="validator2.png"  WIDTH=175 HEIGHT=44>	
            <h1 align="center"> <strong>REPORTE DEL RESULTADO DE LAS PRUEBAS DEL MOV2000 </strong> </h1>
    </div>
    

    </body>""")
    
        TipTar = json2html.convert(json = jsonParametroTipTar)
        ENP = json2html.convert(json = jsonParametroENP)
        PG = json2html.convert(json = jsonParametroPG)
    
    ### TIPOS DE TARJETA + TOTAL###

        archivo_HTML.write("""<div>""")
        archivo_HTML.write(""" 
        <div style= float:left; margin-right: 50px>""")
        archivo_HTML.write(TipTar)
        archivo_HTML.write("<br>")
        archivo_HTML.write(ENP)
        archivo_HTML.write("<br>")
        archivo_HTML.write(PG)
        archivo_HTML.write("""</div>""")

        archivo_HTML.write(""" 
        <div style= float:right; margin-left: 50px>""")
        archivo_HTML.write(TipTar)
        archivo_HTML.write("<br>")
        archivo_HTML.write(ENP)
        archivo_HTML.write("<br>")
        archivo_HTML.write(PG)    
        archivo_HTML.write("""</div>""")
        '''
    archivo_HTML.write(""" 
        <div style= float:center>""")
    archivo_HTML.write(TipTar)
    archivo_HTML.write("<br>")
    archivo_HTML.write(ENP)
    archivo_HTML.write("<br>")
    archivo_HTML.write(PG)    
    archivo_HTML.write("""</div>""")
    '''


        archivo_HTML.write("""</div>""")

        '''
    archivo_HTML.write(""" 
        <div align="left">""")
    archivo_HTML.write(TipTar)
    archivo_HTML.write("<br>")
    archivo_HTML.write(ENP)
    archivo_HTML.write("<br>")
    archivo_HTML.write(PG)    
    archivo_HTML.write("""</div>""")
    
        ### TIPOS DE TARJETA + TOTAL###
    archivo_HTML.write(""" 
        <div align="center">""")
    archivo_HTML.write(TipTar)
    archivo_HTML.write("<br>")
    archivo_HTML.write(ENP)
    archivo_HTML.write("<br>") 
    archivo_HTML.write(PG)    
    archivo_HTML.write("""</div>""")
          



    ### EMISION NO PRISMA ###
    archivo_HTML.write(""" 
        <div align="left">""")
    archivo_HTML.write(ENP)
    archivo_HTML.write("""</div>""")
    ### EMISION NO PRISMA ###
    archivo_HTML.write(""" 
        <div align="right">""")
    archivo_HTML.write(PG)
    archivo_HTML.write("""</div>""")'''
    
    ###NO TOCAR QUE ANDA###
    #archivo_HTML.write(TipTar)
    #archivo_HTML.write("<br>")
    #archivo_HTML.write(ENP)
    #archivo_HTML.write("<br>")
    #archivo_HTML.write(PG)
        archivo_HTML.close()
        os.system("Resultados.html")
    ###NO TOCAR QUE ANDA### 