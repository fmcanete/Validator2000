# Validator2000

En esta versíón se logra parsear aquellos campos basicos del MOV2000:
numTarMovMes,establecimiento,nroAut,planCuot,numCuot,moneda,importe,codPais,importeOrig,binTarj,
nombreComercio,bancoEstablecimiento,numTarMov2000,Token,numToken,posDataCode,visaRelease

Además de parsearlos a raiz del TXT, se logra dejar disponibilizado en el directorio del proyecto un archivo de salida CSV tabulado por ','.


UPDATE 12/11/20
Se corrigió el método: recorrerArchivoMov2000
se agregó que al final de llenar todas las trx, agruege un salto de linea.

Se probó con otro MOV2000 y funcionó.