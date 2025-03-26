def calcular_area(rectangulo:tuple [int,int])->int:
    largo, ancho= rectangulo
    return largo* ancho

def cuadrado(rectangulo:tuple[int,int])-> tuple [int, int]:
    largo, ancho=rectangulo
    largo=largo*ancho
    return (largo,ancho)


if __name__ == '__main__':

    #crea la tupla
    dimensiones =(10, 5)

    #llamar la funcion con la tupla
    area= calcular_area(dimensiones)
    print(f"el area del rectangulo es: {area}mts. cuadrados")
