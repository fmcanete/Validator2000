import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import wx.grid as gridlib
from timeit import timeit
import time as time
# IMPORTAR LOS ARCHIVOS
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time

ventana = Tk()
ventana.title("Cargando..") 
bar = Progressbar(ventana,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

def start1():
    Total = 100
    descarga = 0
    velocidad = 1
    while(descarga<Total):
        time.sleep(0.05)
        bar['value']+=1
        descarga+=velocidad
        percent.set(str(int((descarga/Total)*100))+"%")
        text.set(str(descarga)+"/"+str(Total)+" Carga Completada")
        ventana.update_idletasks()

    percent.set("Espere.. armando grilla")
    ventana.update_idletasks()

percent = StringVar()
text = StringVar()

percentLabel = Label(ventana,textvariable=percent).pack()
taskLabel = Label(ventana,textvariable=text).pack()