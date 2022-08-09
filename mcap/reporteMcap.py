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
def reporteJson2(jsonParametroTipTar, jsonParametroENP, jsonParametroPG):
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