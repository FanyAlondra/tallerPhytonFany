import statistics as mate
#def suma(a:int,b:int):
 #   print(f"la suma de {a}+{b} es {a+b}")
def suma(a:int,b=None,c=None):
    if b is None:
        print(f"la suma de {a} = {a}")
    else:
      if c is None:
        print(f"la suma de {a}+{b} = {a+b}")
      else:
        print(f"la suma de {a}+{b}+{c} = {a+b+c}")

def promedioArreglo(lista):
    lista.append(5)
    lista.append(45)
    lista.append(56)
    p=mate.mean(lista)
    print(f"el promedio es {p}")



if __name__ == '__main__':
    suma(10,52)
    suma(23,47,45)
    suma(12)

    lista2=[1,2,3,4,5]
    promedioArreglo(lista2)
    print(lista2)




