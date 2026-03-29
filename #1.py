# Implementacion de Cola usando dos Pilas (Queue using two Stacks)
# Sin tildes ni caracteres especiales para maxima compatibilidad

def procesar_cola(consultas):
    pila_entrada = []
    pila_salida = []

    # Funciones basicas de Pila
    def push(pila, elemento):
        pila.append(elemento)

    def pop(pila):
        if len(pila) > 0:
            return pila.pop()
        return None

    # Procesamos cada comando de la lista
    for query in consultas:
        partes = query.split()
        tipo = partes[0]

        if tipo == "1":
            # ENQUEUE: Agregar al final
            valor = partes[1]
            push(pila_entrada, valor)
        else:
            # Si la pila de salida esta vacia, movemos todo de entrada a salida
            # Esto invierte el orden para cumplir el principio FIFO
            if len(pila_salida) == 0:
                while len(pila_entrada) > 0:
                    dato_temp = pop(pila_entrada)
                    push(pila_salida, dato_temp)
            
            if tipo == "2":
                # DEQUEUE: Eliminar el frente
                pop(pila_salida)
            elif tipo == "3":
                # PRINT: Mostrar el frente
                if len(pila_salida) > 0:
                    print(pila_salida[-1])

# --- BLOQUE DE EJECUCION CON EJEMPLOS ---

# Ejemplo 1: Operacion basica (Debe imprimir 10)
print("Ejecutando Ejemplo 1:")
ejemplo1 = ["1 10", "1 20", "3"]
procesar_cola(ejemplo1)

    # Ejemplo 2: Efecto FIFO con eliminacion (Debe imprimir 14)
print("\nEjecutando Ejemplo 2:")
ejemplo2 = ["1 42", "1 14", "2", "1 28", "3"]
procesar_cola(ejemplo2)

    # Ejemplo 3: Vaciado completo y recarga (Debe imprimir 100)
print("\nEjecutando Ejemplo 3:")
ejemplo3 = ["1 5", "1 10", "2", "2", "1 100", "3"]
procesar_cola(ejemplo3)