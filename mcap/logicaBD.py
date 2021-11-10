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

def armadoBasicoJsonTipTar(canTrxDebito, tipTarDeb, canTrxCred, tipTarCred, total):
    dataTipTar = {"TIPO_TARJETAS":[{"TIPO":tipTarDeb,"Cantidad":canTrxDebito},{"TIPO":tipTarCred ,"Cantidad":canTrxCred},{"TOTAL":total}]}
    #dataTipTar = 	{"TIPO_TARJETAS": 	[  {"TIPO":tipTarDeb,"Cantidad":canTrxDebito},    {"TIPO":tipTarCred ,"Cantidad":canTrxCred},	{"TOTAL":total}			]}
    return dataTipTar

def armadoBasicoJsonENP(a1, b1):
    dataENP = {"TIPO DE EMISION": 	[  {"TIPO":"ENP","Cantidad":a1,"codbanco":b1}] 	}
    return dataENP

def armadoBasicoJsonPG(c1, d1):
    dataPG = {"TIPO DE PLAN": 	[  {"TIPO":"Plan Gobierno","Cantidad":c1,"Cuotas":d1}] 	}
    return dataPG

def reporteJson(jsonParametroTipTar, jsonParametroENP, jsonParametroPG):
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
    archivo_HTML.write(""" 
        <div align="center">""")
    archivo_HTML.write(TipTar)
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
    archivo_HTML.write("""</div>""")
    
    ###NO TOCAR QUE ANDA###
    #archivo_HTML.write(TipTar)
    #archivo_HTML.write("<br>")
    #archivo_HTML.write(ENP)
    #archivo_HTML.write("<br>")
    #archivo_HTML.write(PG)
    archivo_HTML.close()
    os.system("Resultados.html")
    ###NO TOCAR QUE ANDA### 