def suma_dyq(notas, inicio, fin, memoria):
    # Verificamos si ya hemos calculado la suma para este rango 
    if (inicio, fin) in memoria:
        return memoria[(inicio, fin)]
    # Caso base: si hay solo un elemento
    if inicio == fin:
        return notas[inicio]
    # Caso recursivo: dividimos el problema en dos partes y sumamos
    mitad = (inicio + fin) // 2
    suma_izq = suma_dyq(notas, inicio, mitad, memoria)
    suma_der = suma_dyq(notas, mitad + 1, fin, memoria)
    # Almacenamos el resultado en el diccionario para que no lo calculemos de nuevo
    memoria[(inicio, fin)] = suma_izq + suma_der
    return suma_izq + suma_der

def main():
    nombres = []
    notas = []

    print("Ejemplo de formato correcto: Juan 4.5 Maria 3.0")
    estudiantes = input("Ingresa los nombres y notas de los estudiantes: ")

    # TEST 10: Certificacion de datos
    if (" " not in estudiantes.strip()) or any(s in estudiantes for s in [",", "-", "/", "_"]):
        print("Error: Formato inválido. Debes usar espacios y evitar comas, guiones u otros caracteres de separacion.")
        return

    lista = estudiantes.split()

    # TEST 1: Entrada vacía
    if not lista:
        print("Error: No se ingresaron datos.")
        return

    # TEST 2: Datos impares (Falta una nota o un nombre)
    if len(lista) % 2 != 0:
        print("Error: Cada nombre debe tener una nota correspondiente.")
        return
   
        
    for i in range(0, len(lista), 2):
        nom = lista[i]
        no_str = lista[i + 1]

        # TEST 3: El nombre no debería ser solo números
        if nom.replace('.', '', 1).isdigit():
            print("El orden de los datos esta invertido, debe ser estudiante nota.")
            return
         # TEST 10: Caracteres no permitidos en el nombre
        if not nom.isalpha():
            print(f"Error: El nombre '{nom}' no es válido. Solo se permiten letras (sin números ni símbolos).")
            return
        # TEST 4: La nota debe ser un número válido
        try:
            valor_nota = float(no_str)
        except ValueError:
            print(f"Error: '{no_str}' no es una nota válida, deben ingersarse notas numericas.")
            return
        
        # TEST 5: Rango de nota (0.0 a 5.0)
        if valor_nota < 0 or valor_nota > 5:
            print(f"Error: La nota de {nom} ({valor_nota}) está fuera del rango 0-5.")
            return

        nombres.append(nom)
        notas.append(round(valor_nota, 2))

    memoria = {} # Diccionario para almacenar resultados anteriores

    # TEST 6: Nombres duplicados o iguales
    if len(nombres) != len(set(nombres)):
        print("\nAviso: Se detectaron nombres repetidos en la lista.\n")

    # Solicitamos al usuario el rango de estudiantes para el cálculo del promedio
    # Usamos un try para capturar errores de escritura en los índices
    try:
        # TEST 7: Índices deben ser enteros
        inicio_p = input("Ingrese el indice de inicio para el calculo (por ejemplo, 1): ")
        fin_p = input(f"Ingrese el indice de fin para el calculo (por ejemplo, {len(notas)}): ")
        
        inicio = int(inicio_p) - 1
        fin = int(fin_p) - 1

        # TEST 8: Índice de inicio negativo
        if inicio < 0:
            print("Error: El índice de inicio no puede ser menor a 1.")
            return

        if fin >= len(notas):
            print(f"Error: El índice de fin no puede ser mayor a {len(notas)}.")
            return

        # TEST 9: Orden lógico de los índices
        if inicio > fin:
            print("Error: El indice inicial no puede ser mayor al final.")
            return

         # Calculamos la suma del rango seleccionado
        suma = suma_dyq(notas, inicio, fin, memoria) 
        n = fin - inicio + 1 
        prom = suma / n 
        
        print("Promedio de las notas de los estudiantes: " + str(prom))
        print("\nEstudiantes que aprueban: ")
        
        # Mostrar los estudiantes que superaron el promedio
        for i in range(inicio, fin + 1):
            if notas[i] >= prom:
                print(nombres[i] + " con " + str(notas[i]))

    except ValueError:
        print("Error: Debes ingresar números enteros para los índices.")


main()