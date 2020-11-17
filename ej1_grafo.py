from tda_cola import Cola, cola_vacia, arribo, atencion
from tda_heap import Heap, arribo as arribo_h, heap_vacio, atencion as atencion_h
from tda_heap import cambiar_prioridad, buscar as buscar_h
from tda_pila_dinamico import Pila, apilar, pila_vacia, desapilar
from tda_archivo import abrir, cerrar, guardar, leer
from math import inf


class nodoArista(object):
    """Clase nodo vértice."""

    def __init__(self, info, destino, datos=None):
        """Crea un nodo arista con la información cargada."""
        self.info = info
        self.destino = destino
        self.datos = datos
        self.sig = None


class nodoVertice(object):
    """Clase nodo vértice."""

    def __init__(self, info, datos=None):
        """Crea un nodo vértice con la información cargada."""
        self.info = info
        self.datos = datos
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista() # lista de aristas


class Grafo(object):
    """Clase grafo implementación lista de listas de adyacencia."""

    def __init__(self, dirigido=True):
        """Crea un grafo vacio."""
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


class Arista(object):
    """Clase lista de arsitas implementación sobre lista."""

    def __init__(self):
        """Crea una lista de aristas vacia."""
        self.inicio = None
        self.tamanio = 0


def insertar_vertice(grafo, dato, datos=None):
    """Inserta un vértice al grafo."""
    nodo = nodoVertice(dato, datos)
    if (grafo.inicio is None or grafo.inicio.info > dato):
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info < nodo.info):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1

def insertar_arista(grafo, info, origen, destino, datos):
    """Inserta una arista desde el vértice origen al destino."""
    agregrar_arista(origen.adyacentes, info, destino.info, datos)
    if(not grafo.dirigido):
        agregrar_arista(destino.adyacentes, info, origen.info, datos)

def agregrar_arista(origen, info, destino, datos):
    """Agrega la arista desde el vértice origen al destino."""
    nodo = nodoArista(info, destino, datos)
    if (origen.inicio is None or origen.inicio.destino > destino):
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while(act is not None and act.destino < nodo.destino):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1

def eliminar_vertice(grafo, clave):
    """Elimina un vertice del grafo y lo devuelve si lo encuentra."""
    x = None
    if(grafo.inicio.info == clave):
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if(x is not None):
        aux = grafo.inicio
        while(aux is not None):
            if(aux.adyacentes.inicio is not None):
                quitar_arista(aux.adyacentes, clave)
            aux = aux.sig
        # aca terminar eliminar aristas adyacenes grafo no dirigido
    return x


def quitar_arista(vertice, destino):
    x = None
    if(vertice.adyacentes.inicio.destino == destino):
        x = vertice.adyacentes.inicio.info
        vertice.adyacentes.inicio = vertice.adyacentes.inicio.sig
        vertice.adyacentes.tamanio -= 1
    else:
        ant = vertice.adyacentes.inicio
        act = vertice.adyacentes.inicio.sig
        while(act is not None and act.destino != destino):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            vertice.adyacentes.tamanio -= 1
    return x

def eliminar_arista(grafo, vertice, destino):
    """Elimina una arsita del vertice y lo devuelve si lo encuentra."""
    x = quitar_arista(vertice, destino)    
    
    if(not grafo.dirigido):
        ori = buscar_vertice(grafo, destino)
        quitar_arista(ori, vertice.info)

    return x

def barrido_vertices(grafo):
    """Realiza un barrido de la grafo mostrando sus valores."""
    aux = grafo.inicio
    while(aux is not None):
        print('vertice:', aux.info)
        print('adyacentes:')
        adyacentes(aux)
        aux = aux.sig


