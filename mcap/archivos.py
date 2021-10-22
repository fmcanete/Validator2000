from time import sleep
import time, re, os, csv 
import pandas as pd

class manejoDeLosArchivosTXT():
	

	def abrirArchivo(mov2000Plano,ruta):
		try:
			mov2000Plano = open(ruta, "r",encoding = 'cp850')
			#open("MOV2000.txt", "r")
			return mov2000Plano
		except Exception:
			return 10	#se devuelve un valor 10 entero arbitrariamente para evaluar excepciones posteriores

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
		except (MemoryError):
			return 11,11	#aca se queda sin memoria y no puede seguir procesando
		except (UnicodeDecodeError,TypeError,Exception):
			return 10,10 #aca se queda sin memoria y no puede seguir procesando
			
	def subStringLista(listaArchivo, contadorArchivo, listaCompleta):
		try:
			cont = 1
			numTarMovMes = []
			establecimiento = []
			nroAut =[]
			planCuot =[]
			numCuot =[]
			cuotas = []
			AjusteCuota1STD =[]
			moneda = []
			importe = []
			codPais = []
			importeOrig = []
			binBancoPagador = []
			nombreComercio = []
			TjCodBanco = []
			numTarMov2000 = []
			planGob = []
			token = []
			numToken = []
			posDataCode = []
			visaRelease = []
			tipoTarjeta = []	#campo indTerm
			campoBCRA =[]
			diasPago = []
			saltoLinea = []
			aux = listaArchivo[0]

			if aux[0] == 'H':	#Si la primera transacción no es un Header no lo leo.
				
				while listaArchivo[cont] != "":
					cadena = listaArchivo[cont]
					cont = cont+1
					if cadena[0] == "D":
						numTarMovMes.append(cadena[35:51])
						establecimiento.append(cadena[51:61])
						nroAut.append(cadena[111:119])
						planCuot.append(cadena[127:129])
						numCuot.append(cadena[129:131])
						cuotas.append(cadena[263:265])
						AjusteCuota1STD.append(cadena[198:201])
						moneda.append(cadena[131:134])
						importe.append(str(float(cadena[134:149])/100))
						codPais.append(cadena[153:155])
						importeOrig.append(cadena[156:170])
						binBancoPagador.append(cadena[171:177])
						nombreComercio.append(cadena[321:342])
						TjCodBanco.append(cadena[396:399])
						numTarMov2000.append(cadena[439:458])
						planGob.append(cadena[592])
						token.append(cadena[535])
						numToken.append(cadena[536:552])
						posDataCode.append(cadena[781:794])
						visaRelease.append(cadena[1059])
						tipoTarjeta.append(cadena[318])
						campoBCRA.append(cadena[682:684])
						diasPago.append(cadena[517:519])
						saltoLinea.append(cadena[1053])
						

					pass
				pass
				
				data = {'numTarMovMes': numTarMovMes, 'establecimiento':establecimiento, 'nroAut': nroAut, 'planCuot': planCuot,
						'numCuot': numCuot,'cuotas':cuotas,'AjusteCuota1STD':AjusteCuota1STD, 'moneda': moneda, 'importe': importe, 'codPais': codPais, 'importeOrig': importeOrig, 'binBancoPagador':binBancoPagador,
						'nombreComercio': nombreComercio, 'TjCodBanco': TjCodBanco, 'numTarMov2000': numTarMov2000, 'planGob':planGob,'token':token,'numToken':numToken,
						'posDataCode':posDataCode, 'visaRelease':visaRelease, 'tipoTarjeta': tipoTarjeta,'campoBCRA':campoBCRA,'diasPago':diasPago}
				df = pd.DataFrame(data, columns = ['numTarMovMes', 'establecimiento', 'nroAut','planCuot','numCuot','cuotas' ,'AjusteCuota1STD','moneda',
						'importe', 'codPais','importeOrig', 'binBancoPagador', 'nombreComercio', 'TjCodBanco',
						'numTarMov2000','planGob', 'token', 'numToken', 'posDataCode', 'visaRelease','tipoTarjeta','campoBCRA','diasPago'])


				df.to_csv('CSV_MOV2000.CSV', sep=';')


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
				
				#Metodo de Ejemplo, se coloca la lista del campo, el archivo del log, campo, Mensaje, listaArchivo y la posición inicial/final del campo

				#MetodoContador(TjCodBanco,logContador,'998','Tipo Emision no Prisma: ',listaArchivo,396,399)
				MetodoContador(TjCodBanco,logContador,'998','Tipo Emision no Prisma: ',listaArchivo,0,0)
				MetodoContador(planGob,logContador,'7','Plan Gobierno: ',listaArchivo,0,0)
				MetodoContador(token,logContador,'S','Tokenizada: ',listaArchivo,0,0) 
				MetodoContador(visaRelease,logContador,'V','Visa Release: ',listaArchivo,0,0)
				MetodoContador(visaRelease,logContador,'U1','Campo BCRA UPI: ',listaArchivo,0,0)
				
				logContador.close()


				return listaCompleta

			else:
				return 10 #Si no es un Header devuelvo un 10 para regresar una Excepción


		except(Exception,ValueError):
			print("Formato Erroneo de archivo 1234")
			return 10

	def subStringListaCasos(listaArchivo, contadorArchivo, listaCompleta):
			try:
				cont = 0
				cont1 = 0
				numTarMovMes = []
				establecimiento = []
				nroAut =[]
				planCuot =[]
				numCuot =[]
				cuotas = []
				AjusteCuota1STD= []
				moneda = []
				importe = []
				codPais = []
				importeOrig = []
				binBancoPagador = []
				nombreComercio = []
				TjCodBanco = []
				numTarMov2000 = []
				planGob = []
				token = []
				numToken = []
				posDataCode = []
				visaRelease = []
				tipoTarjeta = []	#campo indTerm
				campoBCRA =[]
				saltoLinea = []
				diasPago = []
				aux = listaArchivo[0]
				listaArchivoCasos = []

				if aux[0] == 'H':	#Si la primera transacción no es un Header no lo leo.

					def MetodoLogTransaccion(loggeador,posicion,contador,lista,nombre):
							loggeador.write(str(Posiciones)+" "+ nombre)
							loggeador.write('\n')
							loggeador.write(lista[contador])
							loggeador.write('\n')	

					logContador = open('logContadorCasos.txt', "w")
					logContador.write('Posición CSV:')
					logContador.write('\n')  
					listaArchivoCasos.append(aux[0])
					Posiciones = 0
					MarcaEmisionPG = 0
					MarcaEmisionSinPG = 0
					MarcaEmisionCuotaACuota = 0
					MarcaplanGob = 0
					MarcaEmisionNPDebito = 0
					MarcaTokenCredito = 0
					MarcaTokenDebito = 0
					MarcaDebito = 0
					MarcaCuotas =0
					MarcaCuotasAce =0
					MarcaCuotasAceSinCuot=0
					MarcaplanGobAceCuota=0
					MarcaplanInternacional =0
					MarcaPropina = 0

					while listaArchivo[cont1] !="":

						cadena2 = listaArchivo[cont1]
						cont2 = 0

						if cadena2[0] == "D":
							#Credito Emision No Prisma Cuotas Plan Gobierno
							if cadena2[396:399] == '998' and cadena2[316] == '8'and cadena2[670] == 'N' and cadena2[593:596] == '900' and cadena2[592] == '7' and cadena2[263:265] != '  ' and cadena2[263:265] != '00' and cadena2[318] == '1'and MarcaEmisionPG == 0:
								MarcaEmisionPG = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Credito - Emision NO Prisma - Cuotas Plan Gobierno')	
							
							#Credito Emision No Prisma Cuotas sin Plan Gobierno
							if cadena2[396:399] == '998' and cadena2[316] == '8'and cadena2[670] == 'N' and cadena2[593:596] == '900' and cadena2[592] != '7' and cadena2[263:265] != '  ' and cadena2[263:265] != '00' and cadena2[318] == '1' and MarcaEmisionSinPG == 0:
								MarcaEmisionSinPG = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Credito - Emision NO Prisma - Cuotas sin Plan Gobierno')	
							
							#Credito Emision No Prisma Cuota a Cuota
							if cadena2[396:399] == '998' and cadena2[316] == '8'and cadena2[670] == 'N' and cadena2[593:596] == '900' and cadena2[592] != '7' and cadena2[263:265] != '  ' and cadena2[263:265] != '00' and MarcaEmisionCuotaACuota == 0 and cadena2[127:129] != '00' and cadena2[129:131] == '01'and cadena2[198:201] == 'STD' and cadena2[318] == '1':
								MarcaEmisionCuotaACuota = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Credito - Emision NO Prisma - Cuota a Cuota')													

							#Debito Emision No Prisma
							if cadena2[396:399] == '998' and cadena2[316] == '8'and cadena2[670] == 'N' and cadena2[593:596] == '900'  and cadena2[318] == 'E'and MarcaEmisionNPDebito == 0:
								MarcaEmisionNPDebito = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Debito - Emision NO Prisma')	

							#Tokenizada Debito
							if cadena2[535] == 'S' and MarcaTokenDebito == 0 and cadena2[318] == 'E' and cadena2[536] != ' ':
								MarcaTokenDebito = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Debito - Tokenización')	

							#Tokenizada Credito
							if cadena2[535] == 'S' and MarcaTokenCredito == 0 and cadena2[318] == '1' and cadena2[536] != ' ':
								MarcaTokenCredito = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Credito - Tokenización')												
							
							#Debito Online
							if cadena2[318] == 'E' and MarcaDebito == 0:
								MarcaDebito = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Debito Online')

							#Cuota a Cuota Online Emisión Prisma
							if cadena2[127:129] != '00' and cadena2[129:131] == '01'and cadena2[198:201] == 'STD' and MarcaCuotas == 0 and cadena2[396:399] != '998':
								MarcaCuotas = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Credito - Emisión Prisma - Cuota a Cuota Online')

							#Cuota Acelerado en Cuotas
							if cadena2[592] != '7' and cadena2[263:265] != '  ' and cadena2[263:265] != '00' and MarcaCuotasAce == 0 and cadena2[318] == '1':
								MarcaCuotasAce = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Credito - Emisión Prisma  - Acelerado en Cuotas')	
							
							#Acelerado sin Cuotas
							if cadena2[263:265] == '  ' and cadena2[263:265] != '00' and MarcaCuotasAceSinCuot == 0 and cadena2[318] == '1':
								MarcaCuotasAceSinCuot = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Credito - Acelerado sin Cuotas')	

							#Plan Gobierno + Plan Acelerado en Cuotas
							if cadena2[592] == '7' and MarcaplanGobAceCuota == 0 and cadena2[263:265] != '  ' and cadena2[263:265] != '00' and cadena2[318] == '1':
								MarcaplanGobAceCuota = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Credito - Plan Gobierno Acelerado en Cuotas')
							
							#Internacional (Validar si hay internacionales en cuotas)
							if MarcaplanInternacional == 0 and cadena2[396:399] == '999' and cadena2[316] == '4' and cadena2[318] == '1':
								MarcaplanInternacional = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Credito - Transaccion Internacional')		
							
							#Propina (Validar si hay internacionales en cuotas)
							if MarcaPropina == 0 and cadena2[887] == 'P':
								MarcaPropina = 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Marca Propina')
								cont1 = cont1 + 1
								listaArchivoCasos.append(listaArchivo[cont1])
								Posiciones=Posiciones+1
								MetodoLogTransaccion(logContador,Posiciones,cont1,listaArchivo,'Marca Consumo')															

						cont1 = cont1 + 1
					
					listaArchivoCasos.append("")

					while listaArchivoCasos[cont] != "":
						cadena = listaArchivoCasos[cont]
						cont = cont+1
						if cadena[0] == "D":
							numTarMovMes.append(cadena[35:51])
							establecimiento.append(cadena[51:61])
							nroAut.append(cadena[111:119])
							planCuot.append(cadena[127:129])
							numCuot.append(cadena[129:131])
							cuotas.append(cadena[263:265])
							AjusteCuota1STD.append(cadena[198:201])
							moneda.append(cadena[131:134])
							importe.append(str(float(cadena[134:149])/100))
							codPais.append(cadena[153:155])
							importeOrig.append(cadena[156:170])
							binBancoPagador.append(cadena[171:177])
							nombreComercio.append(cadena[321:342])
							TjCodBanco.append(cadena[396:399])
							numTarMov2000.append(cadena[439:456])
							planGob.append(cadena[592])
							token.append(cadena[535])
							numToken.append(cadena[536:552])
							posDataCode.append(cadena[781:794])
							visaRelease.append(cadena[1059])
							tipoTarjeta.append(cadena[318])
							campoBCRA.append(cadena[682:684])
							diasPago.append(cadena[517:519])
							saltoLinea.append(cadena[1053])
							

						pass
					pass
					
					data = {'numTarMovMes': numTarMovMes, 'establecimiento':establecimiento, 'nroAut': nroAut, 'planCuot': planCuot,
							'numCuot': numCuot,'cuotas': cuotas,'AjusteCuota1STD':AjusteCuota1STD, 'moneda': moneda, 'importe': importe, 'codPais': codPais, 'importeOrig': importeOrig, 'binBancoPagador':binBancoPagador,
							'nombreComercio': nombreComercio, 'TjCodBanco': TjCodBanco, 'numTarMov2000': numTarMov2000, 'planGob':planGob,'token':token,'numToken':numToken,
							'posDataCode':posDataCode, 'visaRelease':visaRelease, 'tipoTarjeta': tipoTarjeta,'campoBCRA':campoBCRA,'diasPago':diasPago}
					df = pd.DataFrame(data, columns = ['numTarMovMes', 'establecimiento', 'nroAut','planCuot','numCuot','cuotas','AjusteCuota1STD', 'moneda',
							'importe', 'codPais','importeOrig', 'binBancoPagador', 'nombreComercio', 'TjCodBanco',
							'numTarMov2000','planGob', 'token', 'numToken', 'posDataCode', 'visaRelease','tipoTarjeta','campoBCRA','diasPago'])

				
					df.to_csv('CSV_MOV2000.csv', sep=';')





					logContador.write('\n') 
					
					
					logContador.close()



					return listaCompleta

				else:

					return 10 #Si no es un Header devuelvo un 10 para regresar una Excepción

			except(Exception,ValueError):
				print("Formato Erroneo de archivo")
				return 10

