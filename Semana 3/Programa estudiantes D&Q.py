def suma_dyq(notas, inicio, fin):
    if inicio == fin:
        return notas[inicio]
    mitad = (inicio + fin) // 2
    suma_izq = suma_dyq(notas, inicio, mitad)
    suma_der = suma_dyq(notas, mitad + 1, fin)
    return suma_izq + suma_der


def main():
    nombres = []
    notas = []
    estudiantes = input("Ingresa los nombres y notas de los estudiantes: ")
    lista = estudiantes.split()

    for i in range(0, len(lista), 2):
        nom = lista[i]
        no = lista[i + 1]
        nombres.append(nom)
        notas.append(round(float(no), 2))

    suma = suma_dyq(notas, 0, len(notas) - 1)
    n = len(notas)
    prom = suma / n

    for i in range(len(notas)):
        if notas[i] >= prom:
            print(nombres[i])
main()