if __name__ == '__main__':
    x = int(input("ingresa un numero: "))
    y = int(input("ingresa otro numero : "))

    i: int = 1
    mult: int = 1

    while i<y:
        mult=x*y
        i+=1
    print(f"el resultado de {x} y {y} ={mult}")