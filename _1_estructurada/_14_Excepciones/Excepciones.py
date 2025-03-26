if __name__ == '__main__':
    try:
        #codigo que puede causar una excepcion
        numero=int(input("introduce un numero: "))
        resultado = 10 / numero
    except ValueError:
        # mensaje de la excepcion si se introduce un valor no valido
        print("¡Error¡ Debes introducir un numero entero. ")
    except ZeroDivisionError:
        # manejo de la excepcion si se intenta dividir por 0
        print("¡Error¡ No se puede diidir entre cero. ")
    else:
        # se ejecuta si no hubo excepciones
        print("el resultado es: ", resultado)
    finally:
        # se ejecuta siempre, haya o no habido excepciones
        print("fin del programa. ")
