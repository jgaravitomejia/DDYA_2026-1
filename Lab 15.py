import networkx as nx
import matplotlib.pyplot as plt
import heapq


# GRAFOS


def obtener_grafo(opcion):

    # GRAFO 1

    if opcion == 1:

        G = nx.DiGraph()

        edges = [
            (0,1,5),
            (0,2,2),
            (2,1,8),
            (1,3,4),
            (1,4,2),
            (2,4,7),
            (3,4,6),
            (3,5,3),
            (4,5,1)
        ]

        G.add_weighted_edges_from(edges)

        pos = {
            0:(0,1),
            1:(2,2),
            2:(2,0),
            3:(4,2),
            4:(4,0),
            5:(6,1)
        }

        return G, pos, 0, 5

    
# GRAFO 2


    elif opcion == 2:

        G = nx.DiGraph()

        edges = [

        (0,1,10),

        (1,2,20),

        (3,1,1),

        (2,3,1),

        (2,4,30)

        ]

        G.add_weighted_edges_from(edges)

        pos = {

        0:(0,1),

        1:(2,2),

        3:(2,0),

        2:(4,2),

        4:(6,1)

        }

        return G, pos, 0, 4

    # GRAFO 3

    elif opcion == 3:

        G = nx.DiGraph()

        edges = [
            (0,2,2),
            (0,1,2),
            (1,2,2),
            (2,3,2),
            (3,1,-1),
            (2,4,2),
            (3,4,2)
        ]

        G.add_weighted_edges_from(edges)

        pos = {
            0:(0,1),
            1:(2,0),
            2:(2,2),
            3:(4,0),
            4:(6,1)
        }

        return G, pos, 0, 4


# DIBUJAR GRAFO

def dibujar_grafo(G, pos, titulo="", edges_rojas=[]):

    plt.figure(figsize=(9,6))

    colores = []

    for edge in G.edges():

        if edge in edges_rojas:
            colores.append("red")
        else:
            colores.append("gray")

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        node_size=1800,
        edge_color=colores,
        width=4,
        arrows=True,
        font_size=14
    )

    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=labels,
        font_size=13
    )

    plt.title(titulo, fontsize=16)

    plt.show()



# RECONSTRUIR CAMINO


def reconstruir_camino(pred, inicio, fin):

    camino = []

    actual = fin

    while actual != inicio:

        if actual not in pred:
            return []

        anterior = pred[actual]

        camino.append((anterior, actual))

        actual = anterior

    camino.reverse()

    return camino



# BELLMAN FORD


def bellman_ford(G, pos, inicio, fin):

    print("\n===== BELLMAN FORD =====\n")

    # DISTANCIAS

    dist = {v: float('inf') for v in G.nodes()}

    dist[inicio] = 0

    # PREDECESORES

    pred = {}

    # ITERACIONES

    for i in range(len(G.nodes()) - 1):

        print(f"\nITERACION {i+1}")

        cambio = False

        for u, v, w in G.edges(data='weight'):

            # RELAJACION

            if dist[u] != float('inf') and dist[u] + w < dist[v]:

                dist[v] = dist[u] + w

                pred[v] = u

                cambio = True

                
                # CONSTRUIR GRAFO ACTUAL
                

                caminos_actuales = []

                for nodo in pred:

                    caminos_actuales.append(
                        (pred[nodo], nodo)
                    )

                print(f"\nRelajando ({u}->{v})")
                print("Distancias:", dist)

                
                # DIBUJAR
                

                dibujar_grafo(
                    G,
                    pos,
                    f"Bellman-Ford Iteracion {i+1}",
                    caminos_actuales
                )

        if not cambio:
            break

    # VERIFICAR CICLOS NEGATIVOS

    for u, v, w in G.edges(data='weight'):

        if dist[u] + w < dist[v]:

            print("\nExiste ciclo negativo")
            return

    # CAMINO FINAL

    camino_final = reconstruir_camino(
        pred,
        inicio,
        fin
    )

    print("\n================================")
    print("DISTANCIAS FINALES")
    print("================================")

    print(dist)

    print("\n================================")
    print("CAMINO MINIMO FINAL")
    print("================================")

    print(camino_final)

    # DIBUJO FINAL

    dibujar_grafo(
        G,
        pos,
        "Bellman-Ford FINAL",
        camino_final
    )


#DIJKSTRA


