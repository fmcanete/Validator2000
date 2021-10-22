INSERT INTO mov2000_camposBasicos (numTarMovMes, establecimiento, nroAut, planCuot, numCuot,  		
cuotas, AjusteCuota1STD, moneda, importe, codPais, importeOrig, binBancoPagador, nombreComercio, TjCodBanco, 
numTarMov2000, planGob, token, numToken, posDataCode, visaRelease, tipoTarjeta, campoBCRA, diasPago)
SELECT SUBSTRING(Info,36,16),SUBSTRING(Info,52,10),SUBSTRING(Info,112,8),SUBSTRING(Info,128,2),
SUBSTRING(Info,130,2),SUBSTRING(Info,264,2),SUBSTRING(Info,199,3),SUBSTRING(Info,132,3), 
cast (SUBSTRING (Info,135,15) as float), SUBSTRING(Info,154,2), cast (SUBSTRING (Info,157,14) as float),
SUBSTRING(Info,172,6),SUBSTRING(Info,322,21),SUBSTRING(Info,397,3),
SUBSTRING(Info,440,19),SUBSTRING(Info,593,1),SUBSTRING(Info,536,1),SUBSTRING(Info,537,14),SUBSTRING(Info,782,13),
SUBSTRING(Info,1060,1),SUBSTRING(Info,319,1),SUBSTRING(Info,683,2),SUBSTRING(Info,518,2)
FROM MOV2000_V1
WHERE  substring (info, 1,1) = 'D'