def buscar_vertice(grafo, buscado):
    """Devuelve la direccion del elemento buscado."""
    aux = grafo.inicio
    while(aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux

def buscar_arista(vertice, buscado):
    """Devuelve la direccion del elemento buscado."""
    aux = vertice.adyacentes.inicio
    while(aux is not None and aux.destino != buscado):
        aux = aux.sig
    return aux


def tamanio(grafo):
    """Devuelve el numero de vertices en el grafo."""
    return grafo.tamanio


def grafo_vacio(grafo):
    """Devuelve true si el grafo esta vacio."""
    return grafo.inicio is None


def adyacentes(vertice):
    """Muestra los adyacents del vertice."""
    aux = vertice.adyacentes.inicio
    while(aux is not None):
        print(aux.destino, aux.info)
        aux = aux.sig

def marcar_no_visitado(grafo):
    """Marca todos losvertices del grafo como no visitados."""
    aux = grafo.inicio
    while(aux is not None):
        aux.visitado = False
        aux = aux.sig

def barrido_profundidad(grafo, vertice):
    """Barrido en profundidad del grafo."""
    while(vertice is not None):
        if(not vertice.visitado):
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while(adyacentes is not None):
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if(not adyacente.visitado):
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig

def barrido_amplitud(grafo, vertice):
    """Barrido en amplitud del grafo."""
    cola = Cola()
    while(vertice is not None):
        if(not vertice.visitado):
            vertice.visitado = True
            arribo(cola, vertice)
            while(not cola_vacia(cola)):
                nodo = atencion(cola)
                print(nodo.info)
                adyacentes = nodo.adyacentes.inicio
                while(adyacentes is not None):
                    adyacente = buscar_vertice(grafo, adyacentes.destino)
                    if(not adyacente.visitado):
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacentes = adyacentes.sig
        vertice = vertice.sig

def dijkstra(grafo, origen, destino):
    """Algoritmo de Dijkstra para hallar el camino mas corto."""
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while(aux is not None):
        if(aux.info == origen):
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no_visitados, [aux, None], inf)
        aux = aux.sig

    while(not heap_vacio(no_visitados)):
        dato = atencion_h(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while(aux is not None):
            pos = buscar_h(no_visitados, aux.destino)
            if(no_visitados.vector[pos][0] > dato[0] + aux.info):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino

def dijkstra_tiempo(grafo, origen, destino):
    """Algoritmo de Dijkstra para hallar el camino mas corto."""
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while(aux is not None):
        if(aux.info == origen):
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no_visitados, [aux, None], inf)
        aux = aux.sig

    while(not heap_vacio(no_visitados)):
        dato = atencion_h(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while(aux is not None):
            pos = buscar_h(no_visitados, aux.destino)
            if(no_visitados.vector[pos][0] > dato[0] + aux.datos[4]):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.datos[4])
            aux = aux.sig
    return camino

def dijkstra_costo(grafo, origen, destino):
    """Algoritmo de Dijkstra para hallar el camino mas corto."""
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while(aux is not None):
        if(aux.info == origen):
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no_visitados, [aux, None], inf)
        aux = aux.sig

    while(not heap_vacio(no_visitados)):
        dato = atencion_h(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while(aux is not None):
            pos = buscar_h(no_visitados, aux.destino)
            if(no_visitados.vector[pos][0] > dato[0] + aux.datos[3]):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.datos[3])
            aux = aux.sig
    return camino

