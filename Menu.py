import cargarArchivo
from procesar import procesar
from Lista  import ListaSimpleEnlazada

def Menu():

    while True:
        opcion = int(input('Menu Principal \n 1. Cargar Archivo \n 2. Procesar Archivo \n 3. Escribir Archivo Salida \n 4. Mostrar Datos del Estudiante \n 5. Generar Grafica \n 6. Salir \n '  ))
        if opcion ==1: 
            ruta = cargarArchivo.ruta(self=None) 
            #quitar de ultimo
        elif opcion == 2:
            proceso1 = procesar(ruta)

            proceso1.leerXML()

            
            

            continue
        elif opcion == 3:
            continue
        elif opcion == 4:
            continue
        elif opcion ==5:
            continue
        elif opcion == 6:
            print("Ha cerrado la apliacion")
            break
        else:
            print('**ERROR**  Digitar numero correcto en el rango de 1 a 6')