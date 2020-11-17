from time import sleep
import time, re, os, csv
import pandas as pd


class manejoDeLosArchivosTXT():

	def abrirArchivo(mov2000Plano):
		mov2000Plano = open(os.getcwd()+"/MOV2000.txt", "r")
		#open("MOV2000.txt", "r")
		return mov2000Plano

	def cerrarArchivo(mov2000Plano):
		mov2000Plano.close()

	def recorrerArchivoMov2000(mov2000Plano, listaArchivo, contadorArchivo):	#ESTE METODO RECORRE EL ARCHIVO Y GUARDA LA LISTA CON LOS VALORES
		contadorArchivo = 0
		listaArchivo = []
		for linea in mov2000Plano:				#Se modifica el for, se guarda toda la trama incluyendo saltos de linea
			listaArchivo.append(linea)
			contadorArchivo = contadorArchivo + 1
		
		listaArchivo.append("")					#Se le agrega un espacio vacío a la lista para el WHILE siguiente del parseo
		
		return listaArchivo, contadorArchivo

	def subStringLista(listaArchivo, contadorArchivo, listaCompleta):
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
		bancoEstablecimiento = []
		numTarMov2000 = []
		token = []
		numToken = []
		posDataCode = []
		visaRelease = []
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
				importeOrig.append(cadena[156:171])
				binTarj.append(cadena[171:177])
				nombreComercio.append(cadena[321:342])
				bancoEstablecimiento.append(cadena[396:399])
				numTarMov2000.append(cadena[440:456])
				token.append(cadena[535])
				numToken.append(cadena[536:552])
				posDataCode.append(cadena[781:794])
				visaRelease.append(cadena[1059])
				saltoLinea.append(cadena[1053])
				data = {'numTarMovMes': numTarMovMes, 'establecimiento':establecimiento, 'nroAut': nroAut, 'planCuot': planCuot,
				'numCuot': numCuot, 'moneda': moneda, 'importe': importe, 'codPais': codPais, 'importeOrig': importeOrig, 'binTarj':binTarj,
				'nombreComercio': nombreComercio, 'bancoEstablecimiento': bancoEstablecimiento, 'numTarMov2000': numTarMov2000, 'token':token,'numToken':numToken,
				'posDataCode':posDataCode, 'visaRelease':visaRelease}
				df = pd.DataFrame(data, columns = ['numTarMovMes', 'establecimiento', 'nroAut','planCuot','numCuot', 'moneda',
				'importe', 'codPais','importeOrig', 'binTarj', 'nombreComercio', 'bancoEstablecimiento',
				'numTarMov2000', 'token', 'numToken', 'posDataCode', 'visaRelease'])
			pass
		pass
		df.to_csv('CSV_MOV2000.csv', sep=';')
		return listaCompleta