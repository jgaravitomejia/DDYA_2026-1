#Juan Sebsastian Garavito
def main():
    suma=0
    nombres=[]
    notas=[]
    estudiantes=input("Ingresa los nombres y notas de los estudiantes: ")
    lista=estudiantes.split()
    for i in range(0,len(lista),2):
        nom=lista[i]
        no=lista[i+1]
        nombres.append(nom)
        notas.append(round(float(no), 2))
    for i in range(len(notas)):  
        suma=suma+notas[i]
    n=len(notas)
    prom=suma/n
    for i in range(len(notas)):
        if notas[i]>=prom:
            print(nombres[i])

main()
