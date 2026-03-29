#2

def recorrer_arbol(raiz):
    preorden = []

    # Recorrido Preorden (Raíz - Izquierda - Derecha)
    def pre_order(raiz):
        if raiz is not None:
            preorden.append(raiz[0])  # Agregar el valor del nodo
            pre_order(raiz[1])  # Subárbol izquierdo
            pre_order(raiz[2])  # Subárbol derecho

    # Realizar el recorrido preorden
    pre_order(raiz)
    
    return preorden

# Definición del árbol
arbol = (1, None, (2, None, (5, (3, None, (4, None, None)), (6, None, None))))

# Llamada a la función para obtener el recorrido preorden
preorden = recorrer_arbol(arbol)

# Imprimir solo el recorrido Preorden
print("Preorden:")
print(" ".join(map(str, preorden)))
