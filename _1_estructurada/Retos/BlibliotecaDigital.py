#desarrollar un programa en pyton que utilice
#la poo para registrar un libro(ISBN,TITULO Y AUTOR
#Los atributos deben estar en pribado
#debes tener un constructor par el registro
#debes tener solo getters de cada atributo

#en otra clase debera registrar una coleccion de libros
#en esta clase debes tener add,delete y show
# Clase Libro

class Libro:
    def __init__(self, titulo, autor, anio):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_anio(self):
        return self.__anio


class ColeccionLibros:
    def __init__(self):
        self.__libros = []

    def add(self, libro):
        self.__libros.append(libro)
        print(f" Libro agregado: '{libro.get_titulo()}'")

    def delete(self, titulo):
        for libro in self.__libros:
            if libro.get_titulo() == titulo:
                self.__libros.remove(libro)
                print(f"🗑 Libro eliminado: '{titulo}'")
                return
        print(f"Libro '{titulo}' no encontrado en la colección.")

    def show(self):
        if not self.__libros:
            print(" La colección está vacía.")
        else:
            print("\nLista de libros:")
            for i, libro in enumerate(self.__libros, start=1):
                print(f"{i}. Título: {libro.get_titulo()}, Autor: {libro.get_autor()}, Año: {libro.get_anio()}")


if __name__ == "__main__":
    coleccion = ColeccionLibros()

    libro1 = Libro("El diario de ana frank", "Ana frank", 1944)
    libro2 = Libro("Bajo la misma estrella", "jonh green", 2012)
    libro3 = Libro("Romper el circulo", " Colleen Hoover", 2016)
    libro4 = Libro("Yo antes de ti", " Jojo Moyes", 2012)
    libro5 = Libro("A dos metros de ti", " Rachael Lippincott", 2014)

    coleccion.add(libro1)
    coleccion.add(libro2)
    coleccion.add(libro3)
    coleccion.add(libro4)
    coleccion.add(libro5)

    coleccion.show()

    coleccion.delete("2000")

    coleccion.show()