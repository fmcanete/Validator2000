from time import sleep
import time
import re
import os
import csv
import pandas as pd


class manejoDeLosArchivosTXT():

	def abrirArchivo(MEMOVPlano, ruta):
		try:
			MEMOVPlano = open(ruta, "r", encoding='cp850')

			return MEMOVPlano
		except Exception:
			return 10  # se devuelve un valor 10 entero arbitrariamente para evaluar excepciones posteriores

	def cerrarArchivo(MEMOVPlano):
		MEMOVPlano.close()

	# ESTE METODO RECORRE EL ARCHIVO Y GUARDA LA LISTA CON LOS VALORES
	def recorrerArchivoMEMOV(MEMOVPlano, listaArchivo, contadorArchivo):
		try:
			contadorArchivo = 0
			listaArchivo = []
			for linea in MEMOVPlano:  # Se modifica el for, se guarda toda la trama incluyendo saltos de linea
				listaArchivo.append(linea)
				contadorArchivo = contadorArchivo + 1

			# Se le agrega un espacio vacío a la lista para el WHILE siguiente del parseo
			listaArchivo.append("")

			return listaArchivo, contadorArchivo
		except (MemoryError):
			return 11, 11  # aca se queda sin memoria y no puede seguir procesando
		except (UnicodeDecodeError, TypeError, Exception):
			return 10, 10  # aca se queda sin memoria y no puede seguir procesando

	def subStringLista(listaArchivo, contadorArchivo, listaCompleta):
		try:
			cont = 0
			Codsis = []
			Codtar = []
			Codadm = []
			Codbco = []
			Codcasa = []
			Cartera = []
			FPag = []
			Origen = []
			Codop = []
			FProc = []
			Numtar = []
			Numest = []
			Numusu = []
			NumCom = []
			Rescomp = []
			Feproc = []
			DiaPres = []
			MesPres = []
			AnioPres = []
			Ciclo = []
			DIAORIG = []
			MESORIG = []
			AnioOrig = []
			NumAut = []
			Numcomp = []
			Plancuot = []
			Numcuot = []
			Moneda = []
			Importe = []
			Monorig = []
			Nropos = []
			Codpais = []
			Imporig = []
			bin = []
			MicroFilm = []
			Marcaliqusu = []
			Paiscinta = []
			Codraz = []
			AjusteCuota1STD = []
			Respdifer = []
			NroCaja = []
			TipocontIVA = []
			Filler1 = []
			Aranemi = []
			Aranpag = []
			Fcobusu = []
			Binpagint = []
			Aranadm = []
			Liqest = []
			Pagest = []
			Rubvisa = []
			Estado = []
			Regionest = []
			Codadmdest = []
			Importeusuario        = []
			TNAcuotbco            = []
			ModulosBAPRO          = []
			Mcaliqusu             = []
			Dbautomat             = []
			McaIVA                = []
			AnioCero              = []
			AnioValor             = []
			MesValor              = []
			DiaValor              = []
			MotivoDifer           = []
			FpagBAPRO             = []
			Comisteorica          = []
			Mcatartrf             = []
			Marcaint              = []
			Indremb               = []
			indterm               = []
			Millaje               = []
			Atribrem              = []
			Msgtexto              = []
			Martarpro             = []
			Bcodest               = []
			Casadest              = []
			Bcoest                = []
			Casaest               = []
			Comis                 = []
			Mcapresenta           = []
			Cinta                 = []
			Fgenci                = []
			Finten                = []
			Hinten                = []
			Atm                   = []
			Sergrab               = []
			Filler2               = []
			TID                   = []
			Filler3               = []
			ModoEntrada           = []
			Filler4               = []
			MovBanderaEst         = []
			MovAdminADQ           = []
			MovAdminEMI           = []
			MovPosicIVA           = []
			MovAplicProcT300      = []
			MovAplicProcAC        = []
			MovAplicProcRA        = []
			Filler5               = []
			FinReg                = []

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
						Codcasa.append(cadena[12:15]) 
						Cartera.append(cadena[15:17]) 
						FPag.append(cadena[17:23]) 
						Origen.append(cadena[23:24]) 
						Codop.append(cadena[24:28]) 
						FProc.append(cadena[28:34]) 
						Numtar.append(cadena[34:50]) 
						Numest.append(cadena[50:60]) 
						Numusu.append(cadena[60:70]) 
						NumCom.append(cadena[70:80]) 
						Rescomp.append(cadena[80:90]) 
						Feproc.append(cadena[90:96]) 
						DiaPres.append(cadena[96:98]) 
						MesPres.append(cadena[98:100]) 
						AnioPres.append(cadena[100:102]) 
						Ciclo.append(cadena[102:104]) 
						DIAORIG.append(cadena[104:106]) 
						MESORIG.append(cadena[106:108]) 
						AnioOrig.append(cadena[108:110]) 
						NumAut.append(cadena[110:118]) 
						Numcomp.append(cadena[118:126]) 
						Plancuot.append(cadena[126:128]) 
						Numcuot.append(cadena[128:130]) 
						Moneda.append(cadena[130:133]) 
						Importe.append(cadena[133:148]) 
						Monorig.append(cadena[148:151]) 
						Nropos.append(cadena[151:152]) 
						Codpais.append(cadena[152:154]) 
						Imporig.append(cadena[154:169]) 
						bin.append(cadena[169:175]) 
						MicroFilm.append(cadena[175:187]) 
						Marcaliqusu.append(cadena[187:188]) 
						Paiscinta.append(cadena[188:190]) 
						Codraz.append(cadena[190:194]) 
						AjusteCuota1STD.append(cadena[194:197]) 
						Respdifer.append(cadena[197:200]) 
						NroCaja.append(cadena[200:205]) 
						TipocontIVA.append(cadena[205:206]) 
						Filler1.append(cadena[206:208]) 
						Aranemi.append(cadena[208:217]) 
						Aranpag.append(cadena[217:226]) 
						Fcobusu.append(cadena[226:232]) 
						Binpagint.append(cadena[232:238]) 
						Aranadm.append(cadena[238:247]) 
						Liqest.append(cadena[247:248]) 
						Pagest.append(cadena[248:254]) 
						Rubvisa.append(cadena[254:262]) 
						Estado.append(cadena[262:264]) 
						Regionest.append(cadena[264:269]) 
						Codadmdest.append(cadena[269:272]) 
						Importeusuario.append(cadena[272:285]) 
						TNAcuotbco.append(cadena[285:290]) 
						ModulosBAPRO.append(cadena[290:291]) 
						Mcaliqusu.append(cadena[291:292]) 
						Dbautomat.append(cadena[292:293]) 
						McaIVA.append(cadena[293:294]) 
						AnioCero.append(cadena[294:295]) 
						AnioValor.append(cadena[295:297]) 
						MesValor.append(cadena[297:299]) 
						DiaValor.append(cadena[299:301]) 
						MotivoDifer.append(cadena[301:302]) 
						FpagBAPRO.append(cadena[302:309]) 
						Comisteorica.append(cadena[309:314]) 
						Mcatartrf.append(cadena[314:315]) 
						Marcaint.append(cadena[315:316]) 
						Indremb.append(cadena[316:317]) 
						indterm.append(cadena[317:318]) 
						Millaje.append(cadena[318:319]) 
						Atribrem.append(cadena[319:320]) 
						Msgtexto.append(cadena[320:394]) 
						Martarpro.append(cadena[394:395]) 
						Bcodest.append(cadena[395:398]) 
						Casadest.append(cadena[398:401]) 
						Bcoest.append(cadena[401:404]) 
						Casaest.append(cadena[404:407]) 
						Comis.append(cadena[407:412]) 
						Mcapresenta.append(cadena[412:413]) 
						Cinta.append(cadena[413:419]) 
						Fgenci.append(cadena[419:424]) 
						Finten.append(cadena[424:429]) 
						Hinten.append(cadena[429:435]) 
						Atm.append(cadena[435:436]) 
						Sergrab.append(cadena[436:438]) 
						Filler2.append(cadena[438:457]) 
						TID.append(cadena[457:472]) 
						Filler3.append(cadena[472:488]) 
						ModoEntrada.append(cadena[488:490]) 
						Filler4.append(cadena[490:582]) 
						MovBanderaEst.append(cadena[583:585]) 
						MovAdminADQ.append(cadena[585:588]) 
						MovAdminEMI.append(cadena[588:589]) 
						MovPosicIVA.append(cadena[589:590]) 
						MovAplicProcT300.append(cadena[590:591]) 
						MovAplicProcAC.append(cadena[591:592]) 
						MovAplicProcRA.append(cadena[592:596])  
						Filler5.append(cadena[596:688]) 
						FinReg.append(cadena[688:690])  
						########################
					pass
				pass
				
				data = {'Codsis':Codsis,'Codtar':Codtar,'Codadm':Codadm,'Codbco':Codbco,'Codcasa':Codcasa,
				'Cartera':Cartera,'FPag':FPag,'Origen':Origen,'Codop':Codop,'FProc':FProc,
				'Numtar':Numtar,'Numest':Numest,'Numusu':Numusu,'NumCom':NumCom,
				'Rescomp':Rescomp,'Feproc':Feproc,'DiaPres':DiaPres,'MesPres':MesPres,
				'AnioPres':AnioPres,'Ciclo':Ciclo,'DIAORIG':DIAORIG,'MESORIG':MESORIG,
				'AnioOrig':AnioOrig,'NumAut':NumAut,'Numcomp':Numcomp,'Plancuot':Plancuot,
				'Numcuot':Numcuot,'Moneda':Moneda,'Importe':Importe,'Monorig':Monorig,
				'Nropos':Nropos,'Codpais':Codpais,'Imporig':Imporig,'bin':bin,
				'MicroFilm':MicroFilm,'Marcaliqusu':Marcaliqusu,'Paiscinta':Paiscinta,'Codraz':Codraz,
				'AjusteCuota1STD':AjusteCuota1STD,'Respdifer':Respdifer,'NroCaja':NroCaja,'TipocontIVA':TipocontIVA,
				'Filler1':Filler1,'Aranemi':Aranemi,'Aranpag':Aranpag,'Fcobusu':Fcobusu,
				'Binpagint':Binpagint,'Aranadm':Aranadm,'Liqest':Liqest,'Pagest':Pagest,
				'Rubvisa':Rubvisa,'Estado':Estado,'Regionest':Regionest,'Codadmdest':Codadmdest,
				'Importeusuario':Importeusuario,'TNAcuotbco':TNAcuotbco,'ModulosBAPRO':ModulosBAPRO,'Mcaliqusu':Mcaliqusu,
				'Dbautomat':Dbautomat,'McaIVA':McaIVA,'AnioCero':AnioCero,'AnioValor':AnioValor,
				'MesValor':MesValor,'DiaValor':DiaValor,'MotivoDifer':MotivoDifer,'FpagBAPRO':FpagBAPRO,
				'Comisteorica':Comisteorica,'Mcatartrf':Mcatartrf,'Marcaint':Marcaint,'Indremb':Indremb,
				'indterm':indterm,'Millaje':Millaje,'Atribrem':Atribrem,'Msgtexto':Msgtexto,
				'Martarpro':Martarpro,'Bcodest':Bcodest,'Casadest':Casadest,'Bcoest':Bcoest,
				'Casaest':Casaest,'Comis':Comis,'Mcapresenta':Mcapresenta,'Cinta':Cinta,
				'Fgenci':Fgenci,'Finten':Finten,'Hinten':Hinten,'Atm':Atm,
				'Sergrab':Sergrab,'Filler2':Filler2,'TID':TID,'Filler3':Filler3,
				'ModoEntrada':ModoEntrada,'Filler4':Filler4,'MovBanderaEst':MovBanderaEst,'MovAdminADQ':MovAdminADQ,
				'MovAdminEMI':MovAdminEMI,'MovPosicIVA':MovPosicIVA,'MovAplicProcT300':MovAplicProcT300,'MovAplicProcAC':MovAplicProcAC,
				'MovAplicProcRA':MovAplicProcRA,'Filler5':Filler5,'FinReg':FinReg
				} 


				df = pd.DataFrame(data, columns =['Codsis','Codtar','Codadm','Codbco','Codcasa',
				'Cartera','FPag','Origen','Codop','FProc',
				'Numtar','Numest','Numusu','NumCom',
				'Rescomp','Feproc','DiaPres','MesPres',
				'AnioPres','Ciclo','DIAORIG','MESORIG',
				'AnioOrig','NumAut','Numcomp','Plancuot',
				'Numcuot','Moneda','Importe','Monorig',
				'Nropos','Codpais','Imporig','bin',
				'MicroFilm','Marcaliqusu','Paiscinta','Codraz',
				'AjusteCuota1STD','Respdifer','NroCaja','TipocontIVA',
				'Filler1','Aranemi','Aranpag','Fcobusu',
				'Binpagint','Aranadm','Liqest','Pagest',
				'Rubvisa','Estado','Regionest','Codadmdest',
				'Importeusuario','TNAcuotbco','ModulosBAPRO','Mcaliqusu',
				'Dbautomat','McaIVA','AnioCero','AnioValor',
				'MesValor','DiaValor','MotivoDifer','FpagBAPRO',
				'Comisteorica','Mcatartrf','Marcaint','Indremb',
				'indterm','Millaje','Atribrem','Msgtexto',
				'Martarpro','Bcodest','Casadest','Bcoest',
				'Casaest','Comis','Mcapresenta','Cinta',
				'Fgenci','Finten','Hinten','Atm',
				'Sergrab','Filler2','TID','Filler3',
				'ModoEntrada','Filler4','MovBanderaEst','MovAdminADQ',
				'MovAdminEMI','MovPosicIVA','MovAplicProcT300','MovAplicProcAC',
				'MovAplicProcRA','Filler5','FinReg'])

				df.to_csv('CSV_MEMOV.CSV', sep=';')



				return listaCompleta

			else:
				return 10 #Si no es un Header devuelvo un 10 para regresar una Excepción


		except(Exception,ValueError):
			print("Formato Erroneo de archivo 1234")
			return 10

	
