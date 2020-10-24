#Se dejan los métodos a utilizar en todo el programa


def LecturaMov2000(lista_datos_mov2000,rutaArchivo):  #Le paso una lista y la ruta del archivo como parámetro
    		Archivo = open(rutaArchivo,'r')  #Abro el archivo para solo lectura       
    		lista_datos_mov2000 = [0]        #Inicializo la lista
    		dato = Archivo.readline()        #Guardamos la primera linea del MOV2000 en dato
    		cont = int(0)
    		lista_datos_mov2000 = [dato]     #Se guarda (dato) en la lista que es la primera linea 
    		while dato != '':
        			dato = Archivo.readline()
        			lista_datos_mov2000.append(dato)        #Se va leyendo cada linea y se guarda en la lista cada linea
        			cont = cont + 1
        
    		Archivo.close()
    		return lista_datos_mov2000

