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



def start1():
    ventana = Tk()
    ventana.title("Cargando..")
    ventana.geometry('300x100')
    bar = Progressbar(ventana,orient=HORIZONTAL,length=300)
    ventana.eval('tk::PlaceWindow . center')
    ventana.iconbitmap('prisma.ico')
    bar.pack(pady=10)
    percent = StringVar()
    text = StringVar()
    percentLabel = Label(ventana,textvariable=percent).pack()
    taskLabel = Label(ventana,textvariable=text).pack()
    Total = 100
    descarga = 0
    velocidad = 2

    while(descarga<Total):
        time.sleep(0.05)
        try:
            bar['value']+=2
            descarga+=velocidad
            percent.set(str(int((descarga/Total)*100))+"%")
            text.set(str(descarga)+"/"+str(Total)+" Carga Completada")
            ventana.update_idletasks()
        except (Exception):
            print('Igualo ante algún error')
            descarga = Total

    percent.set("Espere.. armando grilla")
    ventana.update_idletasks()
    return ventana


