from time import sleep
import time, re, os, csv 
import pandas as pd

class manejoDeLosArchivosTXT():
	

	def abrirArchivo(m240Plano,ruta):
		try:
			m240Plano = open(ruta, "r",encoding = 'cp850')
			#open("MOV2000.txt", "r")
			return m240Plano
		except Exception:
			return 10	#se devuelve un valor 10 entero arbitrariamente para evaluar excepciones posteriores

	def cerrarArchivo(m240Plano):
		m240Plano.close()

	def recorrerArchivoM240(m240Plano, listaArchivo, contadorArchivo):	#ESTE METODO RECORRE EL ARCHIVO Y GUARDA LA LISTA CON LOS VALORES
		try:
			contadorArchivo = 0
			listaArchivo = []
			for linea in m240Plano:				#Se modifica el for, se guarda toda la trama incluyendo saltos de linea
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
			cont = 0
			Tipo 		= []
			MkOffLine 	= []
			MkBanda 	= []
			Tarjeta 	= []
			Libre1 		= []
			NCupon 		= []
			Dia 		= []
			Mes 		= []
			Anio 		= []
			Libre2 		= []
			Autoriz 	= []
			Importe 	= []
			Cuotas 		= []
			TNABco 		= []
			Ramo 		= []
			MConver 	= []
			Te1 		= []
			TelOrig 	= []
			TelDes 		= []
			TelTpo 		= []
			FinReg 		= []

			####header###
			contEsta = 0
			establecimiento = []


			finRegistro = contadorArchivo - 1

			aux = listaArchivo[finRegistro]

			if listaArchivo[contadorArchivo] == '':	#en el m240 la primera transaccion ya es de detalle. no tiene header
				
				while listaArchivo[cont] != "":
					cadena = listaArchivo[cont]
					cont = cont+1
					if cadena[0] != "0":
						Tipo.append(str(cadena[1:1]))
						MkOffLine.append(cadena[1:2])
						MkBanda.append(cadena[2:3])
						Tarjeta.append(cadena[3:19])
						Libre1.append(cadena[19:20])
						NCupon.append(cadena[20:28])
						Dia.append(cadena[28:30])
						Mes.append(cadena[30:32])
						Anio.append(cadena[32:34])
						Libre2.append(cadena[34:36])
						Autoriz.append(cadena[36:42])
						Importe.append(cadena[42:57])
						Cuotas.append(cadena[57:59])
						TNABco.append(cadena[59:64])
						Ramo.append(cadena[64:72])
						MConver.append(cadena[72:74])
						Te1.append(cadena[74:77])
						TelOrig.append(cadena[77:87])
						TelDes.append(cadena[87:103])
						TelTpo.append(cadena[103:107])

						contEsta = contEsta+1 #contador para nivelar la cantidad de establecimientos en el else

						#
						#establecimiento.append(cadena[31:41])
						#FILLER.append(cadena[172:184])
					else:
						i = 1
						for i in range(contEsta):
							establecimiento.append(cadena[30:40])
						contEsta = 0
					pass
				pass
				
				#data = {'establecimiento': establecimiento,'Tipo':Tipo ,'MkOffLine':MkOffLine,'MkBanda':MkBanda,'Tarjeta':Tarjeta,'Libre1':Libre1, 'NCupon': NCupon}
				data = {'establecimiento': establecimiento,'Tipo':Tipo ,'MkOffLine':MkOffLine,'MkBanda':MkBanda,
				'Tarjeta':Tarjeta,'Libre1':Libre1, 'NCupon': NCupon,'Dia':Dia,'Mes':Mes,'Anio':Anio,'Libre2':Libre2,
				'Autoriz':Autoriz,'Importe':Importe,'Cuotas':Cuotas,'TNABco':TNABco,'Ramo':Ramo,'MConver':MConver,
				'Te1':Te1,'TelOrig':TelOrig,'TelDes':TelDes,'TelTpo':TelTpo}

				#df = pd.DataFrame(data, columns =['establecimiento', 'Tipo','MkOffLine','MkBanda','Tarjeta','Libre1', 'NCupon'])
				df = pd.DataFrame(data, columns =['establecimiento', 'Tipo','MkOffLine','MkBanda','Tarjeta','Libre1', 'NCupon',
				'Dia','Mes','Anio','Libre2','Autoriz','Importe','Cuotas','TNABco','Ramo','MConver','Te1','TelOrig','TelDes',
				'TelTpo'])

				df.to_csv('CSV_M240.CSV', sep=';')



				return listaCompleta

			else:
				return 10 #Si no es un Header devuelvo un 10 para regresar una Excepción


		except(Exception,ValueError):
			print("Formato Erroneo de archivo 1234")
			return 10

	