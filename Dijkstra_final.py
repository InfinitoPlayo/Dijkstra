import time
start_time = time.time()

escenario1 = {
    'a': {'d':3},
    'b': {'d':2},
    'c': {'d':5},
    'd': {'h':1},
    'e': {'g':2},
    'f': {'g':4},
    'g': {'e':2,'j':4},
    'h': {'i':7},
    'i': {'j':3},
    'j': {'l':3},
    'k': {'l':2},
    'l': {'m':1,'k':2,'n':5},
    'm': {'l':1},
    'n': {'l':5} 
}

escenario2 = {
    'a':{'b':5},
    'b':{'i':3,'h':6,'c':2},
    'c':{'d':4,'g':3},
    'd':{'e':3,'f':3},
    'e':{'d':3},
    'f':{'d':3},
    'g':{'m':4,'n':8},
    'h':{'l':3,'m':5},
    'i':{'j':4,'l':2},
    'j':{'k':1},
    'k':{'j':1},
    'l':{'t':5, 'm':3},
    'm':{'l':3,'s':6,'l':5},
    'n':{'q':2,'o':2},
    'o':{'p':3},
    'p':{'o':3},
    'q':{'r':5},
    'r':{'q':5},
    's':{'t':4,'x':2,'q':5},
    't':{'v':3,'u':2,'s':4},
    'u':{'t':2},
    'v':{'w':3,'x':1},
    'w':{'z':4,'y':2},
    'x':{'y':3},
    'y':{'w':2},
    'z':{'w':4}
}

escenario3 = {
    'a':{'b':2},
    'b':{'d':1,'g':3,'c':2},
    'c':{'f':5},
    'd':{'e':4,'h':3},
    'e':{'i':1},
    'f':{'k':5,'g':3},
    'g':{'n':6,'h':3,'j':7,'f':3},
    'h':{'p':2,'g':3},
    'i':{'e':1},
    'j':{'m':1,'k':2},
    'k':{'j':2,'l':3},
    'l':{'k':3},
    'm':{'j':1},
    'n':{'r':4,'t':4},
    'o':{'p':2},
    'p':{'o':2,'q':2,'r':5},
    'q':{'s':1},
    'r':{'y':3,'v':2},
    's':{'q':1},
    't':{'v':6,'w':2,'u':3},
    'u':{'t':3},
    'v':{'bb':2},
    'w':{'bb':4,'cc':5,'x':1},
    'x':{'w':1},
    'y':{'z':6,'aa':5},
    'z':{'ee':6},
    'aa':{'ee':4},
    'bb':{'ff':1},
    'cc':{'ff':2,'jj':6,'dd':7},
    'dd':{'cc':7},
    'ee':{'gg':3,'hh':5},
    'ff':{'ii':4},
    'gg':{'pp':2},
    'hh':{'oo':1,'mm':2},
    'ii':{'ll':2,'jj':2},
    'jj':{'kk':4,'ii':2},
    'kk':{'ll':1},
    'll':{'kk':1,'nn':3},
    'mm':{'hh':2},
    'nn':{'ll':3},
    'oo':{'hh':1},
    'pp':{'gg':2}
}


rutas=[]

def Dijkstra(escenario, inicio, meta): 

    menor_costo = {} #Guarda el costo total de la mejor ruta hasta el momento.
    nodo_anterior= {} #Guarda el nodo anterior al actual (para poder recorrer el grafo de manera inversa)
    nodos_restantes = escenario # Para asegurarse de que se recorra todo el grafo
    infinito = 999999 #Quiere decir que no hay ruta posible de un nodo a otro
    ruta_de_nodos = [] #Guarda la ruta optima que se va generando
    r=[]

    for nodo in nodos_restantes: #Se comienza sin saber el camino de menor costo
        menor_costo[nodo] = infinito
    menor_costo[inicio] = 0

    while nodos_restantes: #Mientras queden nodos por recorrer
        
        nodo_menor_costo = None                 
        for nodo in nodos_restantes:    
            if nodo_menor_costo is None:
                nodo_menor_costo = nodo
            elif menor_costo[nodo] < menor_costo[nodo_menor_costo]: #Si el costo del nodo actual es menor 
                nodo_menor_costo = nodo #Actualizar el menor costo
        
        rutas_posibles = escenario[nodo_menor_costo].items()  

        for nodo_hijo, peso in rutas_posibles: #Se recorren los nodos hijos candidatos 
            if peso + menor_costo[nodo_menor_costo] < menor_costo[nodo_hijo]: #Si se encuentra una mejor ruta...
                menor_costo[nodo_hijo] = peso + menor_costo[nodo_menor_costo] #...actualizar valores
                nodo_anterior[nodo_hijo] = nodo_menor_costo
        
        nodos_restantes.pop(nodo_menor_costo) #Se quita el nodo utilizado de los nodos restantes

    nodoActual = meta
    while nodoActual != inicio: #Se recorre desde el nodo final hasta el nodo inicial
        try:
            ruta_de_nodos.insert(0, nodoActual)
            r.insert(0,nodoActual)
            nodoActual = nodo_anterior[nodoActual] #Ir al nodo anterior
        except KeyError: #No hay ruta
            print("No se puede encontrar el camino")
            break   

    ruta_de_nodos.insert(0, inicio)

    if menor_costo[meta] != infinito:
        r.insert(0,inicio+meta)
        r.insert(1,menor_costo[meta])
        print("La ruta a seguir es " + str(ruta_de_nodos) + " , con un costo de " + str(menor_costo[meta]))

    return r

def insertarRuta(ruta):
    rutas.append(ruta)
    print("La lista de rutas actualizada es de: " + str(rutas))
    return rutas

def main():
    #Escenario 1
    insertarRuta(Dijkstra(escenario1, 'a', 'n'))
    print("...")
    #Escenario 2
    insertarRuta(Dijkstra(escenario2, 'a', 'r'))
    print("...")
    #Escenario 3
    insertarRuta(Dijkstra(escenario3, 'a', 'pp'))
    print("--- %s segundos ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()

