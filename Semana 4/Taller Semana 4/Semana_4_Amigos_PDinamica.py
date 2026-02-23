def formas_amigos(n, memo = None): 
#memo (diccionario) para cuardar las formas, empieza vacia
    if memo is None:
        memo = {} #para que memo sea un diccionario vacio  {}
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n==2: 
        return 2
     #casos base  
    if n in memo:
        return memo[n]
    #si ya se calculo, retornar
    #funcion de recurrencia en caso de no estar calculado 
    resultado = formas_amigos(n-1,memo) + (n-1)* formas_amigos(n-2,memo)
    memo[n]= resultado #se guarda el resultado para n
    return resultado
    
n = int(input("Ingrese el número de amigos:"))
print("Para", n, "amigos, hay", formas_amigos(n), "formas posibles de estar solor o emparejados.")
