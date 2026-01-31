def num_entero():
    num=int(input("Ingresar numero entero: "))
    divisores=[]
    primo=True
    num_f=[0,1]
    if num==0 or num==1:
        fibonacci=True
    else:
        while num_f[-1]<num:
            nuevo_num=num_f[-1]+num_f[-2]
            num_f.append(nuevo_num)
        if num==num_f[-1]:
            fibonacci=True
        else:
            fibonacci=False
    if fibonacci:
        print("El numero es fibonacci")
    if num<2:
        primo=False
    else:
        limite=int(num**0.5)+1
        for i in range(1,limite):
            if num%i==0:
                divisores.append(i)
        if len(divisores)>2:
            primo=False
    if primo:
        print("El numero es primo")
    if num>0:
        print("El numero es positivo")
    elif num<0:
        print("El numero es negativo")
    else:
        print("El numero es cero")
    print("Fin del programa")
num_entero()
