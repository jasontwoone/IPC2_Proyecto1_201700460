from functools import partialmethod
from typing import Collection
from xml.dom import minidom

from ruta import ruta
from coordenada import coordenada
from Lista  import ListaSimpleEnlazada



class procesar:
    
    def __init__(self, ruta):
        self.ruta =ruta
        

    def leerXML(self):

        xml = minidom.parse(self.ruta)
        procesar.mostrar_terrenos(self)

    def mostrar_terrenos(self):
        xml = minidom.parse(self.ruta)
        #obtener el nombre de los terrenos
        terrenosw = xml.getElementsByTagName("terreno")
        # procesar.nombreTerrenos(datos)
       
        print("\033[;36m"+"------------------------------ \n**** PROCESAR ARCHIVO **** \n------------------------------\n")
        print("\033[1;33m"+"Listado de terrenos disponibles:\n"+'\033[0;m')
        
        aux = 1

        for terrenos in terrenosw:
            # terreno = terrenos.getElementsByTagName("terreno")[0]
            nombre= terrenos.getAttribute("nombre")
            print(  aux,". " , nombre )
            aux +=1
            # print(terreno.firstChild.data)
            
        opcion = input("--> Escriba el nombre del terreno que desea procesar:  \n-->  ")

        procesar.indentificar_terreno(self, opcion)
        
  
    
    def indentificar_terreno(self, opcion):
        xml = minidom.parse(self.ruta)

        terrenos = xml.getElementsByTagName("terreno")
        dimensiones = xml.getElementsByTagName("dimension")
        pos_inicio = xml.getElementsByTagName("posicioninicio")     
        pos_final = xml.getElementsByTagName("posicionfin")  
        posicion = xml.getElementsByTagName("posicion")
        te = xml.getElementsByTagName("terreno")[0].childNodes
        x = xml.getElementsByTagName('posicion')[2].attributes
      

        aux = 0
        contador =0 
        for terreno in terrenos:
            d = terreno.getAttribute("nombre")

           
            if d == opcion: 
                
                dir = dimensiones[aux]
                posINI = pos_inicio[aux]
                posFIN = pos_final[aux]
                
                n = dir.getElementsByTagName("n")[0]
                m = dir.getElementsByTagName("m")[0]

                XI = posINI.getElementsByTagName("x")[0]
                YI = posINI.getElementsByTagName("y")[0]

                XF = posFIN.getElementsByTagName("x")[0]
                YF = posFIN.getElementsByTagName("y")[0]

                print(f" {d} \n n = {n.firstChild.data} | m: = {m.firstChild.data} ")    
                print(f" Posicion Inicial X: = {XI.firstChild.data} | Y: = {YI.firstChild.data} ")     
                print(f" Posicion Final   X: = {XF.firstChild.data} | Y: = {YF.firstChild.data} ")      
         
         
                #iteracion de for
                a = int(n.firstChild.data)*int(m.firstChild.data)
                print(a)
                aux2 = 0
                b =contador+a
                
                for pos in range(contador, b):

                    poscor = posicion[contador]

                    
                    x = poscor.getAttribute("x")
                    y= poscor.getAttribute("y")
                    
                    # print(int(x) , " ", int(y), " ", int(poscor.firstChild.data))

                    a = int(x)
                    b= (int(y))
                    combustible = int(poscor.firstChild.data)

                    cor = coordenada(a,b,combustible)

                    # cor.mostrar()

                    rutas = ruta()

                    DX=int(n.firstChild.data)
                    DY = int(m.firstChild.data)
                    PIX = int(XI.firstChild.data)
                    PIY = int(YI.firstChild.data)
                    PFX = int(XF.firstChild.data)
                    PFY = int(YF.firstChild.data)

                    rutas.aguardar(DX,DY,PIX,PIY,PFX,PFY,cor)
                    
                    
                    

                    

                    



                   

                    
                    
                    contador +=1


                print(b)
                
                # print(posicion)
                # for xi in range(0,a):
                    
                #     txt = x.getNamedItem("x").nodeValue , x.getNamedItem("y").nodeValue , " " , x.length
                #     print(txt)
                
                # for posi in posicion  :


                #     posCor = posicion[aux2]
                    

                #     x= posCor.getAttribute("x")
                #     y= posCor.getAttribute("y")

                #     print(x , " ", y)
                #     aux2 += 1
        
            aux +=1




            
            for dimension in dimensiones:
                n = dimension.getElementsByTagName("n")[0]

                # print( n.firstChild.data )

            for dimension in dimensiones:
                n = dimension.getElementsByTagName("n")[0]
                # print(n.firstChild.data)
                if n.firstChild.data == d:
                    print("terrrrrrrrr")
                # print(d)

        
        # terrenosw = xml.getElementsByTagName("terreno")
        # aux = 1


        # terrenos = xml.getElementsByTagName("terreno")[0].childNodes[0]
       
        # for terreno in terrenos:
        #     ter = terreno.getElementsByTagName['dimension'].childNodes[0]
        #     print(ter)


        # dimensiones = xml.getElementsByTag("dimension")
        
        
        # for terreno in terrenos:
        #     ter = terreno.getAttribute("nombre")
        #     if ter == opcion:
                
        #             print()
            
        



            # a = terreno.getElementsByTagName("n")

            # print(a.firstChild.data)
            
            # if terreno.getAttribute("nombre") == opcion:
            #     for dimension in dimensiones:
            #         if terreno.getAttribute("nombre") == opcion:
            #             n= dimension.getElementsByTagName("n")[0]
            #             m= dimension.getElementsByTagName("m")[0]
                  
            #             print('fila ' , n.childNodes , ' m ') 
            

        # for terrenos in terrenosw:
        #     nombre= terrenos.getAttribute("nombre")
        #     if nombre == opcion:
        #         print('se procesara: ' , nombre)
                
                
        #         dimensiones = xml.getElementsByTagName("dimension")

        #         print(dimensiones)
                
        #         for dimension in dimensiones:
        #             fila = dimension.getElementsByTagName("n")[0]
        #             columana = dimension.getElementsByTagName("m")[0]

        #             print(f"fila={fila.firstChild.data} | columna={columana.firstChild.data}")
                    
        #             break 


        #     else: continue


    def letura_terreno_indicado(self):
        
        pass


        