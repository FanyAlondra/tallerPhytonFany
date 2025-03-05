if __name__ == '__main__':
    x=int (input("ingresa un numero: "))
    y=int (input("ingresa la potencia: "))

    i:int=1
    pot:int=1

    while i<y:
        pot=pot*x
        i+=1
        print(f"el resultado de {x}^{y}={pot}")