def dijkstra(G, pos, inicio, fin):

    print("\n===== DIJKSTRA =====\n")

    # DISTANCIAS

    dist = {v: float('inf') for v in G.nodes()}
    dist[inicio] = 0

    # PREDECESORES

    pred = {}

    # PRIORITY QUEUE

    pq = [(0, inicio)]

    visitados = set()

    # ALGORITMO

    while pq:

        distancia_actual, u = heapq.heappop(pq)

        if u in visitados:
            continue

        visitados.add(u)

        # VECINOS

        for v in G.neighbors(u):

            peso = G[u][v]['weight']

            nueva = dist[u] + peso

            # RELAJACION

            if nueva < dist[v]:

                dist[v] = nueva

                pred[v] = u

                heapq.heappush(
                    pq,
                    (nueva, v)
                )

                
                # RECONSTRUIR EL ARBOL VISUAL
                

                caminos_actuales = []

                for nodo in pred:

                    caminos_actuales.append(
                        (pred[nodo], nodo)
                    )

                print(f"\nActualizando ({u}->{v})")
                print("Distancias:", dist)

                
                # DIBUJAR PASO A PASO
                

                dibujar_grafo(
                    G,
                    pos,
                    "Dijkstra Paso a Paso",
                    caminos_actuales
                )

    # CAMINO FINAL

    camino_final = reconstruir_camino(
        pred,
        inicio,
        fin
    )

    print("\n================================")
    print("DISTANCIAS FINALES")
    print("================================")

    print(dist)

    print("\n================================")
    print("CAMINO MINIMO FINAL")
    print("================================")

    print(camino_final)

    # DIBUJO FINAL

    dibujar_grafo(
        G,
        pos,
        "Dijkstra FINAL",
        camino_final
    )


# KRUSKAL (NO DIRIGIDO)


def kruskal(G_original, pos):

    print("\n===== KRUSKAL =====\n")

    
    # SOLO AQUI se vuelve no dirigido
    

    G = G_original.to_undirected()

    parent = {}
    rank = {}

    

    def make_set(v):

        parent[v] = v
        rank[v] = 0

    

    def find(v):

        if parent[v] != v:
            parent[v] = find(parent[v])

        return parent[v]

    

    def union(a, b):

        raizA = find(a)
        raizB = find(b)

        if raizA != raizB:

            if rank[raizA] > rank[raizB]:

                parent[raizB] = raizA

            else:

                parent[raizA] = raizB

                if rank[raizA] == rank[raizB]:
                    rank[raizB] += 1

    

    for node in G.nodes():
        make_set(node)

    edges = list(G.edges(data=True))

    edges.sort(key=lambda x: x[2]['weight'])

    mst_edges = []

    
    # ALGORITMO
    

    for u, v, data in edges:

        if find(u) != find(v):

            union(u, v)

            mst_edges.append((u, v))

            print(f"\nAgregando ({u},{v})")

            dibujar_grafo(
                G,
                pos,
                "Kruskal Paso a Paso",
                mst_edges
            )

    print("\nMST FINAL:")
    print(mst_edges)

    dibujar_grafo(
        G,
        pos,
        "Kruskal FINAL",
        mst_edges
    )


# PRIM 


def prim(G, pos):

    print("\n===== PRIM =====\n")

    inicio = list(G.nodes())[0]

    visitados = set([inicio])

    pq = []

    mst_edges = []

    
    # ARISTAS INICIALES
    

    for vecino in G.neighbors(inicio):

        peso = G[inicio][vecino]['weight']

        heapq.heappush(
            pq,
            (peso, inicio, vecino)
        )

    
   
    while pq:

        peso, u, v = heapq.heappop(pq)

        if v not in visitados:

            visitados.add(v)

            mst_edges.append((u, v))

            print(f"\nAgregando ({u}->{v}) peso={peso}")

            dibujar_grafo(
                G,
                pos,
                "Prim Paso a Paso",
                mst_edges
            )

            
            # NUEVAS ARISTAS
            

            for vecino in G.neighbors(v):

                if vecino not in visitados:

                    nuevo_peso = G[v][vecino]['weight']

                    heapq.heappush(
                        pq,
                        (nuevo_peso, v, vecino)
                    )

    print("\nMST FINAL:")
    print(mst_edges)

    dibujar_grafo(
        G,
        pos,
        "Prim FINAL",
        mst_edges
    )

# MENU PRINCIPAL

while True:

    print("\n===================================")
    print("          MENU PRINCIPAL")
    print("===================================")

    print("1. Grafo 1")
    print("2. Grafo 2")
    print("3. Grafo 3")
    print("0. Salir")

    opcion_grafo = int(input("\nSeleccione grafo: "))

    if opcion_grafo == 0:
        break

    G, pos, inicio, fin = obtener_grafo(opcion_grafo)

    # MENU INTERNO DEL GRAFO

    while True:

        print("\n===================================")
        print(f"        GRAFO {opcion_grafo}")
        print("===================================")

        print("1. Ver grafo")
        print("2. Bellman-Ford")
        print("3. Dijkstra")
        print("4. Kruskal")
        print("5. Prim")
        print("0. Volver al menu principal")

        opcion_algoritmo = int(input("\nSeleccione opcion: "))


        if opcion_algoritmo == 0:
            break

        elif opcion_algoritmo == 1:

            dibujar_grafo(
                G,
                pos,
                f"Grafo {opcion_grafo}"
            )

        elif opcion_algoritmo == 2:

            bellman_ford(
                G,
                pos,
                inicio,
                fin
            )

        elif opcion_algoritmo == 3:

            dijkstra(
                G,
                pos,
                inicio,
                fin
            )

        elif opcion_algoritmo == 4:

            kruskal(
                G,
                pos
            )

        elif opcion_algoritmo == 5:

            prim(
                G,
                pos
            )

        else:
            print("\nOpcion invalida")