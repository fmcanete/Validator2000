from time import sleep
import time, re, os, csv 
import pandas as pd

class manejoDeLosArchivosTXT():
	

	def abrirArchivo(movrechaPlano,ruta):
		try:
			movrechaPlano = open(ruta, "r",encoding = 'cp850')
			#open("MOV2000.txt", "r")
			return movrechaPlano
		except Exception:
			return 10	#se devuelve un valor 10 entero arbitrariamente para evaluar excepciones posteriores

	def cerrarArchivo(movrechaPlano):
		movrechaPlano.close()

	def recorrerArchivoMovrechazo(movrechaPlano, listaArchivo, contadorArchivo):	#ESTE METODO RECORRE EL ARCHIVO Y GUARDA LA LISTA CON LOS VALORES
		try:
			contadorArchivo = 0
			listaArchivo = []
			for linea in movrechaPlano:				#Se modifica el for, se guarda toda la trama incluyendo saltos de linea
				listaArchivo.append(linea)
				contadorArchivo = contadorArchivo + 1
			
			listaArchivo.append("")					#Se le agrega un espacio vacío a la lista para el WHILE siguiente del parseo

			return listaArchivo, contadorArchivo
		except (MemoryError):
			return 11,11	#aca se queda sin memoria y no puede seguir procesando
		except (UnicodeDecodeError,TypeError,Exception):
			return 10,10 #aca se queda sin memoria y no puede seguir procesando
			
	def subStringLista(listaArchivo, contadorArchivo, listaCompleta):
		try:
			cont = 1
			NUMEST      = []
			TERMINAL    = []

			aux = listaArchivo[0]

			#################

			if aux[0] == '0':	#Si la primera transacción no es un Header no lo leo.
				
				while listaArchivo[cont] != "":
					cadena = listaArchivo[cont]
					cont = cont+1
					if cadena[0] == "0":
						NUMEST.append(cadena[1:16])      
						TERMINAL.append(cadena[16:24])   
    


						########################

					pass
				pass
				
				data = {'NUMEST': NUMEST,'TERMINAL':TERMINAL}

				df = pd.DataFrame(data, columns =['NUMEST','TERMINAL'])

				df.to_csv('CSV_MOVRECHAZOS.CSV', sep=';')



				return listaCompleta

			else:
				return 10 #Si no es un Header devuelvo un 10 para regresar una Excepción


		except(Exception,ValueError):
			print("Formato Erroneo de archivo 1234")
			return 10

	