
from Lista import ListaSimpleEnlazada

class ruta():

    def __init__(self):
        pass

    def aguardar(self, DX, DY, PIX, PIY, PFX, PFY, cor):

        nuevalista = ListaSimpleEnlazada()

        nuevalista.agregar_ultimo(cor)
        # a=nuevalista.recorrido()

        a= nuevalista.buscar(3,1)
        
        aux = 0
        for i in str(a):
            
            
            
            if aux == DX:
                print(i , end= " ")
                print("ssssss \n \n \n \n ")
                aux =0
            aux = aux+1 




            






        
        
       