def prim(grafo):
    """Algoritmo de Prim para hallar el árbol de expansión mínimo."""
    bosque = []
    aristas = Heap(tamanio(grafo) ** 2)
    adyac = grafo.inicio.adyacentes.inicio
    while(adyac is not None):
        arribo_h(aristas, [grafo.inicio.info, adyac.destino], adyac.info)
        adyac = adyac.sig
    while(len(bosque) // 2 < tamanio(grafo) and not heap_vacio(aristas)):
        dato = atencion_h(aristas)
        if(len(bosque) == 0 or ((dato[1][0] not in bosque) ^ (dato[1][1] not in bosque))):
            bosque += dato[1]
            destino = buscar_vertice(grafo, dato[1][1])
            adyac = destino.adyacentes.inicio
            while(adyac is not None):
                arribo_h(aristas, [destino.info, adyac.destino], adyac.info)
                adyac = adyac.sig
    return bosque

def kruskal(grafo):
    """Algoritmo de Kruskal para hallar el árbol de expansión mínimo."""
    bosque = []
    aristas = Heap(tamanio(grafo) ** 2)
    aux = grafo.inicio
    while(aux is not None):
        bosque.append([aux.info])
        adyac = aux.adyacentes.inicio
        while(adyac is not None):
            arribo_h(aristas, [aux.info, adyac.destino], adyac.info)
            adyac = adyac.sig
        aux = aux.sig
    while(len(bosque) > 1 and not heap_vacio(aristas)):
        dato = atencion_h(aristas)
        origen = None
        for elemento in bosque:
            if(dato[1][0] in elemento):
                origen = bosque.pop(bosque.index(elemento))
                break
        destino = None
        for elemento in bosque:
            if(dato[1][1] in elemento):
                destino = bosque.pop(bosque.index(elemento))
                break
        if(origen is not None and destino is not None):
            if(len(origen) > 1 and len(destino) == 1):
                destino = [dato[1][0], dato[1][1]]
            elif(len(destino) > 1 and len(origen) == 1):
                origen = [dato[1][0], dato[1][1]]
            elif(len(destino) > 1 and len(origen) > 1):
                origen += [dato[1][0], dato[1][1]]
            bosque.append(origen + destino)
        else:
            bosque.append(origen)
    return bosque[0]

def existe_paso(grafo, origen, destino):
    """Barrido en profundidad del grafo."""
    resultado = False
    if(not origen.visitado):
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while(vadyacentes is not None and not resultado):
            adyacente = buscar_vertice(grafo, vadyacentes.destino)
            if(adyacente.info == destino.info):
                return True
            elif(not adyacente.visitado):
                resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado

def determinar_arribo(grafo, vertice):
    """Barrido en profundidad del grafo."""
    if(not vertice.visitado):
        vertice.visitado = True
        print(vertice.info)
        adyacentes = vertice.adyacentes.inicio
        while(adyacentes is not None):
            adyacente = buscar_vertice(grafo, adyacentes.destino)
            if(not adyacente.visitado):
                    determinar_arribo(grafo, adyacente)
            adyacentes = adyacentes.sig

def exportar_grafo(grafo, file):
    aux = grafo.inicio
    while(aux is not None):
        elementos = []
        elementos.append(aux.info)
        aux2 = aux.adyacentes.inicio
        while(aux2 is not None):
            elementos.append(aux2.destino)
            aux2 = aux2.sig
        aux = aux.sig
        guardar(file, elementos)


g = Grafo(False)

insertar_vertice(g, 'Argentina', [-32, -58, 5])
insertar_vertice(g, 'China', [-32, -58, 5])
insertar_vertice(g, 'Brasil', [-32, -58, 5])
insertar_vertice(g, 'Tailandia', [-32, -58, 5])
insertar_vertice(g, 'Grecia', [-32, -58, 5])
insertar_vertice(g, 'Alemania', [-32, -58, 5])
insertar_vertice(g, 'Francia', [-32, -58, 5])
insertar_vertice(g, 'Estados Unidos', [-32, -58, 5])
insertar_vertice(g, 'Japón', [-32, -58, 5])
insertar_vertice(g, 'Jamaica', [-32, -58, 5])

#info van a ser los km, destino, datos=None -> va a ser el array con los demas datos
ori = buscar_vertice(g, 'Argentina')
des = buscar_vertice(g, 'China')
insertar_arista(g, 550, ori, des, [8, 20, 'Volar S.A', 370, 12])

des = buscar_vertice(g, 'Brasil')
insertar_arista(g, 30, ori, des, [9, 10, 'Volar S.A', 42, 1])

des = buscar_vertice(g, 'Tailandia')
insertar_arista(g, 900, ori, des, [5, 19, 'Volar S.A', 300, 14])

ori = buscar_vertice(g, 'Grecia')
des = buscar_vertice(g, 'Argentina')
insertar_arista(g, 230, ori, des, [3, 6, 'Prueba S.A', 185, 3])

des = buscar_vertice(g, 'Brasil')
insertar_arista(g, 180, ori, des, [4, 8, 'Prueba S.A', 170, 4])

des = buscar_vertice(g, 'Estados Unidos')
insertar_arista(g, 220, ori, des, [6, 10, 'Prueba S.A', 170, 4])

ori = buscar_vertice(g, 'Brasil')
des = buscar_vertice(g, 'Alemania')
insertar_arista(g, 300, ori, des, [12, 16, 'Volar S.A', 150, 4])

ori = buscar_vertice(g, 'Alemania')
des = buscar_vertice(g, 'Francia')
insertar_arista(g, 70, ori, des, [12, 12.30, 'Volar S.A', 50, 0.30])

ori = buscar_vertice(g, 'Francia')
des = buscar_vertice(g, 'Tailandia')
insertar_arista(g, 95, ori, des, [22, 24, 'Volar S.A', 450, 2])

file = abrir('ej1_grafos.txt')
exportar_grafo(g, file)
pos = 0
while(pos < len(file)):
     persona = leer(file, pos)
     pos += 1
     print(persona)
cerrar(file)
a = input()

camino_mas_corto = dijkstra(g, 'Argentina', 'Tailandia')
fin = 'Tailandia'
peso_total = None
while(not pila_vacia(camino_mas_corto)):
    dato = desapilar(camino_mas_corto)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        print(dato[1][0].info)
        fin = dato[1][1]
print('KM total:', peso_total)
print()

camino_mas_corto = dijkstra_tiempo(g, 'Argentina', 'Tailandia')
fin = 'Tailandia'
peso_total = None
while(not pila_vacia(camino_mas_corto)):
    dato = desapilar(camino_mas_corto)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        print(dato[1][0].info)
        fin = dato[1][1]
print('Tiempo total:', peso_total)
print()

camino_mas_corto = dijkstra_costo(g, 'Argentina', 'Tailandia')
fin = 'Tailandia'
peso_total = None
while(not pila_vacia(camino_mas_corto)):
    dato = desapilar(camino_mas_corto)
    if(peso_total is None and fin == dato[1][0].info):
        peso_total = dato[0]
    if(fin == dato[1][0].info):
        print(dato[1][0].info)
        fin = dato[1][1]
print('Costo total:', peso_total)
print() 
 
print('Aeropuertos a los que se puede arribar desde Grecia')
buscado = buscar_vertice(g, 'Grecia')

if (buscado.adyacentes.inicio is not None):
    determinar_arribo(g, buscado)

