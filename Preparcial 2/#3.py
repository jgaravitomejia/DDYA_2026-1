def knight_in_war_grid(R, C, M, N, aguas):
    # Creamos el campo de batalla: 0 es vacio, -1 es agua
    campo = [[0 for _ in range(C)] for _ in range(R)]
    for r_w, c_w in aguas:
        campo[r_w][c_w] = -1
        
    # Definimos los saltos UNICOS (M,N)
    # El set() elimina duplicados si M == N o si alguno es 0
    saltos = set([
        (M, N), (M, -N), (-M, N), (-M, -N),
        (N, M), (N, -M), (-N, M), (-N, -M)
    ])
    
    visitados = [[False for _ in range(C)] for _ in range(R)]
    evens = 0
    odds = 0
    
    # BFS para encontrar celdas alcanzables
    cola = [(0, 0)]
    visitados[0][0] = True
    
    # Mientras haya celdas por explorar
    indice = 0
    while indice < len(cola):
        r_act, c_act = cola[indice]
        indice += 1
        
        # Para la celda actual, contamos cuantos vecinos pueden saltar a ella
        k_i = 0
        for dr, dc in saltos:
            nr, nc = r_act + dr, c_act + dc
            
            # Verificamos si el salto cae dentro del tablero y no es agua
            if 0 <= nr < R and 0 <= nc < C and campo[nr][nc] != -1:
                k_i += 1
                
                # Si el vecino es accesible y no lo hemos visitado, a la cola
                if not visitados[nr][nc]:
                    visitados[nr][nc] = True
                    cola.append((nr, nc))
        
        # Clasificamos segun la paridad de k_i
        if k_i % 2 == 0:
            evens += 1
        else:
            odds += 1
            
    return evens, odds

# --- BLOQUE DE PRUEBA CON TUS ENTRADAS ---

    # Caso 1 del documento: 3 3 2 1, 0 aguas
print("Caso 1 (3x3, M=2, N=1):")
e1, o1 = knight_in_war_grid(3, 3, 2, 1, [])
print(f"Resultado -> Evens: {e1}, Odds: {o1}") # Debe dar 5 0

    # Caso 2 del documento: 4 4 1 2, 2 aguas en (3,3) y (1,1)
print("\nCaso 2 (4x4, M=1, N=2, con Agua):")
e2, o2 = knight_in_war_grid(4, 4, 1, 2, [(3, 3), (1, 1)])
print(f"Resultado -> Evens: {e2}, Odds: {o2}") # Debe dar 4 10