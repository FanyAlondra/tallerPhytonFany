if __name__ == '__main__':
        nombre1 = input("dame un nombre: ")
        nombre2 = input("dame otro nombre: ")

        if len(nombre1) > len(nombre2):
            print(f"El nombre con más letras es: {nombre1}")
        elif len(nombre2) > len(nombre1):
            print(f"El nombre con más letras es: {nombre2}")
        else:
            print("tienen la misma cantidad de letras ")


