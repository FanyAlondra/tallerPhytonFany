import json
import sys

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

def extrae():
    with open ("edad_bd.json", "r", encoding="UTF-8") as archivo:
        datos= json.load(archivo)

    for persona in datos["persona"]:
        yield (persona["id"],persona ["nombre"],persona["edad"],persona["RFC"])


if __name__ == '__main__':
    i=1
    for id,nombre,edad,RFC in extrae():
        match i:
            case 1:
                sys.stdout.write(MAGENTA)
            case 2:
                sys.stdout.write(BLUE)
            case 3:
                sys.stdout.write(CYAN)
            case _:
                sys.stdout.write(RESET)

        print("-" *30)
        print(f"id:{id} ")
        print(f" nombre: {nombre}")
        print(f"edad: {edad}")
        print(f"RFC: {RFC}")

        if int(edad) >= 18:
            print("mayor de edad")
        else:
            print("menor de edad")
            print("-" * 30)

            sys.stdout.write(RESET)
            i+=1
