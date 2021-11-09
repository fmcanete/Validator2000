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
    print("RESULT TIPO TARJETA: ", result_TipoTarjeta)
    return result_TipoTarjeta

def sp_TotalENP(bd, conexion):
    sp_TotalENP = 'exec ' +bd+ '.dbo.sp_TotalENP' 
    llamada_sp_TotalENP = conectionMCAP.accion(conexion, sp_TotalENP)
    result_TotalENP = conectionMCAP.consultaSP(conexion, sp_TotalENP)
    print("RESULT TIPO TARJETA: ", result_TotalENP)
    return result_TotalENP    


def splitearCamposParaJsonPG(tipoTarjetas, filas, columna):
    ###PARA PLAN GOBIERNO###
    canTrxDebito = tipoTarjetas[0][0]
    tipTarDeb = tipoTarjetas[0][1]
    canTrxCred = tipoTarjetas[1][0]
    tipTarCred = tipoTarjetas[1][1]
    return canTrxDebito, tipTarDeb, canTrxCred, tipTarCred

def splitearCamposParaJsonENP(tipoENP):
    canTrxENP = tipoENP[0][0]
    codBanco = tipoENP[0][1] 
    
    return canTrxENP, codBanco    

def armadoBasicoJsonPG(canTrxDebito, tipTarDeb, canTrxCred, tipTarCred):
    dataPG = 	{"TIPO_TARJETAS": 	[  {"TIPO":"DEBITO","Cantidad":canTrxDebito},    {"TIPO":"CREDITO","Cantidad":canTrxCred}   		 ] 	}
    print("DATA: ", dataPG)
    return dataPG

def armadoBasicoJsonENP(a1, b1):
    print("LLEGUE")
    #dataENP = 	{"TIPO DE EMISION": 	[  {"ENP": a1,"COD BANCO":a2},    	] 	}    
    dataENP = {"TIPO DE EMISION": 	[  {"TIPO":"ENP","Cantidad":a1,"codbanco":b1}] 	}
    print("NO LLEGUE: ", dataENP)
    return dataENP

def reporteJson(jsonParametroPG, jsonParametroENP):
    print("JSON REPORTE: ", jsonParametroENP)
    archivo_HTML = open('Resultados.html', "w")
    archivo_HTML.write("""<h2><span class="text"></span><span class="span">
    <img class="goldT" src="validator2.png"  WIDTH=200 HEIGHT=50>
    </span></h2>""")
    #           archivo_HTML.write(test)
    PG = json2html.convert(json = jsonParametroPG)
    ENP = json2html.convert(json = jsonParametroENP)
    archivo_HTML.write(PG)
    archivo_HTML.write(ENP)
    archivo_HTML.close()
    os.system("Resultados.html")