from nodo import Nodo

from coordenada import coordenada

class ListaSimpleEnlazada():

    def __init__(self):
        self.primero = None
        self.ultimo = None


    def  vacia(self):
        return self.primero == None

    def agregar_ultimo(self, dato):
        if self.vacia() == True:
            self.primero = self.ultimo = Nodo(dato)

        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)


    def agregar_inicio(self, dato):
        if self.vacia()== True:
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux

    def eliminar_inicio(self):
        self.primero = self.primero.siguiente


    def eliminar_ultimo(self):
        aux = self.primero

        while aux.siguiente  != self.ultimo:
            aux = aux.siguiente
        aux.siguiente = None
        self.ultimo = aux

    def recorrido(self):
        aux = self.primero

        while aux != None:

            return  aux.dato.x , aux.dato.y , aux.dato.combustible 


            aux = aux.siguiente 

    def buscar(self, x1, y1 ):

        aux = self.primero


        while aux != None:
            
          

            return  aux.dato.combustible 
           

            aux = aux.siguiente 



