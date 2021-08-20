from time import sleep
import time, re, os, csv 
import pandas as pd

class manejoDeLosArchivosTXT():
	

	def abrirArchivo(mkprivPlano,ruta):
		try:
			mkprivPlano = open(ruta, "r",encoding = 'cp850')
			#open("MOV2000.txt", "r")
			return mkprivPlano
		except Exception:
			return 10	#se devuelve un valor 10 entero arbitrariamente para evaluar excepciones posteriores

	def cerrarArchivo(mkprivPlano):
		mkprivPlano.close()

	def recorrerArchivoMkpriv(mkprivPlano, listaArchivo, contadorArchivo):	#ESTE METODO RECORRE EL ARCHIVO Y GUARDA LA LISTA CON LOS VALORES
		try:
			contadorArchivo = 0
			listaArchivo = []
			for linea in mkprivPlano:				#Se modifica el for, se guarda toda la trama incluyendo saltos de linea
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
			NUMTAR      = []
			TIPOMOV     = []
			FECHA       = []
			HORA        = []
			NCUPON      = []
			MONEDA      = []
			IMPORTE     = []
			CUOTAS      = []
			NROAUT      = []
			DIASDIFER   = []
			ESTRUBRO    = []
			ESTDENOM    = []
			CODOP       = []
			FECHADIFER  = []
			NUMLOTE     = []
			FECHACIERRE = []
			CODPLAN    = []
			CODRESPU    = []
			DATADIC    = []
			MODOING    = []
			FILLER      = []
			aux = listaArchivo[0]

			#################
			'''numTarMovMes = []
			establecimiento = []
			nroAut =[]
			planCuot =[]
			saltoLinea = []
			aux = listaArchivo[0]'''

			if aux[0] == 'H':	#Si la primera transacción no es un Header no lo leo.
				
				while listaArchivo[cont] != "":
					cadena = listaArchivo[cont]
					cont = cont+1
					if cadena[0] == "D":
						NUMEST.append(cadena[1:16])      
						TERMINAL.append(cadena[16:24])   
						NUMTAR.append(cadena[24:43])     
						TIPOMOV.append(cadena[43:47])    
						FECHA.append(cadena[47:55])      
						HORA.append(cadena[55:61])       
						NCUPON.append(cadena[61:69])     
						MONEDA.append(cadena[69:72])     
						IMPORTE.append(cadena[72:84])    
						CUOTAS.append(cadena[84:86])     
						NROAUT.append(cadena[86:92])     
						DIASDIFER.append(cadena[92:95])  
						ESTRUBRO.append(cadena[95:99])  
						ESTDENOM.append(cadena[99:124])   
						CODOP.append(cadena[124:128])      
						FECHADIFER.append(cadena[128:136]) 
						NUMLOTE.append(cadena[136:140])    
						FECHACIERRE.append(cadena[140:148])
						CODPLAN.append(cadena[148:149])    
						CODRESPU.append(cadena[149:152])   
						DATADIC.append(cadena[152:171])    
						MODOING.append(cadena[171:172])    
						FILLER.append(cadena[172:184])     


						########################
						'''numTarMovMes.append(cadena[35:51])
						establecimiento.append(cadena[51:61])
						nroAut.append(cadena[111:119])
						planCuot.append(cadena[127:129])
						saltoLinea.append(cadena[130:132])'''
					pass
				pass
				
				data = {'NUMEST': NUMEST,'TERMINAL':TERMINAL,'NUMTAR':NUMTAR,'TIPOMOV':TIPOMOV,'FECHA':FECHA,'HORA':HORA,
				'NCUPON':NCUPON,'MONEDA':MONEDA,'IMPORTE':IMPORTE,'CUOTAS':CUOTAS,'NROAUT':NROAUT,'DIASDIFER':DIASDIFER,
				'ESTRUBRO':ESTRUBRO,'ESTDENOM':ESTDENOM,'CODOP':CODOP,'FECHADIFER':FECHADIFER,'NUMLOTE':NUMLOTE,
				'FECHACIERRE':FECHACIERRE,'CODPLAN':CODPLAN,'CODRESPU':CODRESPU,'DATADIC':DATADIC,'MODOING':MODOING,
				'FILLER':FILLER}

				df = pd.DataFrame(data, columns =['NUMEST','TERMINAL','NUMTAR','TIPOMOV','FECHA','HORA','NCUPON',
				'MONEDA','IMPORTE','CUOTAS','NROAUT','DIASDIFER','ESTRUBRO','ESTDENOM','CODOP','FECHADIFER','NUMLOTE'
				,'FECHACIERRE','CODPLAN','CODRESPU','DATADIC','MODOING','FILLER'])

				df.to_csv('CSV_MKPRIV.CSV', sep=';')



				return listaCompleta

			else:
				return 10 #Si no es un Header devuelvo un 10 para regresar una Excepción


		except(Exception,ValueError):
			print("Formato Erroneo de archivo 1234")
			return 10

	