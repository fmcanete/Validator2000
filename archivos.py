from time import sleep
import time, re, os, csv
import pandas as pd



class manejoDeLosArchivosTXT():

	def abrirArchivo(mov2000Plano,ruta):
		try:
			mov2000Plano = open(ruta, "r")
			#open("MOV2000.txt", "r")
			return mov2000Plano
		except Exception:
			return 10

	def cerrarArchivo(mov2000Plano):
		mov2000Plano.close()

	def recorrerArchivoMov2000(mov2000Plano, listaArchivo, contadorArchivo):	#ESTE METODO RECORRE EL ARCHIVO Y GUARDA LA LISTA CON LOS VALORES
		try:
			contadorArchivo = 0
			listaArchivo = []
			for linea in mov2000Plano:				#Se modifica el for, se guarda toda la trama incluyendo saltos de linea
				listaArchivo.append(linea)
				contadorArchivo = contadorArchivo + 1
			
			listaArchivo.append("")					#Se le agrega un espacio vacío a la lista para el WHILE siguiente del parseo
			
			return listaArchivo, contadorArchivo
		except (UnicodeDecodeError,Exception,TypeError):
			return 10,10
			

	def subStringLista(listaArchivo, contadorArchivo, listaCompleta):
		try:
			cont = 1
			numTarMovMes = []
			establecimiento = []
			nroAut =[]
			planCuot =[]
			numCuot =[]
			moneda = []
			importe = []
			codPais = []
			importeOrig = []
			binTarj = []
			nombreComercio = []
			TjCodBanco = []
			numTarMov2000 = []
			planGob = []
			token = []
			numToken = []
			posDataCode = []
			visaRelease = []
			tipoTarjeta = []	#campo indTerm
			saltoLinea = []
			while listaArchivo[cont] != "":
				cadena = listaArchivo[cont]
				cont = cont+1
				if cadena[0] == "D":
					numTarMovMes.append(cadena[35:51])
					establecimiento.append(cadena[51:61])
					nroAut.append(cadena[111:119])
					planCuot.append(cadena[127:129])
					numCuot.append(cadena[129:131])
					moneda.append(cadena[131:134])
					importe.append(str(float(cadena[134:149])/100))
					codPais.append(cadena[153:155])
					importeOrig.append(cadena[156:170])
					binTarj.append(cadena[171:177])
					nombreComercio.append(cadena[321:342])
					TjCodBanco.append(cadena[396:399])
					numTarMov2000.append(cadena[439:456])
					planGob.append(cadena[592])
					token.append(cadena[535])
					numToken.append(cadena[536:552])
					posDataCode.append(cadena[781:794])
					visaRelease.append(cadena[1059])
					tipoTarjeta.append(cadena[318])
					saltoLinea.append(cadena[1053])
					

				pass
			pass
			
			data = {'numTarMovMes': numTarMovMes, 'establecimiento':establecimiento, 'nroAut': nroAut, 'planCuot': planCuot,
					'numCuot': numCuot, 'moneda': moneda, 'importe': importe, 'codPais': codPais, 'importeOrig': importeOrig, 'binTarj':binTarj,
					'nombreComercio': nombreComercio, 'TjCodBanco': TjCodBanco, 'numTarMov2000': numTarMov2000, 'planGob':planGob,'token':token,'numToken':numToken,
					'posDataCode':posDataCode, 'visaRelease':visaRelease, 'tipoTarjeta': tipoTarjeta}
			df = pd.DataFrame(data, columns = ['numTarMovMes', 'establecimiento', 'nroAut','planCuot','numCuot', 'moneda',
					'importe', 'codPais','importeOrig', 'binTarj', 'nombreComercio', 'TjCodBanco',
					'numTarMov2000','planGob', 'token', 'numToken', 'posDataCode', 'visaRelease','tipoTarjeta'])

		
			df.to_csv('CSV_MOV2000.csv', sep=';')


			#################################
			#CONTADOR DE TRX X FUNCIONALIDAD#
			#################################

			def MetodoContador (listaCampo,archivo,Marca,texto,listaTotal,posIni,posFin):
				i=0
				j=0
				cantidad = listaCampo.count(Marca)
				archivo.write(texto + str(cantidad))
				archivo.write('\n')

				if posIni != 0:
				
					while i == 0 and j < len(listaTotal):
						transaccion = listaTotal[j]
						if transaccion[posIni:posFin] == Marca:
							archivo.write('Transaccion Testigo: ')
							archivo.write(transaccion)
							i = 1
						j = j+1
					#print(cantidad)


			logContador = open('logContador.txt', "w") 
			logContador.write('Total de transacciones: ' + str(len(numTarMovMes))) 
			logContador.write('\n') 
			MetodoContador(tipoTarjeta,logContador,'E','Tipo Debito: ',listaArchivo,0,0) 
			MetodoContador(tipoTarjeta,logContador,'1','Tipo Credito: ',listaArchivo,0,0) 
			
			logContador.write('\n') 
			logContador.write('Desglosados en: ') 
			logContador.write('\n') 
			
			MetodoContador(TjCodBanco,logContador,'998','Tipo Emision no Prisma: ',listaArchivo,396,399)
			MetodoContador(planGob,logContador,'7','Plan Gobierno: ',listaArchivo,592,593)
			MetodoContador(token,logContador,'S','Tokenizada: ',listaArchivo,0,0) 
			MetodoContador(visaRelease,logContador,'V','Visa Release: ',listaArchivo,1059,1060)
			
			logContador.close()



			return listaCompleta

		except(Exception,ValueError):
			print("Formato Erroneo de archivo")
			return 10