from collections import deque

class Nodo: 
    def __init__(self, dato): #almacena el valor del nodo
        self.dato = dato 
        self.izquierdo = None
        self.derecho = None

class Tree:
    def __init__(self):
        self.raiz = None #apunta al nodo raiz del arbol
    
    # def insertar(self, dato):
    #     if self.raiz is None:
    #         self.raiz = Nodo(dato)
    #     else:
    #         self._insertar_recur(dato, self.raiz)

    # def _insertar_recur(self, dato, nodo):
    #     if dato < nodo.dato:
    #         if nodo.izquierdo is None:
    #             nodo.izquierdo = Nodo(dato)
    #         else:
    #             self._insertar_recur(dato, nodo.izquierdo)
    #     else:
    #         if nodo.derecho is None:
    #             nodo.derecho = Nodo(dato)
    #         else:
    #             self._insertar_recur(dato, nodo.derecho)
                
    
    
    def combinar_arboles(self, operador, tree_iz, tree_der):
        nuevo_nodo = Nodo(operador)  #crea un nuevo nodo con el operador (Signos)
         # Enlaza los arboles del nuevo nodo
        nuevo_nodo.izquierdo = tree_iz.raiz
        nuevo_nodo.derecho = tree_der.raiz
        self.raiz = nuevo_nodo  #asigna el nuevo nodo como la raiz del arbol actual

    def construir_arbol(self, ex_sufijo): # ex_sufijo= la cadena que contiene la expresion sufijo 
        pila = deque()
        
         #procesa la expresion elemento por elemento
        for elemento in ex_sufijo:
            if elemento.isnumeric():  #Un operando
                arbol = Tree() 
                arbol.raiz = Nodo (int(elemento))
                pila.append(arbol)
            else:
                tree_der = pila.pop()
                tree_iz = pila.pop()
                self.combinar_arboles(elemento, tree_iz, tree_der) #combina con el operador
                pila.append(self) #Agrega el arbol restante a la pila
        
        if pila:
            self.raiz = pila.pop().raiz #Arbol raiz del objeto tree
        else: 
            print("Expresion del sufijo incorrecta: Pila vacia")

    #  Implementacion del cap 4 
        

    def __inorden_recur(self, nodo):
        if nodo is not None:
            self.__inorden_recur(nodo.izquierdo)
            print(nodo.dato, end=", ")
            self.__inorden_recur(nodo.derecho)

    def __preorden_recur(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recur(nodo.izquierdo)
            self.__preorden_recur(nodo.derecho)

    def __postorden_recur(self, nodo):
        if nodo is not None:
            self.__postorden_recur(nodo.izquierdo)
            self.__postorden_recur(nodo.derecho)
            print(nodo.dato, end=", ")

    def imprimir_arbol(self):
        if not self.raiz:
            print("Árbol vacío")
            return
        
        cola = deque()
        cola.append(self.raiz)
        
        while cola:
            nivel_actual = []
            num_nodos_nivel = len(cola)
            
            for _ in range(num_nodos_nivel):
                nodo = cola.popleft()
                nivel_actual.append(str(nodo.dato) if nodo else "")

                if nodo:
                    cola.append(nodo.izquierdo)
                    cola.append(nodo.derecho)
            
            print(" ".join(nivel_actual))


ex_sufijo= "53+4*"  
arbol_expresion = Tree()
arbol_expresion.construir_arbol(ex_sufijo)

print("Árbol binario que representa la expresión:")
arbol_expresion.imprimir_arbol()

# arbol = Tree()
# arbol.insertar(5)
# arbol.insertar(3)
# arbol.insertar(7)
# arbol.insertar(2)
# arbol.insertar(4)

# arbol.imprimir_arbol()

# print("\nElemetos del arbol en Inorden:")
# arbol._Tree__inorden_recur(arbol.raiz) 
# print("\nElemetos del arbol en Preorden:")
# arbol._Tree__preorden_recur(arbol.raiz)  
# print("\nElemetos del arbol en Postorden:")
# arbol._Tree__postorden_recur(arbol.raiz)  

# Run your program on at least
# the following expressions:
# a. 91 95 + 15 + 19 + 4 *
# b. B B * A C 4 * * –
# c. 42
# d. A 57 # this should produce an exception
# e. + / # this should produce an exception

