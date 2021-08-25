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
			cont = 0
			Codsis      = []
			Codtar      = []
			Codadm      = []
			Codbco      = []
			CodSuc      = []
			Filler1     = []
			Codop       = []
			Fproc       = []
			Numtar      = []
			Numest      = []
			Filler3     = []
			DIAORIG     = []
			MESORIG     = []
			AnioOrig    = []
			NumAut      = []
			NroCupon    = []
			PlnCuo      = []
			Numcuot     = []
			Moneda      = []
			Importe     = []
			Filler5     = []
			Codpais     = []
			Filler6     = []
			CodRechazo  = []
			Filler7     = []
			NroCaja     = []
			Filler9     = []
			MsgRechazo  = []
			Filler2     = []
			Codbco2     = []
			CodSuc2     = []
			MovComis    = []
			Filler8     = []
			FinReg      = []
			

			aux = listaArchivo[0]

			#################

			if aux[0] == '0':	#Si la primera transacción no es un Header no lo leo.
				
				while listaArchivo[cont] != "":
					cadena = listaArchivo[cont]
					cont = cont+1
					if cadena[0] == "0":
						Codsis.append(str(cadena[0:3])) 
						Codtar.append(cadena[3:6]) 
						Codadm.append(cadena[6:9]) 
						Codbco.append(cadena[9:12]) 
						CodSuc.append(cadena[12:15]) 
						Filler1.append(cadena[15:24]) 
						Codop.append(cadena[24:28]) 
						Fproc.append(cadena[28:34]) 
						Numtar.append(cadena[34:50]) 
						Numest.append(cadena[50:60]) 
						Filler3.append(cadena[60:104]) 
						DIAORIG.append(cadena[104:106]) 
						MESORIG.append(cadena[106:108]) 
						AnioOrig.append(cadena[108:110]) 
						NumAut.append(cadena[110:118]) 
						NroCupon.append(cadena[118:126]) 
						PlnCuo.append(cadena[126:128]) 
						Numcuot.append(cadena[128:130]) 
						Moneda.append(cadena[130:133]) 
						Importe.append(cadena[133:148]) 
						Filler5.append(cadena[148:152]) 
						Codpais.append(cadena[152:154]) 
						Filler6.append(cadena[154:162]) 
						CodRechazo.append(cadena[162:165]) 
						Filler7.append(cadena[165:194]) 
						NroCaja.append(cadena[194:198]) 
						Filler9.append(cadena[198:282]) 
						MsgRechazo.append(cadena[282:357])   
						Filler2.append(cadena[357:363]) 
						Codbco2.append(cadena[363:366]) 
						CodSuc2.append(cadena[366:369]) 
						MovComis.append(cadena[369:374]) 
						Filler8.append(cadena[374:650]) 
						FinReg.append(cadena[650:652]) 
    


						########################

					pass
				pass
				
				data = {'Codsis':Codsis,'Codtar':Codtar,'Codadm':Codadm,'Codbco':Codbco,'CodSuc':CodSuc,
				'Filler1':Filler1,'Codop':Codop,'Fproc':Fproc,'Numtar':Numtar,'Numest':Numest,
				'Filler3':Filler3,'DIAORIG':DIAORIG,'MESORIG':MESORIG,'AnioOrig':AnioOrig,
				'NumAut':NumAut,'NroCupon':NroCupon,'PlnCuo':PlnCuo,'Numcuot':Numcuot,
				'Moneda':Moneda,'Importe':Importe,'Filler5':Filler5,'Codpais':Codpais,
				'Filler6':Filler6,'CodRechazo':CodRechazo,'Filler7':Filler7,'NroCaja':NroCaja,
				'Filler9':Filler9,'MsgRechazo':MsgRechazo,'Filler2':Filler2,'Codbco2':Codbco2,
				'CodSuc2':CodSuc2,'MovComis':MovComis,'Filler8':Filler8,'FinReg':FinReg} 

				df = pd.DataFrame(data, columns =['Codsis','Codtar','Codadm','Codbco','CodSuc'
				,'Filler1','Codop','Fproc','Numtar','Numest'
				,'Filler3','DIAORIG','MESORIG','AnioOrig','NumAut'
				,'NroCupon','PlnCuo','Numcuot','Moneda','Importe'
				,'Filler5','Codpais','Filler6','CodRechazo','Filler7'
				,'NroCaja','Filler9','MsgRechazo','Filler2'
				,'Codbco2','CodSuc2','MovComis','Filler8','FinReg'])

				df.to_csv('CSV_MOVRECHAZOS.CSV', sep=';')



				return listaCompleta

			else:
				return 10 #Si no es un Header devuelvo un 10 para regresar una Excepción


		except(Exception,ValueError):
			print("Formato Erroneo de archivo 1234")
			return 10

	